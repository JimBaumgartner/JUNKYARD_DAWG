from flask import Blueprint, render_template, request, json, jsonify
from MODELS.parts_model import Parts, PartsSchema
from SERVICES.parts_service import fetch_parts , fetch_part, edit_part, delete_part
from SERVICES import parts_service
from . import jwt
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
parts_bp = Blueprint('parts', __name__)

@parts_bp.route('/new_part', methods=['POST','GET'])
def new_part():
    if request.method == 'POST':
        part=request.json.get('part')
        make=request.json.get('make')
        model=request.json.get('model')
        trim_package=request.json.get('trim_package')
        year=request.json.get('year')
        target_make=request.json.get('target_make')
        target_model=request.json.get('target_model')
        target_trim_package = request.json.get('target_trim_package')
        target_year = request.json.get('target_year')
        notes = request.json.get('notes')
        result = parts_service.create_part(part, make, model, trim_package, year, target_make, target_model, target_trim_package, target_year, notes)
        return result
    return print( f'New part created for {make} , {model}, {year}')


@parts_bp.route('/search', methods=['GET'])
def search_parts():
    return json.dumps(fetch_parts())


@parts_bp.route('/search/<make>/<model>', methods=['GET'])
def search_part(make,model):
    return json.dumps(fetch_part(make,model))

@parts_bp.route('/delete/<int:part_id>', methods=['DELETE'])
def del_part(part_id):
    if request.method=='DELETE':
        user = get_jwt_identity()
        # part = delete_part(part_id)
        # Parts.query.filter_by(id=part_id).first()
        return delete_part(part_id)
    return f'Part {id} has been deleted'



@parts_bp.route('/update/<int:part_id>', methods=['PUT'])
def update_part(part_id):
        data = request.json
        return jsonify(edit_part(part_id, data))
