import sys
import urllib
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
import time
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
import requests
from urllib.parse import urlparse

class ServerRequestHandler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.0"
    server_version = "PSHS/0.1"
    sys_version = "Python/3.6.x"

    def handler(self):
        print("data:", self.rfile.readline().decode())
        self.wfile.write(self.rfile.readline())

    def do_GET(self):

        print("Accept Get:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        parsed_result = urlparse(self.path)
        query = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(self.path).query))
        print(parsed_result)
        print(query)

        data = {
            'code': 200
        }
        print(requests)

        try:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            # self.wfile.write(json.dumps(self.headers))
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

            print("socket", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        except IOError:
            print("socket.error : Connection broke. ")

    def do_POST(self):

        print(self.headers)
        print(self.command)

        req_datas = self.rfile.read(int(self.headers['content-length']))  # 重点在此步!
     #   req_date_head = req_datas['']
        print(req_datas.decode())

        data = {
            'code' : 200
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_HEAD(self):
        self._set_headers()

def run(server_class=HTTPServer, handler_class=ServerRequestHandler, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # set the target where to mkdir, and default "D:/web"
        ServerRequestHandler.target = sys.argv[1]
    try:
        server = HTTPServer(("", 8001), ServerRequestHandler)
        print("HTTPServer started, serving at http://localhost:8001")
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()