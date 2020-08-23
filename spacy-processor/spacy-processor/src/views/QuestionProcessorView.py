from flask import json, request, Response, Blueprint
from ..processor.spacy_question_processor import SpacyProcessor, SpacyProcessorSchema
from ..processor.spacy_web_page_processor import SpacyWebPageProcessor, SpacyWebPageProcessorSchema, SpacyWebPageFindProcessorSchema


question_processor_api = Blueprint('question_processor_api', __name__)
spacy_processor_schema = SpacyProcessorSchema()
spacy_web_page_processor_schema = SpacyWebPageProcessorSchema()
spacy_web_page_find_processor_schema = SpacyWebPageFindProcessorSchema()


@question_processor_api.route('/similarity', methods=['POST'])
def similarity():

    req_data = request.get_json()
    data = spacy_processor_schema.load(req_data)
    spacy_processor = SpacyProcessor(data)
    spacy_processor.find_similarity()
    answer = spacy_processor_schema.dump(spacy_processor, many=False)

    return custom_response(answer, 200)


@question_processor_api.route('/process', methods=['POST'])
def process_question():

    req_data = request.get_json()
    data = spacy_processor_schema.load(req_data)
    spacy_processor = SpacyProcessor(data)
    spacy_processor.get_question_processed()
    answer = spacy_processor_schema.dump(spacy_processor, many=False)

    return custom_response(answer, 200)


@question_processor_api.route('/process_page', methods=['POST'])
def process_page():

    req_data = request.get_json()
    data = spacy_web_page_processor_schema.load(req_data)
    spacy_web_processor = SpacyWebPageProcessor(data)
    spacy_web_processor.process_page()

    return custom_response({'result': "Success"}, 201)


@question_processor_api.route('/similarity_page', methods=['POST'])
def similarity_page():

    req_data = request.get_json()
    data = spacy_web_page_find_processor_schema.load(req_data)
    spacy_web_find_processor = SpacyWebPageProcessor(data)
    spacy_web_find_processor.find_similarity_page()

    answer = spacy_web_page_find_processor_schema.dump(spacy_web_find_processor, many=False)

    return custom_response(answer, 200)

def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
