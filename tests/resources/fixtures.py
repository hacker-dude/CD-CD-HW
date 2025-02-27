import pytest
import pymssql
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="module")
def db_connection():

    server=os.getenv('SERVER')
    database=os.getenv('DATABASE')
    user=os.getenv('USER')
    password=os.getenv('PASSWORD')

    connection = pymssql.connect(server, user, password, database)

    yield connection
    connection.close()

@pytest.fixture(scope="function")
def db_cursor(db_connection):
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()
