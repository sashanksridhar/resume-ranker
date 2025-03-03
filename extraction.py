from openai import OpenAI
import httpx

# Extract Ranking Criteria from Job Description
def extract_criteria(text):

    transport = httpx.HTTPTransport(verify=False)

    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    http_client=httpx.Client(transport=transport)
    )

    user_msg = f'''
Given a job description, identify the key criteria within the description.
Some examples of key criteria are:
    1. "Must have certification XYZ"
    2. "5+ years of experience in Python development"
    3. "Strong background in Machine Learning"

Job description: {text}

Extract the criterias and return as a Json with the format specified.

'''

    completion = client.chat.completions.create(
model="google/gemini-2.0-flash-lite-preview-02-05:free",
messages=[
    {
        "role": "system",
        "content": "You are a HR Assistant tasked with identifying key criteria from a given job description"
    },
    {
    "role": "user",
    "content": user_msg
    }
],
response_format = {
"type": "json_schema",
"json_schema": {
    "name": "criteria",
    "strict": True,
    "schema": {
    "type": "object",
    "properties": {
    "criteria": {
        "type": "array",
        "items": {
        "type": "string"
        }
    }
}
    },
    "required": ["criteria"],
    }

}
)
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

# Task 2 - Get the summary of the skills
def find_summary(text):
    transport = httpx.HTTPTransport(verify=False)

    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    http_client=httpx.Client(transport=transport)
    )

    user_msg = f'''
Given a particular text of a required skill condition, extract the main skill alone.

E.g. "Must have certification XYZ" -> "Certification XYZ",
    "5+ years of experience in Python development" -> "Python Development",
    "Strong background in Machine Learning" -> "Machine Learning"

Skill condition: {text}

Extract the main skill and return it alone as text.

'''

    completion = client.chat.completions.create(
model="meta-llama/llama-3.3-70b-instruct:free",
messages=[
    {
        "role": "system",
        "content": "You are a HR Assistant tasked with identifying the main skill from a given skill criteria"
    },
    {
    "role": "user",
    "content": user_msg
    }
]
)
    print(completion)
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

