from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Cars


@app.route('/')
def hello():
    cars = Cars.query.all()
    return jsonify(cars)


if __name__ == '__main__':
    app.run()