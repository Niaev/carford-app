"""Integration test for OwnerSevice functions"""

# General imports
from datetime import datetime
import unittest

# Faker imports
from faker import Faker

# Project imports
from index import app, db
from services.OwnerService import OwnerService
from classes.Owners import Owners

class GetOwnersTest(unittest.TestCase):

    def setUp(self):
        self.faker = Faker()

        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()
        self.db = db
    
    def tearDown(self):
        self.context.pop()

    def test_successful_get_all(self):
        """Test successfull case of getting all owners"""

        service = OwnerService(self.db)
        response_json, response_status = service.get_owners()

        expected_status = 200
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 200'
        )

        expected_message = 'Owners successfully gathered'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

class GetOwnerTest(unittest.TestCase):

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
        self.id = this_user.id

    def tearDown(self):

        this_user = Owners.query.filter_by(email=self.email).first()
        self.db.session.delete(this_user)
        self.db.session.commit()

        self.context.pop()

    def test_successful_get_one(self):
        """Test successfull case of gathering only one owner"""

        service = OwnerService(self.db)
        response_json, response_status = service.get_owner(oid=self.id)

        expected_status = 200
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 200'
        )

        expected_message = 'Single owner successfully gathered'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )
    
    def test_unexisting_id(self):
        """Test failure case gathering unexisting owner id"""

        service = OwnerService(self.db)
        response_json, response_status = service.get_owner(oid=0)

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

class CreateOwnerTest(unittest.TestCase):
    def setUp(self):
        self.faker = Faker()

        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()
        self.db = db

    def tearDown(self):
        self.context.pop()

    def test_successful_create(self):
        """Test successful case of owner creation"""

        owner_data = {
            'name': self.faker.name(),
            'email': self.faker.email(),
            'phone': '111111111',
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = OwnerService(self.db)
        response_json, response_status = service.create_owner(**owner_data)

        expected_status = 200
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 200'
        )

        expected_message = 'Owner successfully created'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

        this_owner = Owners.query.filter_by(email=owner_data['email']).first()
        self.db.session.delete(this_owner)
        self.db.session.commit()

    def test_with_existing_email(self):
        """Test failure case of creating owner with existing e-mail"""

        email = self.faker.email()

        owner_data_success = {
            'name': self.faker.name(),
            'email': email,
            'phone': '111111111',
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = OwnerService(self.db)
        response_json, response_status = service.create_owner(**owner_data_success)

        owner_data = {
            'name': self.faker.name(),
            'email': email,
            'phone': '111111111',
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = OwnerService(self.db)
        response_json, response_status = service.create_owner(**owner_data)

        expected_status = 400
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 400'
        )

        expected_message = f'Given Owner email ({email}) is already in use'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

        this_owner = Owners.query.filter_by(email=email).first()
        self.db.session.delete(this_owner)
        self.db.session.commit()

class UpdateOwnerTest(unittest.TestCase):
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
        self.id = this_user.id

    def tearDown(self):

        this_user = Owners.query.filter_by(email=self.email).first()
        self.db.session.delete(this_user)
        self.db.session.commit()

        self.context.pop()

    def test_successful_update(self):
        """Test successfull case of updating owner"""

        owner_data = {
            'oid': self.id,
            'name': self.faker.name(),
            'email': self.email,
            'phone': '999999999',
        }

        service = OwnerService(self.db)
        response_json, response_status = service.update_owner(**owner_data)

        expected_status = 200
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 200'
        )

        expected_message = 'Owner successfully updated'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )
    
    def test_unexisting_id(self):
        """Test failure case of updating with unexisting owner id"""

        owner_data = {
            'oid': 0,
            'name': self.faker.name(),
            'email': self.email,
            'phone': '999999999',
        }

        service = OwnerService(self.db)
        response_json, response_status = service.update_owner(**owner_data)

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

class DeleteOwnerTest(unittest.TestCase):
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
        self.id = this_user.id

        self.deleted = 0

    def tearDown(self):

        if self.deleted == 0:
            this_user = Owners.query.filter_by(email=self.email).first()
            self.db.session.delete(this_user)
            self.db.session.commit()

        self.context.pop()

    def test_successful_delete(self):
        """Test successfull case of deleting owner"""

        owner_data = {
            'oid': self.id,
        }

        service = OwnerService(self.db)
        response_json, response_status = service.delete_owner(**owner_data)

        expected_status = 200
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 200'
        )

        expected_message = 'Owner successfully deleted'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

        self.deleted = 1
    
    def test_unexisting_id(self):
        """Test failure case of updating with unexisting owner id"""

        owner_data = {
            'oid': 0,
        }

        service = OwnerService(self.db)
        response_json, response_status = service.delete_owner(**owner_data)

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