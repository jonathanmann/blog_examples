import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs

PORT = 8080
paths = 'html/part1.html','html/part2.html','data/nodes.dat','data/links.dat'

def get_f_txt(path):
    with open(path,'r') as f:
        return f.read()

part1 = get_f_txt(paths[0])
part2 = get_f_txt(paths[1])
nodes = get_f_txt(paths[2])
links = get_f_txt(paths[3])

class LinkHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = part1 + "var nodes =  [" + nodes + "] \n" + "var links = [" + links + "] \n" + part2
        self.wfile.write(bytes(html, "utf8"))
        return

handler_object = LinkHttpRequestHandler
link_server = socketserver.TCPServer(("", PORT), handler_object)
link_server.serve_forever()
