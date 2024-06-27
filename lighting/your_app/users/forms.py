from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from your_app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    user_type = SelectField('User Type', choices=[('designer', 'Designer'), ('contractor', 'Contractor')], validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already registered. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class CategorySelectionForm(FlaskForm):
    light_type = StringField('Light Type', validators=[DataRequired()])
    bulb_type = StringField('Bulb Type', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    design_type = SelectField('Design Type', choices=[('farmhouse', 'Farmhouse'), ('contemporary', 'Contemporary'), ('modern', 'Modern')], validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')
