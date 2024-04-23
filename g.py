# import the OpenAI Python library for calling the OpenAI API
# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import time
import os
import json

client = OpenAI(api_key=os.environ.get("sk-", "sk-"))

start = time.time()
print(start)

beg = [
    {"role": "user", "content": "Please help me generate a JSON object that contains 100 sentences that are all incorrect grammar."},
  ]

print(beg)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  response_format={ "type": "json_object" },
  messages=beg
)

end = time.time()
print(end)

content = completion.choices[0].message.content

obj = json.loads(content)

sentences = obj["sentences"]

print(sentences)
