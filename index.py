#!/usr/bin/python

'''index.py: The Web.py controller for a simple poll application.
Written by: Aaron Tagliaboschi <aaron.tagliaboschi@gmail.com>
'''

#A view list:
#	main: Lists out current polls
#	create: make a new poll
#	vote: vote on a poll
#	view: A more detailed view of a particular poll

import web

#This decides what class to use based on regular expressions
urls = (
	'/poll/','main',
	'/poll/create/', 'create',
	'/poll/vote/(.*)', 'vote',
	'/poll/view/(.*)', 'view'
)

class main:
	def GET(self):
		return "main"

class create:
	def GET(self):
		return "create"

class vote:
	def GET(self, qid):
		return "vote " + qid

class view:
	def GET(self, qid):
		return "view " + qid

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()