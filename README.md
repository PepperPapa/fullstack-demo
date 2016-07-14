# windows下nginx配置python服务器简单示例
> 该示例实现nginx作为python web server的代理服务器的最基本配置，主要是学习nginx和
python wsgi接口的相关配置

1. 安装python
   步骤略，本例使用版本python3.4
2. 安装flup
   python3可用的flup版本库    
   [flup-py3](https://github.com/PepperPapa/flup-py3.git)
   解压,在解压目录中运行
   python setup.py install

  >成功提示
  Installed f:/python25/lib/site-packages/flup-1.0.2-py2.5.egg
  Processing dependencies for flup==1.0.2
  Finished processing dependencies for flup==1.0.2

3. 创建server.py代码见仓库源码, 执行以下命令（后面参数为可选）  
  python server.py --method=prefork/threaded minspare=50 maxspare=50 maxchildren=1000
4. nginx配置

  ```
   events {
        worker_connections  1024;
    }

    http {
      server {
        listen 8000;   #nginx服务端口
        server_name test.com;
        root E:\my_project\fullstack-demo;

        location / {
          fastcgi_pass 127.0.0.1:8008;  #python server端口
          fastcgi_param SCRIPT_FILENAME "";
          fastcgi_param PATH_INFO $fastcgi_script_name;
          include fastcgi.conf;
        }
      }
    }
    ```
5.启动nginx： start nginx
6.浏览器打开http://127.0.0.1:8000/，或执行curl http://127.0.0.1:8000，返回信息
  Hello World!
