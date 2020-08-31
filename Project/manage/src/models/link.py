from marshmallow import fields, Schema
from . import db
import requests
from ..utils.constants import *
import json

class Link(db.Model):
    """ NLU Model for storing nlu related details """
    __tablename__ = "link"
    __table_args__ = {"schema": "chat_bot"}

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    home_page = db.Column("home_page", db.Text, nullable=False)
    title_page = db.Column("title_page", db.Text, nullable=False)
    simple_title_page = db.Column("simple_title_page", db.Text, nullable=False)
    url_page = db.Column("url_page", db.Text, nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.home_page = data.get('home_page')
        self.title_page = data.get('title_page')
        self.simple_title_page = data.get('simple_title_page')
        self.url_page = data.get('url_page')

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
    def get_all_links():
        return Link.query.all()

    @staticmethod
    def get_one_link(id):
        return Link.query.get(id)

    @staticmethod
    def get_array_string(alist):
        return '{' + ','.join(alist) + '}'


    def __repr(self):
        return '<id {}>'.format(self.id)


class LinkSchema(Schema):
    """
    Link Schema
    """
    id = fields.Int(dump_only=True)
    home_page = fields.Str(required=True)
    title_page = fields.Str(required=True)
    simple_title_page = fields.Str(required=True)
    url_page = fields.Str(required=True)
