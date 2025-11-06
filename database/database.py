from peewee import MySQLDatabase
import os
from dotenv import load_dotenv
import pymysql

pymysql.install_as_MySQLdb()


load_dotenv()

db_url = os.getenv("DATABASE_URL")

import urllib.parse as up
up.uses_netloc.append("mysql")
url = up.urlparse(db_url)

db = MySQLDatabase(
    url.path[1:], 
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
