from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length

class LoginForm(Form):
	email = StringField('E-Mail', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Remember me')
	submit = SubmitField('Log in')