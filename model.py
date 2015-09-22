#!/usr/bin/python

'''model.py: The Web.py controller for a simple poll application.
Written by: Aaron Tagliaboschi <aaron.tagliaboschi@gmail.com>
'''

#A view list:
#	main: Lists out current polls
#	create: make a new poll
#	view: A more detailed view of a particular poll

import web

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

class main:
	def GET(self):
		return "main"

class create:
	def GET(self):
		return "create"

class view:
	def GET(self, qid):
		return "view " + qid

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()