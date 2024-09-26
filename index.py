"""Flask app base file"""

# Web development imports
from flask import Flask
from flask_cors import CORS

# Database imports
from flask_sqlalchemy import SQLAlchemy

# Environment variables
from config import FLASK_SECRET, SA_DB_URI, HOST, PORT, DEBUG_MODE

# Initialize Flask app
app = Flask(__name__)
CORS(app) # Enable CORS for Flask app

# Configure app
## Flask session secret and more
app.secret_key = FLASK_SECRET
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax'
)
## ORM configuration
app.config['SQLALCHEMY_DATABASE_URI'] = SA_DB_URI
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 3600
}

# SQL Alchemy database instance
db = SQLAlchemy(app)

from routes import * 

# Create all tables
with app.app_context():
    db.create_all()

# Development server execution
if __name__ == '__main__':
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG_MODE
    )