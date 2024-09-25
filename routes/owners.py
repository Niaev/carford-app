"""Owners related routes"""

# Project general imports
from index import app, db
from classes.Owners import Owners

@app.post('/owners/create')
def owner_create():
    """Create new owner"""

    return None

@app.put('/owners/update')
def owner_update():
    """Update existing owner"""

    return None

@app.delete('/owners/delete')
def owner_delete():
    """Delete existing owner"""

    return None

@app.get('/owners')
def get_all_owners():
    """Gather all owners"""

    return None

@app.get('/owners/<int:id>')
def get_one_owner(id:int):
    """Gather one owner data"""

    return None