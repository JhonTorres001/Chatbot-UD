from flask import request, json, Response, Blueprint, g
from ..models.logger_message import LoggerMessage, LoggerMessageSchema

logger_message_api = Blueprint('logger_message_api', __name__)
logger_message_schema = LoggerMessageSchema()


@logger_message_api.route('/', methods=['POST'])
def create():
    """
    Create Question  Function
    """
    req_data = request.get_json()
    data = logger_message_schema.load(req_data)
    
    logger_message = LoggerMessage(data)
    logger_message.save()

    return custom_response({'result': "Success"}, 201)


@logger_message_api.route('/', methods=['GET'])
def get_all():
    logger_messages = LoggerMessage.get_all_logger()
    ser_logger_messages = logger_message_schema.dump(logger_messages, many=True)

    return custom_response(ser_logger_messages, 200)

def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
