from . import db
from marshmallow import Schema, fields
from datetime import datetime
class Parts(db.Model):
    __tablename__ = 'parts_model'

    id = db.Column(db.Integer, primary_key=True)
    part = db.Column(db.String(100), nullable=False)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    trim_package = db.Column(db.String(100), nullable=True)
    year = db.Column(db.Integer, nullable=False)
    target_make = db.Column(db.String(100), nullable=False)
    target_model = db.Column(db.String(100), nullable=False)
    target_trim_package = db.Column(db.String(100), nullable=True)
    target_year = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(500), nullable=False)
    def __init__(self,part, make, model, trim_package, year,target_make,target_model,target_trim_package,target_year,notes):
        self.part = part
        self.make = make
        self.model = model
        self.trim_package = trim_package
        self.year = year
        self.target_make  = target_make
        self.target_model  = target_model
        self.target_trim_package  = target_trim_package
        self.target_year  = target_year
        self.notes = notes


    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod  # staic just means dont have to pass self into it
    def get_all_parts():
        return Parts.query.all()

    @staticmethod  # staic just means dont have to pass self into it
    def get_all_part(make,model):
        x = Parts.query.filter_by(make=make,model=model)
        if x:
            return x
        else:
            return 'no'
    
    @staticmethod
    def get_one_part(part_id):
        x = Parts.query.filter_by(id=part_id).first()
        return x


    def update(self, old, data):
        for key, item in data.items():
            setattr(old, key, item)
        self.modified_at = datetime.utcnow()
        db.session.commit()
        return old

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return "Successfully Deleted"


class PartsSchema(Schema):
    id = fields.Int(dump_only=True)
    part = fields.Str(required=True)
    make = fields.Str(required=True)
    model = fields.Str(required=True)
    trim_package = fields.Str(required=False)
    year = fields.Str(required=True)
    target_make = fields.Str(required=True)
    target_model = fields.Str(required=True)
    target_trim_package = fields.Str(required=False)
    target_year = fields.Str(required=False)
    notes = fields.Str(required=False)
