from flask import request, json, Response, Blueprint, g
from ..models.story import Story, StorySchema

story_api = Blueprint('story_api', __name__)
story_schema = StorySchema()


@story_api.route('/', methods=['POST'])
def create():
    """
    Create Story Function
    """
    req_data = request.get_json()
    data = story_schema.load(req_data)
    
    story = Story(data)
    story.save()

    return custom_response({'result': "Success"}, 201)


@story_api.route('/', methods=['GET'])
def get_all():
    stories = Story.get_all_stories()
    ser_stories = story_schema.dump(stories, many=True)

    return custom_response(ser_stories, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
