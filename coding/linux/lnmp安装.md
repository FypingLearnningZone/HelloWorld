环境

Ubuntu 16.04 x64

```bash
#安装nginx
apt-get update
apt-get install nginx

#安装Mysql
apt-get install php7.0
#Nginx生效的站点配置文件在/etc/nginx/sites-enabled/目录下
#安装php-fpm
apt-get install php7-fpm
#nginx配置php-fpm支持php 去除前面的注释
location ~ \.php$ {
	include snippets/fastcgi-php.conf;
#
#	# With php7.0-cgi alone:
#	fastcgi_pass 127.0.0.1:9000;
#	# With php7.0-fpm:
		fastcgi_pass unix:/run/php/php7.0-fpm.sock;
#       fastcgi_index index.php;
#       include fastcgi_params;
	}
#重启ngnix
systemctl restart nginx
#测试nginx支持php
#编辑/var/www/html/info.php  添加
<?php
    phpinfo();
?>
访问
http://server_domain_or_IP/info.php
```

