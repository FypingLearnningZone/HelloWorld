lnmp1.4 php安装模块

```bash
#下载源码
wget php-5.6.25.tar.gz
#解压
tar -zxvf php-5.6.25.tar.gz
#进入扩展目录
cd php-5.6.25/ext/fileinfo
#安装
/usr/local/php/bin/phpize
./configure -with-php-config=/usr/local/php/bin/php-config
./configure -with-php-config=/etc/php/7.0/fpm/php-config
make && make install
#配置
cd /usr/local/php/etc/
vi php.ini 
#添加 extension = "fileinfo.so" 
重启环境
lnmp restart
```

ubuntu14.04下没有phpize的解决方法

apt-get install php5.6-dev

ubuntu14.04下没有php5.6-fpm的解决方法

apt-get install php5.6-fpm 

```
sudo apt-get install php7.0-xxx
#xxx为模块名称如 sudo apt-get install php7.0-mbstring
```



