from .spacy_utils import *
from marshmallow import fields, Schema

class SpacyProcessor:

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.question = data.get('question')
        self.simple_question = ""
        self.answer = ""
        self.score = 0.0
        self.status = ""

    def find_similarity(self):
        question_nlp = NLP(process_question(self.question))
        answers = list()

        for stored_question in ALL_QUESTIONS:
            stored_question_nlp = NLP(stored_question['simple_question'])
            score_found = stored_question_nlp.similarity(question_nlp)
            print(score_found)
            if score_found > 0.85: # parametrizar
                question_found = dict(stored_question)
                question_found["score"] = score_found
                answers.append(question_found)

        if len(answers) > 0:
            best_answer = max(answers, key=lambda x: x['score'])
            self.status = "FOUND"
            self.simple_question = best_answer['simple_question']
            self.question = best_answer['question']
            self.answer = best_answer['answer']
            self.score = best_answer['score']
        else:
            self.answer = ""
            self.status = "NOT_FOUND"

    def __repr(self):
        return '<id {}>'.format(self.question)

    def get_question_processed(self):
        self.simple_question = process_question(self.question)

    def __repr(self):
        return '<id {}>'.format(self.question)

class SpacyProcessorSchema(Schema):
    """
    Nlu Schem
    """

    question = fields.Str(required=True)
    simple_question = fields.Str(dump_only=True)
    answer = fields.Str(dump_only=True)
    status = fields.Str(dump_only=True)
    score = fields.Float(dump_only=True)
