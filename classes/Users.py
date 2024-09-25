"""SQLAlchemy Users database model"""

# Database imports
from index import db

class Users(db.Model):
    __tablename__ = 'tbl_users'
    id = db.Column('usr_id', db.Integer(), primary_key=True, nullable=False, autoincrement=True, )
    name = db.Column('usr_name', db.String(50), nullable=False)
    email = db.Column('usr_email', db.String(50), nullable=False, unique=True)
    pwd = db.Column('usr_pwd', db.String(200), nullable=False)
    created_at = db.Column('usr_created_at', db.String(50))

    def __repr__(self):
        return f'<User [{self.id}] {self.name}, {self.email}>'