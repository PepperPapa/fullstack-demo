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
    else:
        body = "404 not found!"
    return [body.encode("utf-8")]
