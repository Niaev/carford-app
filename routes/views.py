"""Front-end routes"""

# Web development imports
from flask import session, render_template, redirect, url_for

# Project general imports
from index import app

# Form validation imports
from utils.form_validators import SignUpForm, LoginForm, CreateOwnerForm, CreateCarForm

@app.get('/app')
def index():
    """Health check and index page"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return redirect(url_for('login_page'))

    return redirect(url_for('show_owners_page'))

@app.get('/app/signup')
def signup_page():
    """Display sign up page"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        tags = {
            'title': 'Sign Up',
            'form': SignUpForm()
        }
        
        return render_template('signup.html', **tags)

    return redirect(url_for('show_owners_page'))

@app.get('/app/login')
def login_page():
    """Display log in page"""
    
    # Check user session
    if not 'logged' in session or session['logged'] == '':
        tags = {
            'title': 'Log In',
            'form': LoginForm()
        }
        
        return render_template('login.html', **tags)

    return redirect(url_for('show_owners_page'))

@app.get('/app/owners')
def show_owners_page():
    """Display all owner page"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return redirect(url_for('login_page'))

    tags = {
        'title': 'Owners',
        'owners_active': 'active'
    }

    return render_template('owners.html', **tags)

@app.get('/app/owner/create')
def create_owner_page():
    """Display owner creation form"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return redirect(url_for('login_page'))

    tags = {
        'title': 'Create Owner',
        'owners_active': 'active',
        'form': CreateOwnerForm()
    }

    return render_template('create_owner.html', **tags)

@app.get('/app/owner/update/<int:id>')
def update_owner_page(id:int):
    """Display owner creation form"""

    return None

@app.get('/app/cars')
def show_cars_page():
    """Display all cars page"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return redirect(url_for('login_page'))

    tags = {
        'title': 'Cars',
        'cars_active': 'active'
    }

    return render_template('cars.html', **tags)

@app.get('/app/car/create')
def create_car_page():
    """Display car creation form"""

    # Check user session
    if not 'logged' in session or session['logged'] == '':
        return redirect(url_for('login_page'))

    tags = {
        'title': 'Create Car',
        'cars_active': 'active',
        'form': CreateCarForm()
    }

    return render_template('create_car.html', **tags)

@app.get('/app/car/update/<int:id>')
def update_car_page(id:int):
    """Display car creation form"""

    return None
