"""Service for owners"""

# Project general imports
from classes.Owners import Owners

class OwnerService:
    """"""

    def __init__(self, db):
        self.db = db

    def get_owners(self):
        """Get all registered owners"""

        # Get all owners ordered by id
        owners = Owners.query.order_by(Owners.id).all()

        # Transform all owner objects in json format
        owners_json = []
        for owner in owners:
            owners_json.append({
                'id': owner.id,
                'name': owner.name,
                'email': owner.email,
                'phone': owner.phone,
                'created_at': owner.created_at
            })

        return {
            'message': 'Owners successfully gathered',
            'owners': owners_json
        }, 200

    def get_owner(self, oid:int):
        """Get one single registered owner by its id"""

        # Get single owner by id
        owner = Owners.query.filter_by(id=oid).first()
        if not owner:
            return {
                'message': 'Given owner id doesn\'t exist'
            }, 400

        return {
            'message': 'Single owner successfully gathered',
            'owner': {
                'id': owner.id,
                'name': owner.name,
                'email': owner.email,
                'phone': owner.phone,
                'created_at': owner.created_at
            }
        }, 200

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

    def update_owner(self, oid: int, 
        name:str, email:str, 
        phone:str):
        """Update existing owner"""

        # Check if owner exists
        owner = Owners.query.filter_by(id=oid).first()
        if not owner:
            return {
                'message': 'Given owner id doesn\'t exist'
            }, 400

        # Update owner data
        owner.name = name
        owner.email = email
        owner.phone = phone
        self.db.session.commit()

        return {
            'message': 'Owner successfully updated'
        }, 200