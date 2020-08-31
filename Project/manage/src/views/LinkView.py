from flask import request, json, Response, Blueprint, g
from ..models.link import Link, LinkSchema

link_api = Blueprint('link_api', __name__)
link_schema = LinkSchema()


@link_api.route('/', methods=['POST'])
def create():
    """
    Create Question  Function
    """
    req_data = request.get_json()
    data = link_schema.load(req_data)
    
    link = Link(data)
    link.save()

    return custom_response({'result': "Success"}, 201)


@link_api.route('/', methods=['GET'])
def get_all():
    links = Link.get_all_links()
    ser_links = link_schema.dump(links, many=True)

    return custom_response(ser_links, 200)

def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
