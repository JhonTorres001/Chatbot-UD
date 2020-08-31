from marshmallow import fields, Schema
from . import db


class Story(db.Model):
    """ Story Model for storing nlu related details """
    __tablename__ = "story"
    __table_args__ = {"schema": "chat_bot"}

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name_story = db.Column("name_story", db.String(100), nullable=False)
    content_story = db.Column("content_story", db.Text, nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name_story = data.get('name_story')
        self.content_story = data.get('content_story')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_stories():
        return Story.query.all()

    @staticmethod
    def get_one_story(id):
        return Story.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class StorySchema(Schema):
    
    """
    Nlu Schema
    """

    id = fields.Int(dump_only=True)
    name_story = fields.Str(required=True)
    content_story = fields.Str(required=True)
