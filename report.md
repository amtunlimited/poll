#Web Based Polling System
Designed and programmed by Aaron Tagliaboschi

##Summary
This project required a web interface to a database-driven polling system. Users
should be able to make a new poll with new options, and users should be able to 
see how many votes there have been and how many votes for each option

##Project Analysis and Design
For this project I decided to use SQLite for my database and Python as my server-
side language. I started by making all of the views (create, view, vote, and
list). I ended up consolidating the vote and view lists. I built up the project
by first being able to list the options, then being able to list the questions, 
then being able to vote, then creating questions. The project was relitively 
simple, but this much database-driven design meant keeping a lot of things in
the head.

##User Manual
The design of the program is pretty much self-explanitory. You start off in The
'main' view, where you get your list of polls. Click on a poll to see the number
of vote and vote for a new one. On the main view is also the "Create a new poll"
link to go to the creation page. Once you've filled out the form, you'll be
redirected to the new poll.

##Known Problems
I completely forgot about the graph display, so that was unimplemented. When you
submit a vote, it redirects you, so it will add another entry to your browser
history and if you hit "back" you'll be redirected again.