from flask import Flask, g
from app.views.index import index_bp
from app.views.result import result_bp


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


app.register_blueprint(index_bp)
app.register_blueprint(result_bp)