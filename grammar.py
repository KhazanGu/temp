from openai import OpenAI
import time
import os

def grammary(client, text):

  start = time.time()
  print(start)

  content1 = "Please help me correct a sentence if it has incorrect grammar \"" + text + "\""
  
  content2 = "Please output the result with a JSON object format like: {\"content\": \"\", \"recommend\": \"\", \"explain\": \"\"}"
  
  content3 = "the value of the content key should be the \"" + text + "\" 

  content4 = "the value of the recommend key should be a sentence with the correct grammar"

  content5 = "the value of the explain key should be the incorrect grammar words" 

  beg = [
      {"role": "system", "content": "You are an english teacher"},
      {"role": "user", "content": content1},
      {"role": "user", "content": content2},
      {"role": "user", "content": content3},
      {"role": "user", "content": content4},
      {"role": "user", "content": content5} 
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


  def test()
    arg1 = input("Enter the first argument: ")
    grammary(arg1)

