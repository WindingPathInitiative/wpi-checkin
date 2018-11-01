from peewee import *
from app import config

db = MySQLDatabase(config['db']['database'],user=config['db']['username'],password=config['db']['password'], host=config['db']['host'], port=config['db']['port'])

class Event(Model):
	id = IntegerField(primary_key=True)
	orgId = IntegerField()
	name = CharField()

	class Meta:
		database = db # This model uses the "people.db" database.
		
def create_tables():
    with db:
        db.create_tables([Event])