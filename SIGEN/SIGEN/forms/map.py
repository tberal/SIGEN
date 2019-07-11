from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, FormField, FieldList
from flask_wtf.file import FileField, FileRequired

from SIGEN.configs import plants, envs, files, entrada, saida, receituario

class ReceituarioHeader(FlaskForm):
    pass

class ReceituarioItem(FlaskForm):
    pass
