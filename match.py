from openai import OpenAI
import httpx
import json

# Find resume score for all the skills needed
def find_matches(criteria_list, summary_list, text):
    result = []

    for ind, criteria in enumerate(criteria_list):
        transport = httpx.HTTPTransport(verify=False)

        client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
        http_client=httpx.Client(transport=transport)
        )

        user_msg = f'''
    Given a resume of a candidate and a skill criteria, evaluate the resume based on the criteria and return a score between 0 and 5.

    Skill criteria: {criteria}

    ----

    Resume: {text}

    Return only a score between 0 and 5 based on the presence and relevance of the criteria in the resume.

    '''

        completion = client.chat.completions.create(
    model="google/gemini-2.0-flash-lite-preview-02-05:free",
    messages=[
        {
            "role": "system",
            "content": "You are a HR Assistant tasked with identifying the presence and relevance of a given skill criteria in a given resume."
        },
        {
        "role": "user",
        "content": user_msg
        }
    ],
    response_format = {
"type": "json_schema",
"json_schema": {
    "name": "rating",
    "strict": True,
    "schema": {
    "type": "object",
    "properties": {
    "rating": {
        "type": "integer",
        
    }
}
    },
    "required": ["rating"],
    }

}
    )

        dat = json.loads(completion.choices[0].message.content)
        rating = dat.get("rating", 0)
        result.append(rating)
    return result