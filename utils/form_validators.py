"""Include all WTForms validators"""

# Form validation imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, validators, DecimalField

class SignUpForm(FlaskForm):
    class Meta:
        csrf = False

    name = StringField(
        'Name',
        [validators.DataRequired(),
         validators.Length(min=1, max=50)]
    )
    email = EmailField(
        'E-mail',
        [validators.DataRequired(),
        validators.Length(min=6, max=50)]
    )
    password = PasswordField(
        'Password',
        [validators.DataRequired(),
        validators.Length(min=64, max=64)]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        [validators.DataRequired(),
        validators.Length(min=64, max=64)]
    )
    signup = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    class Meta:
        csrf = False

    email = EmailField(
        'E-mail',
        [validators.DataRequired(),
        validators.Length(min=6, max=50)]
    )
    password = PasswordField(
        'Password',
        [validators.DataRequired(),
        validators.Length(min=64, max=64)]
    )
    login = SubmitField('Log in')

class CreateOwnerForm(FlaskForm):
    class Meta:
        csrf = False

    name = StringField(
        'Name',
        [validators.DataRequired(),
         validators.Length(min=1, max=50)]
    )
    email = EmailField(
        'E-mail',
        [validators.DataRequired(),
        validators.Length(min=6, max=50)]
    )
    phone = EmailField(
        'Telephone',
        [validators.DataRequired(),
        validators.Length(min=6, max=50)]
    )
    create_owner = SubmitField('Create Owner')

class UpdateOwnerForm(FlaskForm):
    class Meta:
        csrf = False

    id = DecimalField(
        'ID',
        [validators.DataRequired()]
    )
    name = StringField(
        'Name',
        [validators.DataRequired(),
         validators.Length(min=1, max=50)]
    )
    email = EmailField(
        'E-mail',
        [validators.DataRequired(),
        validators.Length(min=6, max=50)]
    )
    phone = EmailField(
        'Telephone',
        [validators.DataRequired(),
        validators.Length(min=6, max=50)]
    )
    update_owner = SubmitField('Update Owner')