from marshmallow import fields, Schema
from . import db


class Nlu(db.Model):
    """ NLU Model for storing nlu related details """
    __tablename__ = "nlu"
    __table_args__ = {"schema": "chat_bot"}

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    type_nlu = db.Column("nlu_type", db.String(100), nullable=False)
    name = db.Column("nlu_name", db.String(100), nullable=False)
    value = db.Column("value", db.String(1000), nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.type_nlu = data.get('type_nlu')
        self.value = Nlu.to_array_db(data.get('value'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_nlus():
        return Nlu.query.all()

    @staticmethod
    def get_one_nlu(id):
        return Nlu.query.get(id)

    @staticmethod
    def get_array_string(alist):
        return '{' + ','.join(alist) + '}'


    def __repr(self):
        return '<id {}>'.format(self.id)

class NluSchema(Schema):
    
    """
    Nlu Schema
    """

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    type_nlu = fields.Str(required=True)
    value = fields.List(fields.String(), description='nlu value')
