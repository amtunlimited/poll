import web, datetime

db = web.database(dbn='sqlite', db='poll.db')

def get_polls():
	db.select(