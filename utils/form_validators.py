"""Include all WTForms validators"""

# Form validation imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, validators, DecimalField

def validate_car_fields(color:str, model:str) -> tuple:
    """Validate color and model fields from a car"""

    valid_colors = [
        'yellow',
        'blue',
        'gray'
    ]

    valid_models = [
        'hatch',
        'sedan',
        'convertible'
    ]

    if color not in valid_colors:
        return {
            'message': 'Provide all required information',
            'missing': {
                'color': f'Provide a valid color: {valid_colors}'
            }
        }, 400

    if model not in valid_models:
        return {
            'message': 'Provide all required information',
            'missing': {
                'model': f'Provide a valid model: {valid_models}'
            }
        }, 400

    # If it is all good
    return None, None

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

class DeleteOwnerForm(FlaskForm):
    class Meta:
        csrf = False

    id = DecimalField(
        'ID',
        [validators.DataRequired()]
    )

class CreateCarForm(FlaskForm):
    class Meta:
        csrf = False

    owner_id = DecimalField(
        'Owner ID',
        [validators.DataRequired()]
    )
    color = StringField(
        'Color',
        [validators.DataRequired(),
        validators.Length(max=50)]
    )
    model = StringField(
        'Model',
        [validators.DataRequired(),
        validators.Length(max=50)]
    )
    create_car = SubmitField('Create Car')