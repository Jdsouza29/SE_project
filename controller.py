import mysql.connector
import os

from config import config
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=config.get("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=config.get("DB_NAME"),
    port="3306",
    autocommit=config.get("DB_AUTOCOMMIT"),
)

cursor = connection.cursor(buffered=True)

# def checkUser(username, password=None):
#     cmd = f"Select count(username) from user_train where U_ID='{username}' and BINARY Fname='{password}'"
#     cursor.execute(cmd)
#     cmd = None
#     a = cursor.fetchone()[0] >= 1
#     return a