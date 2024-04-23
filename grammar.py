from openai import OpenAI
import time
import os

# Get the current directory
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
file_path = os.path.join(parent_directory, "key.txt")

file_content = ""

with open(file_path, 'r') as file:
    # Read the entire file content into a string
    file_content = file.read()

print(file_content)

key = file_content.rstrip("\n")


def grammary(client, text):

  start = time.time()
  print(start)

  content1 = "Please help me correct a sentence about \"" + text + "\" if it is incorrect."
  
  content2 = "Please output the result with a JSON object format like: {\"correct\": \"\", \"error\": \"\", \"error_words\": \"\"}"

  content3 = "The value of the key name \"correct\" should be an empty string if the sentence is correct else should be a correct sentence." 

  content4 = "The value of the key name \"error\" should be an empty string if the sentence is correct else should be the reason for incorrect and must be in Simplified Chinese."

  content5 = "The value of the key name \"error_words\" should be an empty string if the sentence is correct else should be those incorrect words."

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
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=beg
  )
  
  end = time.time()
  print(end)

  content = completion.choices[0].message.content

  print(content)

#   # Specify the file path
#   file_path = "output.txt"

# # Open the file in write mode
#   with open(file_path, 'a') as file:
#     # Iterate over the strings and write each one to the file
#     file.write(content + '\n')  #


if __name__ == '__main__':
  arg1 = input("Enter the first argument: ")
  client = OpenAI(api_key=os.environ.get(key, key))
  grammary(client, arg1)
