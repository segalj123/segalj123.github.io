from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    user_type = SelectField('User Type', choices=[('designer', 'Designer'), ('contractor', 'Contractor')], validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class CategoryForm(FlaskForm):
    light_type = StringField('Light Type', validators=[DataRequired()])
    bulb_type = StringField('Bulb Type', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    design_type = StringField('Design Type', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')
