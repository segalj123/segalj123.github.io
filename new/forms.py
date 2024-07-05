from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class LightUploadForm(FlaskForm):
    name = StringField('Light Name', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    image_file = FileField('Upload Light Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')
