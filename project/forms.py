from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    role = SelectField('Role', choices=[('swiper', 'Swiper (Looking for lighting)'), ('builder', 'Builder (Supplying the lights)')], validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class LightUploadForm(FlaskForm):
    name = StringField('Light Name', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    height = StringField('Height', validators=[DataRequired()])
    submit = SubmitField('Upload')
