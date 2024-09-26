"""SQLAlchemy Cars database model"""

# Database imports
from index import db

# Models imports
from classes.Owners import Owners

class Cars(db.Model):
    __tablename__ = 'tbl_cars'
    id = db.Column('car_id', db.Integer(), primary_key=True, nullable=False, autoincrement=True, )
    color = db.Column('car_color', db.String(50), nullable=False)
    model = db.Column('car_model', db.String(50), nullable=False)
    created_at = db.Column('car_created_at', db.String(50))

    owner_id = db.Column('car_own_id', db.Integer(), db.ForeignKey(Owners.id), nullable=False)
    owner = db.relationship('Owners', foreign_keys='Cars.owner_id')

    def __repr__(self):
        return f'<Car [{self.id}] {self.color}, {self.model}>'