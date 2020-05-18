from app import db
from sqlalchemy.dialects.postgresql import JSON


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