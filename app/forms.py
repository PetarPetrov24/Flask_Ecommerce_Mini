from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, IntegerField, FileField
from wtforms.validators import DataRequired, Regexp
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class AddProduct(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired(), 
    Regexp(r'^\d+(\.\d{1,2})?$', message="Only numbers allowed, optional 2 decimals")])
    image = FileField('Product Image', validators=[FileAllowed(['jpg','png','jpeg','gif'], 'Images only!')])
    stock = IntegerField('Stock', validators=[DataRequired()])
    submit = SubmitField('Add Product')

class RemoveFromCartForm(FlaskForm):
    submit = SubmitField('Remove')
    