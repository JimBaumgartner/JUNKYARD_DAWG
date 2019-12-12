from flask import Flask, session, request, flash, url_for, redirect, render_template
from flask_jwt_extended import create_access_token, get_jwt_identity
from SERVICES.user_service import fetch_users, create_user
from flask import Blueprint, render_template, request, json
from MODELS.user_model import Users, UserSchema
from SERVICES import user_service, bcrypt
from flask_login  import logout_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST','GET'])
def register():
	body = request.json
	message = create_user(
		body['email'],
		body['password'],
		bcrypt.generate_password_hash(body['password']).decode('utf-8'))
	return {
		'message': message,
		}
 
@user_bp.route('/login', methods=['POST'])
def login():
	body = request.json
	to_check = Users.query.filter_by(email=body['email']).first()
	if bcrypt.check_password_hash(to_check.password, body['password']):
		access_token = create_access_token(to_check.id)
		return {
			'message': 'Hey, you logged in',
			'token': access_token
		}
	else:
		return {
			'message': 'Incorrect password'
		}
	access_token = create_access_token(identity=username)
	return jsonify(access_token=access_token), 200


@user_bp.route('/search', methods=['GET'])
def search_users():
	return json.dumps(fetch_users())
from flask_login import logout_user
# other imports as necessary

@user_bp.route("/logout", methods=['POST'])
def logout():
	logout_user()
	return "You have succesfully logged out"