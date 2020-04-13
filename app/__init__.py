import os

from flask import Flask, session
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# app.config['SESSION_TYPE'] = 'filesystem'
# app.config['SECRET_KEY'] = os.urandom(24)
# session(app)


from app import routes
