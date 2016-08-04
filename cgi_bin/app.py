# python3.5
# os: windows7
# email: zhongxin2506@outlook.com

def app_demo(environ, start_response):
    url = environ["PATH_INFO"]
    start_response("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    if url == "/test.py":
        body = "hello world"
    else:
        body = "404 not found!"
    return [body.encode("utf-8")]
