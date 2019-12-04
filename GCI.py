import http.server
import socketserver
import os
os.chdir("D:\GCI-2019")
host = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("localhost", 8080), host) as httpd:
    httpd.serve_forever()
