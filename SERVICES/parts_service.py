from MODELS.parts_model import Parts, PartsSchema
from CONTROLLERS import parts_controller 
from marshmallow import Schema, fields
from MODELS import db


parts_schema = PartsSchema()

def create_part(part, make, model, trim_package, year, target_make, target_model, target_trim_package, target_year, notes):
    new_part = Parts(part, make, model, trim_package, year,target_make, target_model, target_trim_package, target_year, notes)
    try:
        new_part.save()
        # this message will print in Postman 
        message = {
           'Message' : f'New Part  has been created:>>> part({part})  for a {year} {make} {model}. This Part will fit a {target_year} {target_make} {target_model}'
        }
        return message
    except Exception as e:
        return str(e), 400

def fetch_parts():
    x = Parts.get_all_parts()
    all_parts = parts_schema.dump(x, many=True)
    return all_parts


def fetch_part(make,model):
    x = Parts.get_all_part(make,model)
    all_part = parts_schema.dump(x, many=True)
    return all_part


def edit_part(part_id, data):
    x = Parts.get_one_part(part_id)
    updated = x.update(x, data)
    new_part = parts_schema.dump(updated)
    return new_part


def delete_part(part_id):
    x = Parts.get_one_part(part_id)
    return x.delete()
