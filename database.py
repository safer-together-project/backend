import os
import mysql.connector as database

username = os.environ.get("DB_USER")
password = os.environ.get("DB_SECRET")
localhost = os.environ.get("DB_HOST")
database = os.environ.get("DB_NAME")

connection = database.connect(
    user=username,
    password=password,
    host=localhost,
    database=database)

cursor = connection.cursor()

