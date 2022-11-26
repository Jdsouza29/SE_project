import mysql.connector
import os

from config import config
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pes1ug20cs652_rr',
    port="3306"
)

cursor = connection.cursor(buffered=True)

# def checkUser(username, password=None):
#     cmd = f"Select count(username) from user_train where U_ID='{username}' and BINARY Fname='{password}'"
#     cursor.execute(cmd)
#     cmd = None
#     a = cursor.fetchone()[0] >= 1
#     return a