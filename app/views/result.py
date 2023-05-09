from flask import Blueprint, request, jsonify, session, g
import openai
from config import OPENAI_API_KEY
from app.database import Database

result_bp = Blueprint('result', __name__)

openai.api_key = OPENAI_API_KEY
db = Database()
# 记录当前的上下文
def set_context(response):
    session['current_context']=response

# 获取训练数据，存入上下文
def get_context():    
    return session.get('current_context', '')


# 分段
def get_paragraphs(msg):
    # 将文本按换行符分割成多个段落
    paragraphs = msg.split('\n')
    # 删除空白的段落，输出结果
    return [p for p in paragraphs]
    

# 聊天
@result_bp.route('/send', methods=['POST'])
def process_message():
    prompt = request.json.get('message', '')
    # context = get_context()
    context = g.context
    response = ''

    ask = {'role': 'user', 'content': prompt}
    # 用户消息加入上下文
    context.append(ask)
    messages=context

    try:
        # 发送请求       
        print(messages)
        print('waiting...')
        output = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        response = output.choices[0].message["content"]
        print(response)
    except Exception as e:
        print(e)
    
    # 提取回复并保存上下文
    if response:
        messages.append({'role':'assistant', 'content': response})
        # set_context(messages)
    return jsonify({'response': get_paragraphs(response)})