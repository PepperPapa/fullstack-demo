
def app_demo(environ, start_response):
    start_response("200 OK", [("Content-type", "text/html")])
    return "hello world"
