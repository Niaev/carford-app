"""Service for cars"""

# Project general imports
from classes.Cars import Cars

class CarService:
    """"""

    def __init__(self, db):
        self.db = db

    def get_cars(self):
        """Get all registered cars"""

        # Get all cars ordered by id
        cars = Cars.query.order_by(Cars.id).all()

        # Transform all car objects in json format
        cars_json = []
        for car in cars:
            cars_json.append({
                'id': car.id,
                'color': car.color,
                'model': car.model,
                'owner': {
                    'id': car.owner.id,
                    'name': car.owner.name,
                    'email': car.owner.email,
                    'phone': car.owner.phone,
                    'created_at': car.owner.created_at
                },
                'created_at': car.created_at
            })

        return {
            'message': 'Cars successfully gathered',
            'cars': cars_json
        }, 200

    def get_car(self, cid:int):
        """Get one single registered car by its id"""

        # Get single car by id
        car = Cars.query.filter_by(id=cid).first()
        if not car:
            return {
                'message': 'Given car id doesn\'t exist'
            }, 400

        return {
            'message': 'Single car successfully gathered',
            'car': {
                'id': car.id,
                'color': car.color,
                'model': car.model,
                'owner': {
                    'id': car.owner.id,
                    'name': car.owner.name,
                    'email': car.owner.email,
                    'phone': car.owner.phone,
                    'created_at': car.owner.created_at
                },
                'created_at': car.created_at
            }
        }, 200