from openai import OpenAI
import time
import os
import json
import gra

client = OpenAI(api_key=os.environ.get("sk-", "sk-"))

start = time.time()
print(start)

beg = [
    {"role": "user", "content": "Please help me generate a JSON object that contains 100 sentences that 50 sentences are incorrect grammar and 50 sentences are correct grammar."},  
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

print(obj)

sentences = obj["sentences"]

for element in sentences:
    gra.grammary(client, element)


#print(sentences)
