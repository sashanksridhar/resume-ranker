from openai import OpenAI
import httpx

# To extract candidate name from the resume
def find_candidate(text):
    transport = httpx.HTTPTransport(verify=False)

    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    http_client=httpx.Client(transport=transport)
    )

    user_msg = f'''
Given a resume of a candidate, extract the name of the candidate alone.

Resume: {text}

Extract the resume and return the name of the candidate alone.

'''

    completion = client.chat.completions.create(
model="meta-llama/llama-3.3-70b-instruct:free",
messages=[
    {
        "role": "system",
        "content": "You are a HR Assistant tasked with identifying the name of the candidate from the resume"
    },
    {
    "role": "user",
    "content": user_msg
    }
]
)
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content