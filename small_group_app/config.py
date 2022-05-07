import json
import os

LOCAL_DEVELOPMENT = True
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
PARENT_DIR = os.path.dirname(ROOT_DIR)

if not LOCAL_DEVELOPMENT:
    MARIADB_CREDENTIALS_PATH = None
else:
    MARIADB_CREDENTIALS_PATH = os.path.join(PARENT_DIR,'mariadb_connection.local.json')

with open(MARIADB_CREDENTIALS_PATH, 'rb') as fp:
    mariadb_creds = json.load(fp)

class Config:

    SECRET_KEY = "LKJHOIHoih98y98"
    
    # Maria DB settings
    MARIADB_CREDENTIALS_PATH = MARIADB_CREDENTIALS_PATH
    MARIADB_SERVER = mariadb_creds.get('server')
    MARIADB_PORT = mariadb_creds.get('port')
    MARIADB_DATABASE = mariadb_creds.get('database')
    MARIADB_USER = mariadb_creds.get('user')
    MARIADB_PASSWORD = mariadb_creds.get('password')

    SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://{}:{}@{}:{}/{}'.format(
        MARIADB_USER,
        MARIADB_PASSWORD,
        MARIADB_SERVER,
        MARIADB_PORT,
        MARIADB_DATABASE,
    )
    
