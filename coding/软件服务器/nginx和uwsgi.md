### nginx 的作用

反向代理和负载均衡

### wsgi是什么？

在生产环境中使用WSGI作为python web的服务器。
 WSGI：全拼为Python Web Server Gateway Interface，Python Web服务器网关接口，是Python应用程序或框架和Web服务器之间的一种接口，被广泛接受。WSGI没有官方的实现, 因为WSGI更像一个协议，只要遵照这些协议，WSGI应用(Application)都可以在任何服务器(Server)上运行。

#### uwsgi

Uwsgi 实现了wsgi的全部接口，它由c编写，高效稳定



## 1，布署

当项目开发完成后，需要将项目代码放到服务器上，这个服务器拥有固定的IP，再通过域名绑定，就可以供其它人浏览，对于python web开发，可以使用wsgi、apache服务器。

服务器首先是物理上的一台性能高、线路全、运行稳定的机器，分为私有服务器、公有服务器。

私有服务器：公司自己购买、自己维护，只布署自己的应用，可供公司内部或外网访问，成本高，需要专业人员维护，适合大公司使用。

公有服务器：集成好运营环境，销售空间或主机，供其布署自己的应用，适合初创公司使用，成本低。

常用的公有服务器，如阿里云、青云等，可按流量收费或按时间收费。服务器还需要安装服务器软件，此处需要uWSGI、Nginx。

## 2，搭建服务器虚拟环境

```
1）在本机进入虚拟环境，执行命令导出当前需要的所有包。

pip freeze > plist.txt

2）通过ftp软件将项目代码和plist.txt文件上传到服务器。

3）创建虚拟环境，在虚拟环境上安装包。
mkvirtualenv 虚拟环境名称
pip install -r plist.txt
```

## 3，WSGI

在生产环境中使用WSGI作为python web的服务器。
 WSGI：全拼为Python Web Server Gateway Interface，Python Web服务器网关接口，是Python应用程序或框架和Web服务器之间的一种接口，被广泛接受。WSGI没有官方的实现, 因为WSGI更像一个协议，只要遵照这些协议，WSGI应用(Application)都可以在任何服务器(Server)上运行。

项目默认会生成一个wsgi.py文件，确定了settings模块、application对象。

application对象：在Python模块中使用application对象与应用服务器交互。
 settings模块：用于进行项目配置。

## 4，uWSGI

uWSGI实现了WSGI的所有接口，是一个快速、自我修复、开发人员和系统管理员友好的服务器。uWSGI代码完全用C编写，效率高、性能稳定。

```
1）安装uWSGI。
pip install uwsgi

2）配置uWSGI，在项目目录下创建uwsgi.ini文件，配置如下：
# 这句代码必须加上
[uwsgi]
#使用nginx连接时使用
#socket=127.0.0.1:8080
#直接做web服务器使用
http=127.0.0.1:8080
#项目目录
chdir=/home/xxoo
#项目中wsgi.py文件的目录，相对于项目目录
wsgi-file=xxoo/wsgi.py
processes=4
threads=2
master=True
pidfile=uwsgi.pid
daemonize=uswgi.log

3）启动。
uwsgi --ini uwsgi.ini

4）查看。
ps ajx|grep uwsgi

5）停止。
uwsgi --stop uwsgi.pid
```

## 5,Nginx

使用nginx的作用主要包括负载均衡、反向代理。

使用方法如下：

```
1）下载nginx后放到桌面上，解压缩。
tar zxvf nginx-1.6.3.tar.gz

2）进入nginx-1.6.3目录，依次执行以下命令进行安装。
./configure
make
sudo make install

3）默认安装到/usr/local/nginx/目录，进入此目录。
cd /usr/local/nginx/

4）启动。
sudo sbin/nginx

5）查看进程。
ps ajx|grep nginx

6）停止。
sudo sbin/nginx -s stop
```

#### 指向uwsgi项目

1）打开conf/nginx.conf文件。
 sudo gedit conf/nginx.conf

2）在server节点下添加新的location项，指向uwsgi的ip与端口。

```
    location / {
        #将所有的参数转到uwsgi下
        include uwsgi_params;
        #uwsgi的ip与端口
        uwsgi_pass 127.0.0.1:8080;
    }
```

代码效果如下图：



![img](https:////upload-images.jianshu.io/upload_images/3827414-b30b2aff32763902?imageMogr2/auto-orient/strip%7CimageView2/2/w/472/format/webp)

这里写图片描述

## 6，小知识点：异步调度器Celery

情景：用户发起request，并等待response返回。在一些views中，可能需要执行一段耗时的程序，那么用户就会等待很长时间，造成不好的用户体验，比如发送邮件、手机验证码等。

使用celery后，情况就不一样了。解决：将耗时的程序放到celery中执行。

### celery名词：

任务task：就是一个Python函数。
 队列queue：将需要执行的任务加入到队列中。
 工人worker：在一个新进程中，负责执行队列中的任务。
 代理人broker：负责调度，在布置环境中使用redis。

看下图理解：



![img](https:////upload-images.jianshu.io/upload_images/3827414-c534bf6ca7bde05c?imageMogr2/auto-orient/strip%7CimageView2/2/w/789/format/webp)

作者：晓可加油

链接：https://www.jianshu.com/p/bf6c3cc16326

來源：简书

简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。