#!/usr/bin/python
"""
This module defines a basic HTTP server using http.server """

import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class RequestHandler(BaseHTTPRequestHandler):
    """ Custom request handler for our simple HTTP server.
    Inherits from BaseHTTPRequestHandler to handle HTTP requests."""
    def do_GET(self):
        """ Handle the GET requests """
        # Handles request to the root '/' endpoint
        if self.path == '/':
            self.send_response(200, message='OK')
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Handles requesst to the '/data' endpoint
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            json_string = json.dumps(data)
            self.send_response(200, message='OK')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json_string.encode('utf-8'))

        # Handles to the '/status' endpoint
        elif self.path == '/status':
            self.send_response(200, message='OK')
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        # Handles all other unknown endpoints
        else:
            self.send_response(404, message='Not Found')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Hello, this is a simple API!")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
