from peewee import CharField, DateTimeField, Model
from database.database import db
import datetime

class Cliente(Model):
    nome = CharField()
    gmail = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta: 
        database = db