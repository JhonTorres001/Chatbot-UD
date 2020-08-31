from flask import json, Response, Blueprint
from ..models.story import Story, StorySchema
from ..models.nlu import Nlu, NluSchema
from ..models.rasa_template import RasaTemplate, TemplateSchema
from ..processors.story_processor import StoryProccesor
from ..processors.nlu_processor import NluProccesor
from ..processors.domain_processor import DomainProccesor

build_api = Blueprint('build_api', __name__)
story_schema = StorySchema()
nlu_schema = NluSchema()
template_schema = TemplateSchema()


@build_api.route('/all', methods=['POST'])
def create():

    # nlu process
    nlus = Nlu.get_all_nlus()
    ser_nlus = nlu_schema.dump(nlus, many=True)
    nlu_processor = NluProccesor(ser_nlus)
    nlu_processor.proccess()

    templates = RasaTemplate.get_all_templates()
    ser_templates = template_schema.dump(templates,  many=True)

    # domain process
    intents = [intent for intent in ser_nlus if intent["type_nlu"] == "intent"]
    domain_processor = DomainProccesor(intents, ser_templates)
    domain_processor.proccess()

    #filtrar nlus por intents

    # story process

    stories = Story.get_all_stories()
    ser_stories = story_schema.dump(stories, many=True)
    story_processor = StoryProccesor(ser_stories)
    story_processor.proccess()

    return custom_response({'result': 'success'}, 201)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
