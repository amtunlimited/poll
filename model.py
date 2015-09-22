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

t_globals = {
    'datestr': web.datestr
}

render = web.template.render('templates', base='base', globals=t_globals)

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
		title = db.select('questions', dict(quid=qid), where='qid = $quid')[0].question
		options = db.select('options', dict(quid=qid), where='qid = $quid')
		
		return render.view(title, options)
			
			

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()