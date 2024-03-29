import mysql.connector

# Import the file that contains the database password (local_settings.py) and this file will be ignored by git while pushing
from local_settings import *


def connecter():
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    password=DATABASE_PASSWORD,
    database="cryptodb"
    )
    return db


