"""Integration test for CarSevice functions"""

# General imports
from datetime import datetime
import unittest
import random

# Faker imports
from faker import Faker

# Project imports
from index import app, db
from services.OwnerService import OwnerService
from services.CarService import CarService
from classes.Owners import Owners
from classes.Cars import Cars

class GetCarsTest(unittest.TestCase):

    def setUp(self):
        self.faker = Faker()

        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()
        self.db = db
    
    def tearDown(self):
        self.context.pop()

    def test_successful_get_all(self):
        """Test successfull case of getting all cars"""

        service = CarService(self.db)
        response_json, response_status = service.get_cars()

        expected_status = 200
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 200'
        )

        expected_message = 'Cars successfully gathered'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

class GetCarTest(unittest.TestCase):

    def setUp(self):
        self.faker = Faker()

        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()
        self.db = db

        self.email = self.faker.email()

        owner_data = {
            'name': self.faker.name(),
            'email': self.email,
            'phone': '111111111',
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = OwnerService(self.db)
        response_json, response_status = service.create_owner(**owner_data)

        this_user = Owners.query.filter_by(email=self.email).first()
        self.owner_id = this_user.id

        car_data = {
            'oid': self.owner_id,
            'color': random.choice(['gray', 'blue', 'yellow']),
            'model': random.choice(['hatch', 'sedan', 'convertible']),
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = CarService(self.db)
        response_json, response_status = service.create_car(**car_data)

        this_car = Cars.query.order_by(Cars.id.desc()).first()
        self.car_id = this_car.id

    def tearDown(self):

        this_car = Cars.query.filter_by(id=self.car_id).first()
        self.db.session.delete(this_car)
        self.db.session.commit()

        self.context.pop()

    def test_successful_get_one(self):
        """Test successfull case of gathering only one car"""

        service = CarService(self.db)
        response_json, response_status = service.get_car(cid=self.car_id)

        expected_status = 200
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 200'
        )

        expected_message = 'Single car successfully gathered'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )
    
    def test_unexisting_id(self):
        """Test failure case gathering unexisting car id"""

        service = CarService(self.db)
        response_json, response_status = service.get_car(cid=0)

        expected_status = 400
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 400'
        )

        expected_message = 'Given car id doesn\'t exist'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

class CreateCarTest(unittest.TestCase):
    def setUp(self):
        self.faker = Faker()

        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()
        self.db = db

        self.email = self.faker.email()

        owner_data = {
            'name': self.faker.name(),
            'email': self.email,
            'phone': '111111111',
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = OwnerService(self.db)
        response_json, response_status = service.create_owner(**owner_data)

        this_user = Owners.query.filter_by(email=self.email).first()
        self.owner_id = this_user.id

    def tearDown(self):
        self.context.pop()

    def test_successful_create(self):
        """Test successful case of car creation"""

        car_data = {
            'oid': self.owner_id,
            'color': random.choice(['gray', 'blue', 'yellow']),
            'model': random.choice(['hatch', 'sedan', 'convertible']),
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = CarService(self.db)
        response_json, response_status = service.create_car(**car_data)

        expected_status = 200
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 200'
        )

        expected_message = 'Car successfully created'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

        this_car = Cars.query.order_by(Cars.id.desc()).first()
        self.db.session.delete(this_car)
        self.db.session.commit()

    def test_with_uexisting_owner(self):
        """Test failure case of creating car with existing owner"""

        car_data = {
            'oid': 0,
            'color': random.choice(['gray', 'blue', 'yellow']),
            'model': random.choice(['hatch', 'sedan', 'convertible']),
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = CarService(self.db)
        response_json, response_status = service.create_car(**car_data)

        expected_status = 400
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 400'
        )

        expected_message = f'Given owner id doesn\'t exist'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

class UpdateCarTest(unittest.TestCase):
    def setUp(self):
        self.faker = Faker()

        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()
        self.db = db

        self.email = self.faker.email()

        owner_data = {
            'name': self.faker.name(),
            'email': self.email,
            'phone': '111111111',
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = OwnerService(self.db)
        response_json, response_status = service.create_owner(**owner_data)

        this_user = Owners.query.filter_by(email=self.email).first()
        self.owner_id = this_user.id

        car_data = {
            'oid': self.owner_id,
            'color': random.choice(['gray', 'blue', 'yellow']),
            'model': random.choice(['hatch', 'sedan', 'convertible']),
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = CarService(self.db)
        response_json, response_status = service.create_car(**car_data)

        this_car = Cars.query.order_by(Cars.id.desc()).first()
        self.car_id = this_car.id

    def tearDown(self):

        this_car = Cars.query.filter_by(id=self.car_id).first()
        self.db.session.delete(this_car)
        self.db.session.commit()

        self.context.pop()

    def test_successful_update(self):
        """Test successfull case of updating car"""

        car_data = {
            'cid': self.car_id,
            'oid': self.owner_id,
            'color': random.choice(['gray', 'blue', 'yellow']),
            'model': random.choice(['hatch', 'sedan', 'convertible'])
        }

        service = CarService(self.db)
        response_json, response_status = service.update_car(**car_data)

        expected_status = 200
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 200'
        )

        expected_message = 'Car successfully updated'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )
    
    def test_unexisting_id(self):
        """Test failure case of updating with unexisting car id"""

        car_data = {
            'cid': 0,
            'oid': self.owner_id,
            'color': random.choice(['gray', 'blue', 'yellow']),
            'model': random.choice(['hatch', 'sedan', 'convertible'])
        }

        service = CarService(self.db)
        response_json, response_status = service.update_car(**car_data)

        expected_status = 400
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 400'
        )

        expected_message = 'Given car id doesn\'t exist'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

    def test_unexisting_owner_id(self):
        """Test failure case of updating with unexisting owner id"""

        car_data = {
            'cid': self.car_id,
            'oid': 0,
            'color': random.choice(['gray', 'blue', 'yellow']),
            'model': random.choice(['hatch', 'sedan', 'convertible'])
        }

        service = CarService(self.db)
        response_json, response_status = service.update_car(**car_data)

        expected_status = 400
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 400'
        )

        expected_message = 'Given owner id doesn\'t exist'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

class DeleteCarTest(unittest.TestCase):
    def setUp(self):
        self.faker = Faker()

        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()
        self.db = db

        self.email = self.faker.email()

        owner_data = {
            'name': self.faker.name(),
            'email': self.email,
            'phone': '111111111',
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = OwnerService(self.db)
        response_json, response_status = service.create_owner(**owner_data)

        this_user = Owners.query.filter_by(email=self.email).first()
        self.owner_id = this_user.id

        car_data = {
            'oid': self.owner_id,
            'color': random.choice(['gray', 'blue', 'yellow']),
            'model': random.choice(['hatch', 'sedan', 'convertible']),
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = CarService(self.db)
        response_json, response_status = service.create_car(**car_data)

        this_car = Cars.query.order_by(Cars.id.desc()).first()
        self.car_id = this_car.id

        self.deleted = 0

    def tearDown(self):

        if self.deleted == 0:
            this_car = Cars.query.order_by(Cars.id.desc()).first()
            self.db.session.delete(this_car)
            self.db.session.commit()

        self.context.pop()

    def test_successful_delete(self):
        """Test successfull case of deleting car"""

        car_data = {
            'cid': self.car_id,
        }

        service = CarService(self.db)
        response_json, response_status = service.delete_car(**car_data)

        expected_status = 200
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 200'
        )

        expected_message = 'Car successfully deleted'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

        self.deleted = 1
    
    def test_unexisting_id(self):
        """Test failure case of updating with unexisting car id"""

        car_data = {
            'cid': 0,
        }

        service = CarService(self.db)
        response_json, response_status = service.delete_car(**car_data)

        expected_status = 400
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 400'
        )

        expected_message = 'Given car id doesn\'t exist'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )