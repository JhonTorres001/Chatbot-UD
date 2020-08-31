from marshmallow import fields, Schema
from . import db
import requests
from ..utils.constants import *
import json

class LoggerMessage(db.Model):
    """ NLU Model for storing nlu related details """
    __tablename__ = "logger_messages"
    __table_args__ = {"schema": "chat_bot"}

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column("user_id", db.Text, nullable=False)
    question = db.Column("question", db.Text, nullable=False)
    answer = db.Column("answer", db.Text, nullable=False)
    score = db.Column("score", db.Text, nullable=False)
    date_message = db.Column("date_message", db.Text, nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.user_id = data.get('user_id')
        self.question = data.get('question')
        self.answer = data.get('answer')
        self.score = data.get('score')
        self.date_message = data.get('date_message')

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
    def get_all_logger():
        return LoggerMessage.query.all()

    @staticmethod
    def get_one_logger(id):
        return LoggerMessage.query.get(id)

    @staticmethod
    def get_array_string(alist):
        return '{' + ','.join(alist) + '}'


    def __repr(self):
        return '<id {}>'.format(self.id)


class LoggerMessageSchema(Schema):
    """
    Link Schema
    """
    id = fields.Int(dump_only=True)
    user_id = fields.Str(required=True)
    question = fields.Str(required=True)
    answer = fields.Str(required=True)
    score = fields.Str(required=True)
    date_message = fields.Str(required=True)
