#!/usr/bin/python
# encoding : utf-8
from flup.server.fcgi import WSGIServer

def myapp(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    # 服务器端打印environ的所有信息
    for k, v in environ.items():
        print(k, ":", v)
    return ['Hello World!\n']

if __name__  == '__main__':
    WSGIServer(myapp,bindAddress=('127.0.0.1',8008)).run()
