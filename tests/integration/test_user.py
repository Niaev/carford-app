"""Integration test for UserSevice functions"""

# General imports
from datetime import datetime
import unittest

# Faker imports
from faker import Faker

# Project imports
from index import app, db
from services.UserService import UserService
from classes.Users import Users

class SignUpUserTest(unittest.TestCase):

    def setUp(self):
        self.faker = Faker()

        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()
        self.db = db

    def tearDown(self):
        self.context.pop()

    def test_successful_signup(self):
        """Test successful case of user creation"""

        pwd = self.faker.sha256()

        user_data = {
            'name': self.faker.name(),
            'email': self.faker.email(),
            'pwd': pwd,
            'cpwd': pwd,
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = UserService(self.db)
        response_json, response_status = service.create_user(**user_data)

        expected_status = 200
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 200'
        )

        expected_message = 'User successfully created'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

        this_user = Users.query.filter_by(email=user_data['email']).first()
        self.db.session.delete(this_user)
        self.db.session.commit()

    def test_signup_with_different_passwords(self):
        """Test failure case of user creation with different password confirmation"""

        user_data = {
            'name': self.faker.name(),
            'email': self.faker.email(),
            'pwd': self.faker.sha256(),
            'cpwd': self.faker.sha256(),
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = UserService(db)
        response_json, response_status = service.create_user(**user_data)

        expected_status = 400
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 400'
        )

        expected_message = 'Given passwords don\'t match'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

    def test_signup_with_existing_email(self):
        """Test failure case of user creation with existing email"""

        email = self.faker.email()
        pwd = self.faker.sha256()

        user_data_success = {
            'name': self.faker.name(),
            'email': email,
            'pwd': pwd,
            'cpwd': pwd,
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = UserService(db)
        response_json, response_status = service.create_user(**user_data_success)

        pwd = self.faker.sha256()

        user_data = {
            'name': self.faker.name(),
            'email': email,
            'pwd': pwd,
            'cpwd': pwd,
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = UserService(db)
        response_json, response_status = service.create_user(**user_data)

        expected_status = 400
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 400'
        )

        expected_message = f'Given email ({email}) is already in use'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

        this_user = Users.query.filter_by(email=user_data_success['email']).first()
        self.db.session.delete(this_user)
        self.db.session.commit()

class AuthUserTest(unittest.TestCase):

    def setUp(self):
        self.faker = Faker()

        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()
        self.db = db

        self.email = self.faker.email()
        self.pwd = self.faker.sha256()

        user_data = {
            'name': self.faker.name(),
            'email': self.email,
            'pwd': self.pwd,
            'cpwd': self.pwd,
            'created_at': datetime.now().strftime('%Y-%m-%d'),
        }

        service = UserService(self.db)
        response_json, response_status = service.create_user(**user_data)

    def tearDown(self):

        this_user = Users.query.filter_by(email=self.email).first()
        self.db.session.delete(this_user)
        self.db.session.commit()

        self.context.pop()

    def test_successful_auth(self):
        """Test successful case of user authentication"""

        service = UserService(self.db)
        response_json, response_status = service.auth_user(
            email=self.email,
            pwd=self.pwd,
            test=True
        )

        expected_status = 200
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 200'
        )

        expected_message = 'User successfully logged'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

    def test_wrong_password(self):
        """Test failure case with wrong password"""

        service = UserService(self.db)
        response_json, response_status = service.auth_user(
            email=self.email,
            pwd=self.faker.sha256()
        )

        expected_status = 400
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 400'
        )

        expected_message = 'E-mail or password incorrect. Please, try again.'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )

    def test_wrong_email(self):
        """Test failure case with wrong password"""

        service = UserService(self.db)
        response_json, response_status = service.auth_user(
            email=self.faker.email(),
            pwd=self.pwd
        )

        expected_status = 400
        self.assertEqual(
            expected_status,
            response_status,
            'Not the expected status 400'
        )

        expected_message = 'E-mail or password incorrect. Please, try again.'
        self.assertEqual(
            expected_message,
            response_json['message'],
            'Not the expected response message'
        )