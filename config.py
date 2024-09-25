# General imports
import os

# Environment imports
from dotenv import load_dotenv

load_dotenv()
env = os.environ.get

DEBUG_MODE = bool(env('DEBUG_MODE'))
HOST = env('HOST')
PORT = int(env('PORT'))

FLASK_SECRET = env('FLASK_SECRET')

SGDB = env('SGDB')
DB_HOST = env('DB_HOST')
DB_USER = env('DB_USER')
DB_PASS = env('DB_PASS')
DB_SCHEMA = env('DB_SCHEMA')

SA_DB_URI = f'{SGDB}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_SCHEMA}'