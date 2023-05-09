from flask import Flask, g
from app.views.index import index_bp
from app.views.result import result_bp
from app.database import Database


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
db = Database()

app.register_blueprint(index_bp)
app.register_blueprint(result_bp)

@app.before_request
def before_request():
    g.context = db.get_conversation()