# -*- coding: utf-8 -*- 
#!/usr/bin/python3.5
# win7环境

from wsgiref.simple_server import make_server
from cgi_bin.app import app_demo

"""
def app_demo(environ, start_response):
    url = environ["PATH_INFO"]
    start_response("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    if url == "/test.py":
        body = "hello world"
    else:
        body = "404 not found!"
    return [body.encode("utf-8")]
"""

httpd = make_server('', 8008, app_demo)
print("Serving HTTP on port 8000...")

# Respond to requests until process is killed
httpd.serve_forever()

# Alternative: serve one request, then exit
httpd.handle_request()
