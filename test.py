Either create test.py file for importing openai api key or directly run in terminal 

from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello"}]
)

print(response.choices[0].message.content)
