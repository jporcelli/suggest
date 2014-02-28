"""
Python module for use as server side implementation
of an auto-complete app.

__author__ James Porcelli

"""

from twisted.web import server, resource
from twisted.internet import reactor
import trie
import json

"""
Auto-suggest server uses the event driven
twistedmatrix library for event driven servers
using select, poll, epoll, or kqeue.
"""
class Suggest(resource.Resource):
	isLeaf = True

	"""
	Create the Trie which will then be available in memory
	upon starting of the server
	"""
	def __init__(self):
		# @TODO - Create a logger for this server and
		# log the creation of this resource

		self.t = trie.Trie()

		with open('input.txt', 'rt') as f:
			for line in f:
				self.t.insert(line.strip('\n '))

	"""
	Handle only HTTP GET requests where the prefix
	to search on is specified by the key 'q'
	"""
	def render_GET(self, request):
		q = request.args['q']
		# Return a list of results keyed on the prefix that was
		# used to search with
		return json.dumps({q : self.t.getDescendents(q)})

reactor.listenTCP(8080, server.Site(Suggest()))
reactor.run()




		