from flask import request, json, Response, Blueprint, g
from ..models.question import Question, QuestionSchema

question_api = Blueprint('question_api', __name__)
question_schema = QuestionSchema()


@question_api.route('/', methods=['POST'])
def create():
    """
    Create Question  Function
    """
    req_data = request.get_json()
    data = question_schema.load(req_data)
    
    question = Question(data)
    question.process_question()
    question.save()

    return custom_response({'result': "Success"}, 201)


@question_api.route('/', methods=['GET'])
def get_all():
    quuestions = Question.get_all_questions()
    ser_questions = question_schema.dump(quuestions, many=True)

    return custom_response(ser_questions, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
