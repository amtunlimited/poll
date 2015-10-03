#!/usr/bin/python

'''model.py: The Web.py controller for a simple poll application.
Written by: Aaron Tagliaboschi <aaron.tagliaboschi@gmail.com>
'''

#A view list:
#	main: Lists out current polls
#	create: make a new poll
#	view: A more detailed view of a particular poll

import web, datetime

#This decides what class to use based on regular expressions
urls = (
	'/poll/','main',
	'/poll/create/', 'create',
	'/poll/view/(.*)', 'view'
)

#These are variables tat will be used in every class.
#Render uses the templating language "Templator" to make templates.
render = web.template.render('templates', base='base')
#This makes a connection to the database. Here I'm using SQLite because I didn't
#feel like setting up MySQL on my server. Maybe later...
db = web.database(dbn='sqlite', db='poll.db')

class main:
	def GET(self):
		polls = db.select('questions', order='qid DESC')
		return render.main(polls)

class create:
	def GET(self):
		return "create"

class view:
	def GET(self, qid):
		title = db.select('questions', dict(quid=qid), where='qid = $quid')[0]
		options = db.select('options', dict(quid=qid), where='qid = $quid')
		count = db.query(
			'SELECT options.option AS option, count(vote.vid) AS count \
			FROM vote JOIN options \
			WHERE options.oid=vote.oid AND qid = $quid \
			GROUP BY vote.oid', 
			vars={'quid':qid}
		)
		
		return render.view(title, count, options)
		#return count
		
	def POST(self, qid):
		data = web.input()
		db.insert('vote', oid=data.oid)
		
		raise web.seeother("/poll/view/" + qid)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()