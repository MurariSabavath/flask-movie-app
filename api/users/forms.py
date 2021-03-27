from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(4, 60), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(4, 100)])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(4, 60)])
    email = StringField("Email", validators=[DataRequired(), Length(4, 60), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(4, 100)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")
