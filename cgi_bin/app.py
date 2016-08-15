# python3.5
# os: windows7
# email: zhongxin2506@outlook.com

def app_demo(environ, start_response):
    url = environ["PATH_INFO"]
    if url == "/test.py":
        start_response("200 OK", [("Content-Type", "text/html;charset=utf-8")])
        body = "hello world"
    elif url == "/json.py":
        start_response("200 OK", [("Content-Type", "application/json;charset=utf-8")])
        body = '{"name": "zx", "password": "1234"}'
    elif url == "/redirect.py":
        start_response("303 OK", [("Content-Type", "text/plain;charset=utf-8"),
                                                        ("Location", "http://127.0.0.1:8000/redirect.html")])
        body = ""
    elif url == "/cookie.py":
        start_response("200 OK", [("Content-Type", "text/plain;charset=utf-8"),
                                                        ("Set-Cookie", "name=pepperpapa; domain=127.0.0.1; Expires=Sun, 14-Dec-16 00:00:00 GMT")])
        body = ""
    else:
        body = "404 not found!"
    return [body.encode("utf-8")]
