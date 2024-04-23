# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import time
import os

client = OpenAI(api_key=os.environ.get("sk-", "sk-"))

start = time.time()
print(start)

beg = [
    {"role": "user", "content": "Please help me generate 100 sentences that are all incorrect grammar."},
  ]

print(beg)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  response_format={ "type": "json_object" },
  messages=beg
)

end = time.time()
print(end)

print(completion.choices[0].message)
