from flask import request, json, Response, Blueprint, g
from ..models.rasa_template import TemplateSchema, RasaTemplate
from ..models.rasa_template_item import RasaTemplateItem

template_api = Blueprint('template_api', __name__)
template_schema = TemplateSchema()


@template_api.route('/', methods=['POST'])
def create():
    """
    Create Template Function
    """
    req_data = request.get_json()
    data = template_schema.load(req_data)

    template = RasaTemplate(data)
    template.save()
    ser_template = template_schema.dump(template)
    for item in data["items"]:

        item_save = RasaTemplateItem(item, ser_template.get("id"))
        item_save.save()

    return custom_response({'result': "Success"}, 201)


@template_api.route('/', methods=['GET'])
def get_all():
    templates = RasaTemplate.get_all_templates()
    ser_templates = template_schema.dump(templates, many=True)
    return custom_response(ser_templates, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
