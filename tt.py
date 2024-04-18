# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import time
import os

client = OpenAI(api_key=os.environ.get("sk-", "sk-"))

start = time.time()
print(start)

beg = [
    {"role": "system", "content": "你是英语教师"},
    {"role": "user", "content": "我正在练习英语，当前的对话场景是旅游出行，我们的对话都应该是中文,我们的对话都应该是旅游相关的，如果我的提问与旅游无关的请你提醒我。"},
    {"role": "user", "content": "请你模仿被求助人，说一句少于30字的开场问候"}
  ]

print(beg)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=beg
)

end = time.time()
print(end)

print(completion.choices[0].message)
