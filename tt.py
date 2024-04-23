# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import time
import os

client = OpenAI(api_key=os.environ.get("sk-", "sk-"))

start = time.time()
print(start)

beg = [
    {"role": "system", "content": "You are an english teacher"},
    {"role": "user", "content": "Please help me recommend a sentence better than \"I would like have one cup of office.\", and explain why in chinese."},
    {"role": "user", "content": "Please output the result with the JSON formate like: {\"content\": \"user\", \"recommend\": \"server\", \"explain\": \"reasion\"}, the vaule of the content key should be the \"I would like have one cup of office\", the vaule of the recommend key should be the recommend sentence, the vaule of the explain key should be the explain sentence."} 
  ]

print(beg)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=beg
)

end = time.time()
print(end)

print(completion.choices[0].message)
