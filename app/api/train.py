import openai
import json
import os
import sys


# 获取根目录的路径，并将其添加到sys.path中
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(root_path)
from config import OPENAI_API_KEY
from app.database import Database

# 设置OpenAI API密钥
openai.api_key = OPENAI_API_KEY
db = Database()
# 设置文件路径
filename = "conversation.db"

# 如果文件存在，就读取历史聊天记录
if os.path.isfile(filename):
    chat_history = db.get_conversation()
else:
    chat_history = []

# 系统消息
message = {
    'role': 'system',
    'content': '''你现在是一个英语老师，你的任务是帮助用户练习翻译。每次只要用户发送"开始练习", 你就随机生成一段100字左右的中文,话题可以是任意形式，
    但一定是记叙类，不要生成需要表达观点的文章。
    然后你需要等待用户发过来英文翻译，在此期间你不需要做任何事情，不要事先提供英文翻译，只需等用户发送。用户发送过来之后你需要检查他的
    英文翻译，包括单词拼写是否正确，短语的使用是否合适。把你的意见用中文写出来。
    最后你再提供一份标准的英文翻译事例。'''
}


chat_history.append(message)
# 与AI聊天
while True:
    prompt = input("You: ")
    if prompt.lower() == "bye":
        break
    print("\rAI: ....", end="")
    chat_history.append({
        'role': 'user',
        'content': prompt,
    })
    # 向OpenAI提问
    output = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=chat_history,
        temperature=0.5,
    )
    response = output.choices[0].message["content"]
    chat_history.append({"role": 'assistant', "content": response})
    print("\rAI: " + response)

    # 保存聊天记录
    # with open('conversation.json', 'w', encoding='utf-8') as f:
    #     json.dump(chat_history, f, ensure_ascii=False, indent=4)
    
    for item in chat_history:
        db.add_conversation(item["role"], item["content"])
db.close_connection()