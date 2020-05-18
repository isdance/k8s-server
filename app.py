from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
# from models import Cars
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cars(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String())
    model = db.Column(db.String())

    def __init__(self, type, model):
        self.type = type
        self.model = model

    def __repr__(self):
        return '<id {}>'.format(self.id)


@app.route('/')
def hello():
    cars = Cars.query.all()
    return jsonify(cars)


if __name__ == '__main__':
    app.run()