from flask_wtf import FlaskForm
from wtforms import SelectField
from flask_wtf.file import FileField, FileRequired

from SIGEN.configs import plants, envs, files

class UploadFile(FlaskForm):
    plant = SelectField('Planta', choices = [(p, p) for p in plants.keys()])
    env = SelectField('Ambiente', choices = [(e, e) for e in envs.keys()])
    filetype = SelectField('Tipo de Arquivo', choices = [(x, y) for x, y in files.items()])
    file = FileField('Arquivo', validators=[FileRequired()],
            render_kw={})
