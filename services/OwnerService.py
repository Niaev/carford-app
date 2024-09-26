"""Service for owners"""

# Project general imports
from classes.Owners import Owners

class OwnerService:
    """"""

    def __init__(self, db):
        self.db = db

    def create_owner(self, name:str, 
        email:str, phone:str, 
        created_at:str):
        """Create new owner"""

        # Check if user email already exists
        owner = Owners.query.filter_by(email=email).first()
        if owner:
            return {
                'message': f'Given Owner email ({email}) is already in use'
            }, 400

        # Create new owner
        new_owner = Owners(
            name=name,
            email=email,
            phone=phone,
            created_at=created_at
        )
        self.db.session.add(new_owner)
        self.db.session.commit()

        return {
            'message': 'Owner successfully created'
        }, 200