from flask import request, json, Response, Blueprint, g
from ..models.nlu import Nlu, NluSchema

nlu_api = Blueprint('nlu_api', __name__)
nlu_schema = NluSchema()

@nlu_api.route('/', methods=['POST'])
def create():
    """
    Create Nlu Function
    """
    req_data = request.get_json()
    data = nlu_schema.load(req_data)
    
    nlu = Nlu(data)
    nlu.save()

    return custom_response({'result': "Success"}, 201)


@nlu_api.route('/', methods=['GET'])
def get_all():
    nlus = Nlu.get_all_nlus()
    ser_nlus = nlu_schema.dump(nlus, many=True)

    return custom_response(ser_nlus, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
