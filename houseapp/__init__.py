from flask import Flask
from houseapp.config import Config
from flask_sqlalchemy import SQLAlchemy
import pickle

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# model = pickle.load(open('houseapp/static/ml/model.pkl', 'rb'))

from houseapp import routes, models
