# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import time
import os

client = OpenAI(api_key=os.environ.get("sk-", "sk-"))

start = time.time()
print(start)

beg = [
    {"role": "system", "content": "You are an english teacher"},
    # {"role": "user", "content": "Please help me check the grammar about "I would like have one cup of office.""},
    {"role": "user", "content": "Please help me recommend a sentence greate than "I would like have one cup of office."", and explain why},
  ]

print(beg)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=beg
)

end = time.time()
print(end)

print(completion.choices[0].message)
