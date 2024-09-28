"""Service for users"""

# Web development imports
from flask import session
from flask_bcrypt import generate_password_hash, check_password_hash

# Project general imports
from classes.Users import Users

class UserService:
    """"""

    def __init__(self, db):
        self.db = db

    def create_user(self, name:str, 
        email:str, pwd:str, 
        cpwd:str, created_at:str):
        """Create new user"""

        # Checking password
        if pwd != cpwd:
            return {
                'message': 'Given passwords don\'t match'
            }, 400

        # Check if user email already exists
        user = Users.query.filter_by(email=email).first()
        if user:
            return {
                'message': f'Given email ({email}) is already in use'
            }, 400

        # Update password hash
        pwd = generate_password_hash(pwd).decode('utf-8')

        # Create new user
        new_user = Users(
            name=name,
            email=email,
            pwd=pwd,
            created_at=created_at
        )
        self.db.session.add(new_user)
        self.db.session.commit()

        return {
            'message': 'User successfully created'
        }, 200

    def auth_user(self, email:str, pwd:str, test=False):
        """Authenticate user"""

        # Check if user exists
        user = Users.query.filter_by(email=email).first()
        if user:
            # Check password
            check_pwd = check_password_hash(user.pwd, pwd)
            if check_pwd:
                # Create session
                if not test:
                    session['logged'] = user.email
                    session.new = True
                    session.modified = True
                return {
                    'message': 'User successfully logged'
                }, 200
        
        return {
            'message': 'E-mail or password incorrect. Please, try again.'
        }, 400