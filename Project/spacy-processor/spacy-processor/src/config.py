import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = "postgresql://postgres:12345678@rasa-api-db.cji4kt3jve9x.us-east-2.rds.amazonaws.com/rasa_api_db"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123456@localhost/rasa_api_db"

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    #SQLALCHEMY_DATABASE_URI = "postgresql://postgres:12345678@rasa-api-db.cji4kt3jve9x.us-east-2.rds.amazonaws.com/rasa_api_db"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123456@localhost/rasa_api_db"
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app_config = {
    'development': Development,
    'production': Production,
}