from openai import OpenAI
import time
import os

def grammary(client, text)

  start = time.time()
  print(start)
  
  beg = [
      {"role": "system", "content": "You are an english teacher"},
      {"role": "user", f"content": "Please help me recommend a sentence better than \"{text}\", and in Chinese explain why ."},
      {"role": "user", f"content": "Please output the result with the JSON format like: {\"content\": \"\", \"recommend\": \"\", \"explain\": \"\"}, the value of the content key should be the \"{text}\", the value of the recommend key should be the recommend sentence, the value of the explain key should be the explain sentence."} 
    ]
  
  print(beg)
  
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=beg
  )
  
  end = time.time()
  print(end)
  
  print(completion.choices[0].message)
