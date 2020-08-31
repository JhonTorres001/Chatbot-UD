from marshmallow import fields, Schema
import datetime
from . import db
from ..app import bcrypt

class UserModel(db.Model):
    """
    User Model
    """

    # table name
    __tablename__ = 'user'
    __table_args__ = {"schema": "chat_bot"}

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name_user = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_user = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name_user = data.get('name_user')
        self.email = data.get('email')
        self.password_user = self.__generate_hash(data.get('password_user'))
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            if key == 'password':
                self.password_user = self.__generate_hash(item) 
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_one_user(id):
        return UserModel.query.get(id)

    # add this new method
    def __generate_hash(self, password_user):
        return bcrypt.generate_password_hash(password_user, rounds=10).decode("utf-8")

    # add this new method   
    def check_hash(self, password_user):
        return bcrypt.check_password_hash(self.password_user, password_user)
    
    def __repr(self):
        return '<id {}>'.format(self.id)

    @staticmethod
    def get_user_by_email(value):
        return UserModel.query.filter_by(email=value).first()

# add this class
class UserSchema(Schema):
    """
    User Schema
    """
    id = fields.Int(dump_only=True)
    name_user = fields.Str(required=True)
    email = fields.Email(required=True)
    password_user = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
