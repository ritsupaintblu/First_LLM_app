from openai import OpenAI

client = OpenAI()   # reads OPENAI_API_KEY + OPENAI_BASE_URL from the environment
resp = client.chat.completions.create(
    model="gemma-4-E4B-it",
    messages=[{"role": "user", "content": "Say hi in one sentence."}],
)
print(resp.choices[0].message.content)