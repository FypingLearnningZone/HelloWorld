# CGI

CGI是通用网关接口，是连接web服务器和应用程序的接口，用户通过CGI来获取动态数据或文件等。 CGI程序是一个独立的程序，它可以用几乎所有语言来写，包括perl，c，lua，python等等。

# WSGI

WSGI, Web Server Gateway Interface，是Python应用程序或框架和Web服务器之间的一种接口，WSGI的其中一个目的就是让用户可以用统一的语言(Python)编写前后端。

# UWSGI

uWSGI 是一个 Web 服务器，它实现了 WSGI 协议、uwsgi协议、http 等协议。
注意 uwsgi 是一种通信协议，它用于定义传输信息的类型，而 uWSGI 是实现 uwsgi 协议和 WSGI 协议的 Web 服务器

# 为什么有了uWSGI为什么还需要nginx？
因为nginx具备优秀的静态内容处理能力，然后将动态内容转发给uWSGI服务器，这样可以达到很好的客户端响应。