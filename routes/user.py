"""User related routes"""

# General imports
from datetime import datetime

# Web development imports
from flask import session

# Project general imports
from index import app, db
from services.UserService import UserService

# Form validation imports
from utils.form_validators import SignUpForm, LoginForm

@app.post('/users/signup')
def user_signup():
    """Sign Up user"""

    # Get form from request payload
    form = SignUpForm()

    # Validate form
    if not form.validate_on_submit():
        return {
            'message': 'Provide all requred information',
            'missing': form.errors
        }, 400

    # Get data from form
    user_data = {
        'name': form.name.data,
        'email': form.email.data,
        'pwd': form.password.data,
        'cpwd': form.confirm_password.data,
        'created_at': datetime.now().strftime('%Y-%m-%d')
    }
    
    service = UserService(db)
    try:
        response_json, response_status = service.create_user(**user_data)
    except Exception as e:
        return {
            'message': 'There was an internal server error',
            'error': repr(e)
        }, 500

    return response_json, response_status

@app.post('/users/login')
def user_login():
    """Log In user"""

    # Get form from request payload
    form = LoginForm()

    # Validate form
    if not form.validate_on_submit():
        return {
            'message': 'Provide all requred information',
            'missing': form.errors
        }, 400

    # Get data from form
    user_data = {
        'email': form.email.data,
        'pwd': form.password.data
    }
    
    service = UserService(db)
    try:
        response_json, response_status = service.auth_user(**user_data)
    except Exception as e:
        return {
            'message': 'There was an internal server error',
            'error': repr(e)
        }, 500

    return response_json, response_status

@app.post('/users/logout')
def user_logout():
    """Log Out current user"""

    session.clear()
    session.modified = True

    return {
        'message': 'Successfully logged out'
    }, 200