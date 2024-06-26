from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    user_type = RadioField('I am a', choices=[('designer', 'Designer'), ('seller', 'Seller')], validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UploadForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('Chandelier', 'Chandelier'),
        ('Pendant', 'Pendant'),
        ('Ceiling', 'Ceiling'),
        ('Wall', 'Wall'),
        ('Table', 'Table'),
        ('Floor', 'Floor')
    ], validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png'])])
    color = StringField('Color', validators=[Optional()])
    price = FloatField('Price', validators=[Optional()])
    min_order_quantity = IntegerField('Min Order Quantity', validators=[Optional()])
    submit = SubmitField('Upload')

class FilterForm(FlaskForm):
    category = SelectField('Category', choices=[
        ('Chandelier', 'Chandelier'),
        ('Pendant', 'Pendant'),
        ('Ceiling', 'Ceiling'),
        ('Wall', 'Wall'),
        ('Table', 'Table'),
        ('Floor', 'Floor')
    ], validators=[Optional()])
    color = StringField('Color', validators=[Optional()])
    min_price = FloatField('Min Price', validators=[Optional()])
    max_price = FloatField('Max Price', validators=[Optional()])
    min_order_quantity = IntegerField('Min Order Quantity', validators=[Optional()])
    location_type = SelectField('Location Type', choices=[
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Industrial', 'Industrial'),
        ('Commercial', 'Commercial'),
        ('Outdoor', 'Outdoor'),
        ('Other', 'Other')
    ], validators=[Optional()])
    submit = SubmitField('Apply Filters')
