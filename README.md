# windows下nginx代理python server的简单配置

> 该示例主要目的是实现nginx代理静态文件，python server执行python脚本处理客户端的动态数据请求，nginx代理python server。
 为了尽量使用python原生的库，本示例使用的是nginx的http代理方式，未使用fastcgi、uwsgi等代理方式，python wsgi接口的相关配置
 本示例目前实现还比较简单，持续更新中...

1. 操作系统环境
   windows7
2. python版本
    python3.5
3. nginx配置

  ```
   # user test conf
   http {
     upstream test.com {
       server 127.0.0.1:8008 weight=1;
     }
     server {
       listen 8000;
       
       location / {
         root html;
         index index.html index.html;
       }
       
       location ~\.(py) {
         root E:\my_project\fullstack-demo;
         proxy_pass http://test.com;
         proxy_redirect default;
       }
     }
   }
  ```
4. cd到nginx的安装目录，执行启动nginx命令： start nginx。
5. cd到server.py文件的目录，执行命令：python server.py，输出信息如下：

> E:\my_project\fullstack-demo>python server.py
> Serving HTTP on port 8000...

6. 浏览器打开http://127.0.0.1:8000（或者cmd下执行curl http://127.0.0.1:8000），应显示welcome to nginx!欢迎页面, 表示nginx代理静态页面工作正常。

> Welcome to nginx!

> If you see this page, the nginx web server is successfully installed and working. Further configuration is required.

> For online documentation and support please refer to nginx.org.
> Commercial support is available at nginx.com.

> Thank you for using nginx.

7. 浏览器打开http://127.0.0.1:8000/test.py（或者cmd下执行curl http://127.0.0.1:8000/test.py），应显示hello, world, 表示代理python server返回成功。
> hello world
