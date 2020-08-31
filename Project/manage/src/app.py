from flask import Flask

from .config import app_config
from .models import db, bcrypt

from .views.UserView import user_api as user_blueprint
from .views.NluView import nlu_api as nlu_blueprint
from .views.TemplateView import template_api as template_blueprint
from .views.StoryView import story_api as story_blueprint
from .views.BuildView import build_api as build_blueprint
from .views.LinkView import link_api as link_blueprint
from .views.LoggerMessageView import logger_message_api as logger_message_blueprint

from .views.QuestionView import question_api as question_blueprint


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    # initializing bcrypt
    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(nlu_blueprint, url_prefix='/api/v1/nlus')
    app.register_blueprint(template_blueprint, url_prefix='/api/v1/templates')
    app.register_blueprint(story_blueprint, url_prefix='/api/v1/stories')
    app.register_blueprint(build_blueprint, url_prefix='/api/v1/build')
    app.register_blueprint(question_blueprint, url_prefix='/api/v1/question')
    app.register_blueprint(link_blueprint, url_prefix='/api/v1/link')
    app.register_blueprint(logger_message_blueprint, url_prefix='/api/v1/logger')

    @app.route("/", methods=["GET"])
    def index():
        return "Congratulations! Your first endpoint is working"

    return app

