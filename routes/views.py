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

@app.get('/app/users')
def show_users_page():
    """Display all users page"""

    return None

@app.get('/app/user/create')
def create_user_page():
    """Display user creation form"""

    return None

@app.get('/app/user/update/<int:id>')
def update_user_page(id:int):
    """Display user creation form"""

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
