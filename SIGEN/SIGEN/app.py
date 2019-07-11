from flask import Flask, redirect, url_for
from flask_wtf.csrf import CSRFProtect

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Test'

csrf = CSRFProtect(app)


