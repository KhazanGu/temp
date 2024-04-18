# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("sk-", "sk-"))


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
