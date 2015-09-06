import json

class API:

    exposed = True

    def __init__(self,dct={}):
        self.items = dct

    def GET(self, id=None):

        if id is None:
            return(json.dumps(self.items))
        elif id in self.items:
            item = self.items[id]
            return(json.dumps(item))
        else:
            return("{}")

    def POST(self, description):

        #update with uuid
        id = str(max([int(_) for _ in self.items.keys()]) + 1)

        self.items[id] = {
                'description': description
                }

        return ('Created ID: %s' % id)

    def PUT(self, id, title=None, artist=None):

        #need to fix put
        if id in self.items:
            item = self.items[id]

            item['description'] = description or item['description']

            return('ID %s updated' % id)
        else:
            return('No ID %s' % id)

    def DELETE(self, id):
        if id in items:
            items.pop(id)

            return('ID %s deleted.' % id)
        else:
            return('No ID %s' % id)

