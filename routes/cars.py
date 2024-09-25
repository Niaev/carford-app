"""Cars related routes"""

# Project general imports
from index import app, db
from classes.Cars import Cars

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

    return None

@app.get('/cars/<int:id>')
def get_one_car(id:int):
    """Gather one car data"""

    return None