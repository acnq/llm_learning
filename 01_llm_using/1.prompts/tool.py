import os

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

def get_openai_key():
  # 读取本地/项目的环境变量。

  # find_dotenv()寻找并定位.env文件的路径
  # load_dotenv()读取该.env文件，并将其中的环境变量加载到当前的运行环境中  
  # 如果你设置的是全局的环境变量，这行代码则没有任何作用。
  _ = load_dotenv(find_dotenv())
  return os.environ['OPENAI_API_KEY']


client = OpenAI(api_key=get_openai_key(), base_url="https://api.deepseek.com/beta")

def get_completion(prompt, model="deepseek-chat", temperature=0):
  '''
  prompt: 对应的提示词
  model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)，有内测资格的用户可以选择 gpt-4
  '''
  messages = [{"role": "user", "content": prompt}]
  response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=temperature,
  )
  # 调用OpenAI的ChatCompletion 接口
  return response.choices[0].message.content

def get_completion_from_messages(messages, model="deepseek-chat", temperature=0):
  response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=temperature,
  )
  # 调用OpenAI的ChatCompletion 接口
  return response.choices[0].message.content
  