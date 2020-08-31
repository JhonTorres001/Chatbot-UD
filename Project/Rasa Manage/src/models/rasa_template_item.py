from marshmallow import fields, Schema
from . import db


class RasaTemplateItem(db.Model):
    """ rasa_template_item Model for storing rasa_template_item related details """
    __tablename__ = "rasa_template_item"
    __table_args__ = {"schema": "chat_bot"}

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    item_type = db.Column("item_type", db.String(100), nullable=False)
    item_value = db.Column("item_value", db.String(100), nullable=False)
    tem_id = db.Column("tem_id", db.Integer, db.ForeignKey('chat_bot.rasa_template.id'), nullable=False)

    # class constructor
    def __init__(self, data, tem_id):
        """
        Class constructor
        """
        self.item_type = data.get('item_type')
        self.item_value = data.get('item_value')
        self.tem_id = tem_id

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
    def get_all_template_items():
        return RasaTemplateItem.query.all()

    @staticmethod
    def get_one_template_item(id):
        return RasaTemplateItem.query.get(id)

    def __repr__(self):
        return "<RasaTemplateItem '{}'>".format(self.id)


class TemplateItemSchema(Schema):
    
    """
    Template Item Schema
    """

    id = fields.Int(dump_only=True)
    tem_id = fields.Int(dump_only=True, description='rasa_template_item name')
    item_value = fields.Str(required=True)
    item_type = fields.Str(required=True)
