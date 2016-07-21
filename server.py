# python3.4
# very simple socket server
# just for verify how bowser can request an image file
# and display normally

"""
steps to test:
1.download server.py and google.png to your local machine.
2.cd to that directory same as server.py's.
3.run command "python server.py"
4.using the browser request url "http://127.0.0.1:8008/google.png"
5.google.png should be display normally.
"""
import socket

HOST = ""
PORT = 8008

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print("conn: ", conn)
print("add: ", addr)
print("\n\n==zx==\n\n")
request = conn.recv(1024).decode("utf-8")
print(request, type(request))
print("\n\n==zx==\n\n")
request = request.split("\r\n")
rurl = request[0].split()[1]
print(rurl)

# response for url '/'
response = """
HTTP/1.1 200 OK
Server: python socket
Content-Type: text/html

<html>
  <head>
    <title>hi</title>
  </head>
  <body>
    <h1>Hello {0}</h1>
  </body>
</html>
"""

# response header for request url '/google.png'
headers = """
HTTP/1.1 200 OK
Content-Type: image/png

"""

# read the image file, the open mode should be 'rb', must include 'b'
f = open("google.png", 'rb')
img_data = f.read()
f.close()

# process for url '/'
if (rurl == "/"):
    conn.sendall(response.format("index").encode("utf-8"))
# process for url '/google.png'    
if rurl == "/google.png":
    conn.sendall(headers.encode("utf-8"))
    # the type of img_data is 'bytes'
    conn.sendall(img_data)
    
