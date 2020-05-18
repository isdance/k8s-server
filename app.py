from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
# from models import Cars
from flask_marshmallow import Marshmallow
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


ma = Marshmallow(app)


class CarsSchema(ma.Schema):
    class Meta:
        fields = ('id','type','model')


@app.route('/')
def hello():
    cars = Cars.query.all()
    cars_schema = CarsSchema(many=True) 
    result = cars_schema.dump(cars)
    return jsonify(result)


if __name__ == '__main__':
    app.run()

