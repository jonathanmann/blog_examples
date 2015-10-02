#!/usr/bin/python
import os
import cherrypy
from api_tools.QueryTools import QueryTools
from api_tools.APITools import API

vote_query = "SELECT B.ID, T.DESCRIPTION FROM BALLOT B INNER JOIN TICKET T ON B.TICKET_ID = T.ID;"
ticket_query = "SELECT ID, DESCRIPTION AS NAME FROM TICKET;"

class Root: pass

if __name__ == '__main__':
    PATH = os.path.abspath(os.path.dirname(__file__))

    cherrypy.tree.mount(Root(), '/', config={
            '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': PATH,
                'tools.staticdir.index': 'index.html'
                },
            })

    cherrypy.tree.mount(API(vote_query), '/api/votes', config={
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher()
                },
            })

    cherrypy.tree.mount(API(ticket_query,True), '/api/tickets', config={
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher()
                },
            })

    cherrypy.engine.start()
    cherrypy.engine.block()
