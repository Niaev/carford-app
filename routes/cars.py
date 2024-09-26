"""Cars related routes"""

# Web development imports
from flask import session

# Project general imports
from index import app, db
from services.CarService import CarService

@app.post('/cars/create')
def car_create():
    """Create new car"""

    return None

@app.put('/cars/update')
def car_update():
    """Update existing car"""

    return None

@app.delete('/cars/delete')
def car_delete():
    """Delete existing car"""

    return None

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