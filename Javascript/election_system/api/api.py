import cherrypy
import json
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

    cherrypy.tree.mount(
        Votes(), '/api/votes',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
         }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
