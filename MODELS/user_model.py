from datetime import datetime
from . import db
from marshmallow import Schema, fields



class Users(db.Model):
    __tablename__ = 'users_model'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique = True, nullable=False)
    email = db.Column(db.String(50), unique = True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.date_created = datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()


    @staticmethod  # staic just means dont have to pass self into it
    def get_all_users():
        return Users.query.all()    




class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    user_name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
