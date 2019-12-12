from flask_jwt_extended import JWTManager

jwt = JWTManager()
from .users_controller import user_bp
from .parts_controller import parts_bp