from marshmallow import fields, Schema
from . import db
from .rasa_template_item import TemplateItemSchema, RasaTemplateItem


class RasaTemplate(db.Model):
    """ Rasa_Template Model for storing Rasa_Template related details """
    __tablename__ = "rasa_template"
    __table_args__ = {"schema": "chat_bot"}

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    tem_name = db.Column("tem_name", db.String(255), unique=True, nullable=False)
    items = db.relationship(RasaTemplateItem, backref='chat_bot.rasa_template', lazy=True)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.tem_name = data.get('tem_name')

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
    def get_all_templates():
        return RasaTemplate.query.all()

    @staticmethod
    def get_one_template(id):
        return RasaTemplate.query.get(id)

    def __repr__(self):
        return "<RasaTemplate '{}'>".format(self.tem_name)

class TemplateSchema(Schema):
    
    """
    Template Item Schema
    """

    id = fields.Int(dump_only=True)
    tem_name = fields.Str(required=True)
    items = fields.Nested(TemplateItemSchema, many=True)
