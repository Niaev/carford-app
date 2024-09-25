"""User related routes"""

# Project general imports
from index import app, db
from classes.Users import Users

@app.post('/users/signup')
def user_signup():
    """Sign Up user"""

    return None

@app.post('/users/login')
def user_login():
    """Log In user"""

    return None

@app.post('/users/logout')
def user_logout():
    """Log Out current user"""

    return None