from flask import Flask

from .config import app_config

from .views.QuestionProcessorView import question_processor_api as question_blueprint



def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    app.register_blueprint(question_blueprint, url_prefix='/api/v1/question')

    @app.route("/", methods=["GET"])
    def index():
        return "Congratulations! Your first endpoint is working"

    return app

