import json
import uuid
from QueryTools import QueryTools

class API:

    exposed = True

    def __init__(self,query,attr=False):
        if attr:
            self.items = QueryTools(query).get_attr_list()
        else:
            self.items = QueryTools(query).result_dict

    def GET(self, u_id=None):

        if u_id is None:
            return(json.dumps(self.items))
        elif u_id in self.items:
            item = self.items[u_id]
            return(json.dumps(item))
        else:
            return("{}")

    def POST(self, dct):

        u_id = uuid.uuid4()
        d = eval(dct)
        t = d["table"]
        t_id = d["ticket_id"]
        stmt = "insert into " + str(t) + " select '" + str(u_id) + "' id, '" + t_id + "' ticket_id"
        try:
            QueryTools(stmt,write=True)
            return ('{"success": true,"message" : "%s"}' % u_id)
        except:
            return ('{"success": false,"message" : "%s"}' % u_id)

    """

    def PUT(self, u_id, dct):

        #fix put
        if u_id in self.items:
            item = self.items[u_id]

            return('ID %s updated' % u_id)
        else:
            return('No ID %s' % u_id)

    def DELETE(self, u_id):
        if id in items:
            items.pop(u_id)

            return('ID %s deleted.' % u_id)
        else:
            return('No ID %s' % u_id)
    """

