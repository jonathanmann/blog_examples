import json
import uuid

class API:

    exposed = True

    def __init__(self,dct={}):
        self.items = dct

    def GET(self, u_id=None):

        if u_id is None:
            return(json.dumps(self.items))
        elif u_id in self.items:
            item = self.items[u_id]
            return(json.dumps(item))
        else:
            return("{}")

    def POST(self, description):
        u_id = uuid.uuid4()
        self.items[u_id] = {
                'description': description
                }

        return ('Created ID: %s' % u_id)

    def PUT(self, u_id, title=None, artist=None):

        #need to fix put
        if u_id in self.items:
            item = self.items[u_id]

            item['description'] = description or item['description']

            return('ID %s updated' % u_id)
        else:
            return('No ID %s' % u_id)

    def DELETE(self, u_id):
        if id in items:
            items.pop(u_id)

            return('ID %s deleted.' % u_id)
        else:
            return('No ID %s' % u_id)

