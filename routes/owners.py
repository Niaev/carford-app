"""Owners related routes"""

# General imports
from datetime import datetime

# Web development imports
from flask import session

# Project general imports
from index import app, db
from services.OwnerService import OwnerService

# Form validation imports
from utils.form_validators import CreateOwnerForm

@app.post('/owners/create')
def owner_create():
    """Create new owner"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return {
            'message': 'Login first to access this function'
        }, 403

    # Get form from request payload
    form = CreateOwnerForm()

    # Validate form
    if not form.validate_on_submit():
        return {
            'message': 'Provide all requred information',
            'missing': form.errors
        }, 400

    # Get data from form
    owner_data = {
        'name': form.name.data,
        'email': form.email.data,
        'phone': form.phone.data,
        'created_at': datetime.now().strftime('%Y-%m-%d')
    }
    
    # Create owner
    service = OwnerService(db)
    try:
        response_json, response_status = service.create_owner(**owner_data)
    except Exception as e:
        return {
            'message': 'There was an internal server error',
            'error': repr(e)
        }, 500

    return response_json, response_status

@app.put('/owners/update')
def owner_update():
    """Update existing owner"""

    return None

@app.delete('/owners/delete')
def owner_delete():
    """Delete existing owner"""

    return None

@app.get('/owners')
def get_all_owners():
    """Gather all owners"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return {
            'message': 'Login first to access this function'
        }, 403

    # Create owner
    service = OwnerService(db)
    try:
        response_json, response_status = service.get_owners()
    except Exception as e:
        return {
            'message': 'There was an internal server error',
            'error': repr(e)
        }, 500

    return response_json, response_status

@app.get('/owners/<int:oid>')
def get_one_owner(oid:int):
    """Gather one owner data"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return {
            'message': 'Login first to access this function'
        }, 403

    # Create owner
    service = OwnerService(db)
    try:
        response_json, response_status = service.get_owner(oid=oid)
    except Exception as e:
        return {
            'message': 'There was an internal server error',
            'error': repr(e)
        }, 500

    return response_json, response_status