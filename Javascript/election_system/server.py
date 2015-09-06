#!/usr/bin/python
import os
import cherrypy
from pg_tools.QueryTools import QueryTools
from api_tools.APITools import API

vote_query = "SELECT B.ID, T.DESCRIPTION FROM BALLOT B INNER JOIN TICKET T ON B.TICKET_ID = T.ID;"
votes = QueryTools(vote_query).result_dict

ticket_query = "SELECT DESCRIPTION AS NAME FROM TICKET"
tickets = QueryTools(ticket_query).get_attr_list()

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

    cherrypy.tree.mount(API(votes), '/api/votes', config={
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher()
                },
            })

    cherrypy.tree.mount(API(tickets), '/api/tickets', config={
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher()
                },
            })

    cherrypy.engine.start()
    cherrypy.engine.block()
