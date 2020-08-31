from marshmallow import fields, Schema
from . import db
import requests
from ..utils.constants import *
import json

class Question(db.Model):
    """ NLU Model for storing nlu related details """
    __tablename__ = "question"
    __table_args__ = {"schema": "chat_bot"}

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    question = db.Column("question", db.Text, nullable=False)
    simple_question = db.Column("simple_question", db.Text, nullable=False)
    answer = db.Column("answer", db.Text, nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.question = data.get('question')
        self.simple_question = ""#data.get('simple_question')
        self.answer = data.get('answer')

    def process_question(self):
        url = SPACY_PROCESS_QUESTION_ENDPOINT
        headers = {'content-type': 'application/json'}
        requestProcessQuestion = {
            "question": self.question
        }

        print(json.dumps(requestProcessQuestion))

        response = requests.post(url, data=json.dumps(requestProcessQuestion), headers=headers)
        simple_question_response = json.loads(response.text)
        self.simple_question = simple_question_response['simple_question']

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
    def get_all_questions():
        return Question.query.all()

    @staticmethod
    def get_one_question(id):
        return Question.query.get(id)

    @staticmethod
    def get_array_string(alist):
        return '{' + ','.join(alist) + '}'


    def __repr(self):
        return '<id {}>'.format(self.id)


class QuestionSchema(Schema):
    
    """
    Question Schema
    """

    id = fields.Int(dump_only=True)
    question = fields.Str(required=True)
    answer = fields.Str(required=True)
    simple_question = fields.Str(dump_only=True)
