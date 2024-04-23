
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
  
# Use the OpenAI API to correct the sentence
  response = client.Completion.create(
      engine="text-davinci-003",  # Choose the engine you want to use
      prompt=text,
      max_tokens=50  # Adjust as needed
  )

  end = time.time()
  print(end)

  corrected_sentence = response.choices[0].text.strip()

  print(corrected_sentence)

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
