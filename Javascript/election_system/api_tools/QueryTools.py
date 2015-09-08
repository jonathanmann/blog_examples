import json

class QueryTools:
    """
    QueryTools : convert the results of a query to a python dictionary using the first column as the dictionary key
    """

    def __init__(self,query,write=False,config_file='api_tools/config/config.json'):
        """
        Connect to the database using the provided config file and fetch the result
        """
        import psycopg2
        self.conf = config_file
        conn_str = self.get_conn_str()
        conn = psycopg2.connect(conn_str)
        cur = conn.cursor()
        cur.execute(query)
        if write:
            conn.commit()
            print 'committed'
        else:
            self.data = cur.fetchall()
            self.cols = [desc[0] for desc in cur.description]
            self.result_dict = self.get_dict()
            self.result_json = json.dumps(self.result_dict)
        cur.close()
        conn.close()

    def get_conn_str(self):
        """
        @return : database connection string
        """
        with open(self.conf) as json_data_file:
            cfg = json.load(json_data_file)
        dbname = cfg['dbname']
        host = cfg['host']
        user = cfg['user']
        password = cfg['password']
        return "dbname='%s' user='%s' host='%s' password='%s'" % (dbname,user,host,password)

    def get_dict(self):
        d = {}
        for row in self.data:
            d[row[0]] = dict(zip(self.cols[1:],row[1:]))
        return d

    def get_attr_list(self):
        j = [] 
        for row in self.data:
            j.append(dict(zip(self.cols,row)))
        return j
            


