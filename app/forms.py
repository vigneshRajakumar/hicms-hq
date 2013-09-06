from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators, BooleanField, TextAreaField, SubmitField, ValidationError
from models import User

class LoginForm(Form):
	userid = TextField('userid', [validators.Length(min=5, max=25),validators.Required()])
	password = PasswordField('password',[validators.Required()])
	remember_me = BooleanField('remember_me', default = False)

# TODO: Remove this class from here
class RegisterShopForm(Form):
	shopname = TextField('shopname', validators = [validators.Required()])
	location = TextField('location', validators = [validators.Required()])
	shopid = TextField('userid', [validators.Length(min=5, max=25),validators.Required()])
	password = PasswordField('password',[validators.Required()])
	confirmpassword = PasswordField('confirmpassword',[validators.Required()])

################################################################################################################################################
class SignupForm(Form):
  firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
  lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Create account")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user:
      self.email.errors.append("That email is already taken")
      return False
    else:
      return True

class SigninForm(Form):
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Sign In")
   
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.email.errors.append("Invalid e-mail or password")
      return False
#####################################################################################################################################################