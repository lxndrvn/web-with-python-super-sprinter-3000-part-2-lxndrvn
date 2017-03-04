from connect import ConnectDatabase
from peewee import *


class BaseModel(Model):
	class Meta:
		database = ConnectDatabase.db

class Story(Model):
	title = CharField()
	text = CharField()
	criteria = CharField()
	business_value = IntegerField()
	estimation = FloatField()
	status = CharField()
