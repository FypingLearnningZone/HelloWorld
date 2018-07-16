针对很多朋友反映按照教程的做法始终只能看到 Nginx 欢迎页面的问题，Tian Pengfei sanyuwen 给出了很好的建议。如果你也被类似问题困扰，不妨尝试一下这个建议。

> 这个问题也困扰了很久，最终发现是sites-enabled文件夹里默认的default文件中的配置覆盖了自己写的配置，导致配置不生效，把default文件删掉就可以正常被nginx代理过去了，亲测有效



```bash
pip install uwsgi
#测试你的Django项目
python manage.py runserver 0.0.0.0:8000
#而如果正常，则使用uWSGI来运行它:
#module mysite.wsgi: 加载指定的wsgi模块
uwsgi --http :8000 --module mysite.wsgi

```

```bash
#nginx 站点配置
# configuration of the server
server {
    # the port your site will be served on
    listen      80;
    # the domain name it will serve for
    server_name video.scavenger.top; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /var/www/video_site/media;  # your Django project's media files - amend as required
    }

    location /static {
        alias /var/www/video_site/static; # your Django project's static files - amend as required
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  unix:///var/www/video_site/video.sock;
        include     /etc/nginx/uwsgi_params; # the uwsgi_params file you installed
    }
}

```

```bash
#uwsgi配置文件 
[uwsgi]

# Django-related settings
# the base directory (full path)
chdir           = /var/www/django_video
# Django's wsgi file
module          = video.wsgi
# the virtualenv (full path)
home            = /var/www/django_video/venv

# process-related settings
# master
master          = true
# maximum number of worker processes
processes       = 10
# the socket (use the full path to be safe
socket          = /var/www/django_video/video.sock
# ... with appropriate permissions - may be needed
# chmod-socket    = 664
# clear environment on exit
vacuum          = true

```

```bash
#用uwsgi启动整个站点
uwsgi --ini mysite_uwsgi.ini
```



