from flask_wtf import FlaskForm
from wtforms import fields

class SampleForm(FlaskForm):
    name = fields.StringField()
    age = fields.IntegerField()