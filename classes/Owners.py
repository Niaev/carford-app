"""SQLAlchemy Owners database model"""

# Database imports
from index import db

class Owners(db.Model):
    __tablename__ = 'tbl_owners'
    id = db.Column('own_id', db.Integer(), primary_key=True, nullable=False, autoincrement=True, )
    name = db.Column('own_name', db.String(50), nullable=False)
    email = db.Column('own_email', db.String(50), nullable=False, unique=True)
    phone = db.Column('own_phone', db.String(50), nullable=False)
    created_at = db.Column('own_created_at', db.String(50))

    def __repr__(self):
        return f'<Owner [{self.id}] {self.name}, {self.email}>'