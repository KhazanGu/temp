from openai import OpenAI
import time
import os

def grammary(client, text):

  start = time.time()
  print(start)

  content1 = "Please help me recommend a sentence better than \"" + text + "\", and in Simplified Chinese explain why."
  
  content2 = "Please output the result with the JSON format like: {\"content\": \"\", \"recommend\": \"\", \"explain\": \"\"}, the value of the content key should be the \"" + text + "\", the value of the recommend key should be the recommend sentence, the value of the explain key should in Simplified Chinese be the explain sentence."

  beg = [
      {"role": "system", "content": "You are an english teacher"},
      {"role": "user", "content": content1},
      {"role": "user", "content": content2} 
    ]
  
  print(beg)
  
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=beg
  )
  
  end = time.time()
  print(end)

  content = completion.choices[0].message.content


  # Specify the file path
  file_path = "output.txt"

# Open the file in write mode
  with open(file_path, 'a') as file:
    # Iterate over the strings and write each one to the file
    file.write(content + '\n')  #
