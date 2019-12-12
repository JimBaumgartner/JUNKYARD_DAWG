from MODELS.user_model import Users, UserSchema
from marshmallow import Schema, fields
from MODELS import db
from flask_jwt_extended import create_access_token
user_schema = UserSchema()
from . import bcrypt

def create_user(email, username, password):
    new_user = Users( username, email, password)
    try:
        new_user.save()
        #this message will print in Postman
        message = {
            'Message': f'New user {username} has been created'
        }
        return message 
    except Exception as e:
        return str(e), 400


def fetch_users():
    x = Users.get_all_users()
    all_users = user_schema.dump(x, many=True)
    return all_users
   

def generate_password_hash(password):
    my_hash = bcrypt.generate_password_hash(password)
    return my_hash


def check_password_hash(password):
    pass



