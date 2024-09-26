"""Cars related routes"""

# General imports
from datetime import datetime

# Web development imports
from flask import session

# Project general imports
from index import app, db
from services.CarService import CarService

# Form validation imports
from utils.form_validators import CreateCarForm, validate_car_fields, UpdateCarForm, DeleteCarForm

@app.post('/cars/create')
def car_create():
    """Create new car"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return {
            'message': 'Login first to access this function'
        }, 403

    # Get form from request payload
    form = CreateCarForm()

    # Validate form
    if not form.validate_on_submit():
        return {
            'message': 'Provide all requred information',
            'missing': form.errors
        }, 400

    # Get data from form
    car_data = {
        'oid': form.owner_id.data,
        'color': form.color.data,
        'model': form.model.data,
        'created_at': datetime.now().strftime('%Y-%m-%d')
    }

    # Validate color and model data from form
    response_json, response_status = validate_car_fields(car_data['color'], car_data['model'])
    if response_json and response_status:
        return response_json, response_status
    
    # Create car
    service = CarService(db)
    try:
        response_json, response_status = service.create_car(**car_data)
    except Exception as e:
        return {
            'message': 'There was an internal server error',
            'error': repr(e)
        }, 500

    return response_json, response_status

@app.put('/cars/update')
def car_update():
    """Update existing car"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return {
            'message': 'Login first to access this function'
        }, 403

    # Get form from request payload
    form = UpdateCarForm()

    # Validate form
    if not form.validate_on_submit():
        return {
            'message': 'Provide all requred information',
            'missing': form.errors
        }, 400

    # Get data from form
    car_data = {
        'cid': form.id.data,
        'oid': form.owner_id.data,
        'color': form.color.data,
        'model': form.model.data
    }

    # Validate color and model data from form
    response_json, response_status = validate_car_fields(car_data['color'], car_data['model'])
    if response_json and response_status:
        return response_json, response_status
    
    # Update car
    service = CarService(db)
    try:
        response_json, response_status = service.update_car(**car_data)
    except Exception as e:
        return {
            'message': 'There was an internal server error',
            'error': repr(e)
        }, 500

    return response_json, response_status

@app.delete('/cars/delete')
def car_delete():
    """Delete existing car"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return {
            'message': 'Login first to access this function'
        }, 403

    # Get form from request payload
    form = DeleteCarForm()

    # Validate form
    if not form.validate_on_submit():
        return {
            'message': 'Provide all requred information',
            'missing': form.errors
        }, 400

    # Get data from form
    car_data = {
        'cid': form.id.data,
    }
    
    # Delete car
    service = CarService(db)
    try:
        response_json, response_status = service.delete_car(**car_data)
    except Exception as e:
        return {
            'message': 'There was an internal server error',
            'error': repr(e)
        }, 500

    return response_json, response_status

@app.get('/cars')
def get_all_cars():
    """Gather all cars"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return {
            'message': 'Login first to access this function'
        }, 403

    # Get car
    service = CarService(db)
    try:
        response_json, response_status = service.get_cars()
    except Exception as e:
        return {
            'message': 'There was an internal server error',
            'error': repr(e)
        }, 500

    return response_json, response_status

@app.get('/cars/<int:cid>')
def get_one_car(cid:int):
    """Gather one car data"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return {
            'message': 'Login first to access this function'
        }, 403

    # Get car
    service = CarService(db)
    try:
        response_json, response_status = service.get_car(cid=cid)
    except Exception as e:
        return {
            'message': 'There was an internal server error',
            'error': repr(e)
        }, 500

    return response_json, response_status