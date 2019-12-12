from flask import Flask, Blueprint, render_template, request, json
from flask_sqlalchemy import SQLAlchemy
from CONTROLLERS.users_controller import user_bp
from CONTROLLERS.parts_controller import parts_bp
from MODELS import db  
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity)

import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') 
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')  # setting the URI for sqlalchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence the deprecation warning

db.init_app(app)  # initalizing the init
jwt = JWTManager(app)
# registering all of the blueprints
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(parts_bp, url_prefix="/parts")


if __name__ == "__main__":
    app.run(debug=True)
