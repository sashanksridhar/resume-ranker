import os
from utils import extract_text_from_pdf, extract_text_from_docx, extract_text_from_pdf_stream, extract_text_from_docx_stream, allowed_file
from flask import Flask, Response, request, jsonify
from werkzeug.utils import secure_filename
from extraction import extract_criteria, find_summary
from flask_swagger_ui import get_swaggerui_blueprint
from match import find_matches
import pandas as pd
from candidate import find_candidate

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Swagger UI Configuration
SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"  # JSON file containing API documentation
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Task 1 - Extract Ranking Criteria from Job Description
@app.route("/extract-criteria", methods=["POST"])
def extract_criterias():
    
    # Check if file is uploaded
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    # Extract file from request
    file = request.files["file"]

    # Ignore malformed files
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):

        # Save file locally
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(filepath)
        elif filename.endswith(".docx"):
            text = extract_text_from_docx(filepath)
        else:
            return jsonify({"error": "Unsupported file format"}), 400
        
        criteria = extract_criteria(text)

        return jsonify({"criteria": criteria})

    return jsonify({"error": "Invalid file format"}), 400

# Task 2 - Score Resumes Against Extracted Criteria
@app.route("/score-resumes", methods=["POST"])
def score_resumes():

    # Check if file is uploaded and the criteria to rank should be present
    if "files" not in request.files or "criteria" not in request.form:
        return jsonify({"error": "Missing files or criteria"}), 400

    criterias = str(request.form["criteria"])
    criteria_list = []

    # Headers for result csv
    summary_list = []
    summary_list.append("Candidate Name")

    for item in criterias.split("\","):
        criteria_list.append(item.strip())

        # Find summary to add as header in csv file
        summary_list.append(find_summary(criteria_list[-1]))

    if not isinstance(criteria_list, list):
        raise ValueError("Criteria must be a list of strings")

    files = request.files.getlist("files")

    summary_list.append("Total Score")

    # Result csv
    results = pd.DataFrame(columns=summary_list)

    for ind, file in enumerate(files):
        if file.filename.endswith(".pdf"):
            text = extract_text_from_pdf_stream(file)
            
        elif file.filename.endswith(".docx"):
            text = extract_text_from_docx_stream(file)
        else:
            continue
        
        # Step 1 - Find candidate name from resume
        candidate_name = find_candidate(text)
        data_candidate = []
        data_candidate.append(candidate_name)

        # Step 2 - Find the score between 0 and 5 for each skill
        matched = find_matches(criteria_list, summary_list, text)

        # Step 3 - Add up the scores for the total score
        total = 0
        for i in matched:
            total+= int(i)
        matched.append(str(total))

        data_candidate.extend(matched)

        new_row = pd.DataFrame([data_candidate], columns=summary_list)
        
        results = pd.concat([results, new_row], ignore_index=True)

    csv_data = results.to_csv(index=False)

    # Create response with CSV MIME type
    response = Response(csv_data, mimetype="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=data.csv"

    return response


if __name__ == "__main__":
    app.run(debug=True)
