from flask import Blueprint, render_template, session, g
import json

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    # 加载训练数据
    with open('conversation.json', "r", encoding='utf-8') as f:
        chat_history = json.load(f)
    session['current_context']=chat_history
    return render_template('index.html')