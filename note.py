#Заметка
import datetime

class Note:
	def __init__(self, id, title, body, time_last_edition = datetime.datetime.now()):
		self.id = id
		self.title = title
		self.body = body
		self.time_last_edition = time_last_edition

	def set_title(new_title):
		self.title = new_title
		self.time_last_edition = datetime.datetime.now()

	def set_body(new_body):
		self.body = new_body
		self.time_last_edition = datetime.datetime.now()