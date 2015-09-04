import os
import cherrypy
import json
import psycopg2

with open('config/config.json') as json_data_file:
    cfg = json.load(json_data_file)

dbname = cfg['dbname']
host = cfg['host']
user = cfg['user']
password = cfg['password']

connection_string = "dbname='%s' user='%s' host='%s' password='%s'" % (dbname,user,host,password)

try:
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    cur.execute("SELECT B.ID, T.DESCRIPTION FROM BALLOT B INNER JOIN TICKET T ON B.TICKET_ID = T.ID;")
    colnames = [desc[0] for desc in cur.description]
    results = [] 
    for row in cur.fetchall():
        results.append(dict(zip(colnames,row)))
    votes = results
    #votes = json.dumps(results,indent=2)
    cur.close()
    conn.close()
    print votes
except:
    print("database connection error")

    votes = {
            '1': {
                'item1': 'Party1',
                'item2': 'Info1'
                },

            '2': {
                'item1': 'Party2',
                'item2': 'Info2'
                },

            '3': {
                'item1': 'Party3',
                'item2': 'Info3'
                }
            }

class Root: pass

class Votes:

    exposed = True

    def GET(self, id=None):

        if id is None:
            return(json.dumps(votes))
        elif id in votes:
            vote = votes[id]

            return(vote)
        else:
            return('No vote with ID %s' % id)

    def POST(self, item1, item2):

        id = str(max([int(_) for _ in votes.keys()]) + 1)

        votes[id] = {
                'item1': item1,
                'item2': item2
                }

        return ('Created new vote with the ID: %s' % id)

    def PUT(self, id, title=None, artist=None):
        if id in votes:
            vote = votes[id]

            vote['item1'] = title or vote['item1']
            vote['item2'] = artist or vote['item2']

            return('Vote ID %s updated' % id)
        else:
            return('No vote with ID %s' % id)

    def DELETE(self, id):
        if id in votes:
            votes.pop(id)

            return('Vote with ID %s has been deleted.' % id)
        else:
            return('No vote with ID %s' % id)


if __name__ == '__main__':
    PATH = os.path.abspath(os.path.dirname(__file__))

    cherrypy.tree.mount(Root(), '/', config={
            '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': PATH,
                'tools.staticdir.index': 'index.html'
                },
            })


    cherrypy.tree.mount(Votes(), '/api/votes', config={
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher()
                },
            })


    cherrypy.engine.start()
    cherrypy.engine.block()
