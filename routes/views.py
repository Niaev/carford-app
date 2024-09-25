"""Front-end routes"""

# Project general imports
from index import app

@app.get('/app')
def index():
    """Health check and index page"""

    return None

@app.get('/app/signup')
def signup_page():
    """Display sign up page"""
    
    return None

@app.get('/app/login')
def login_page():
    """Display log in page"""
    
    return None

@app.get('/app/owners')
def show_owners_page():
    """Display all owner page"""

    return None

@app.get('/app/owner/create')
def create_owner_page():
    """Display owner creation form"""

    return None

@app.get('/app/owner/update/<int:id>')
def update_owner_page(id:int):
    """Display owner creation form"""

    return None

@app.get('/app/cars')
def show_cars_page():
    """Display all cars page"""

    return None

@app.get('/app/car/create')
def create_car_page():
    """Display car creation form"""

    return None

@app.get('/app/car/update/<int:id>')
def update_car_page(id:int):
    """Display car creation form"""

    return None
