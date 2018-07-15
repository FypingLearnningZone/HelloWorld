```bash
#查看依赖
dpkg --list|grep mysql
sudo apt-get remove --purge mysql-\*
sudo find  / -name mysql -print
#再用dpkg --list|grep mysql查看，还剩什么就卸载什么
dpkg --list|grep mysql
whereis mysql

#清除残留
dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P
```

```bash
#安装
sudo apt-get install mysql-server mysql-client
#运行数据库Mysql安全配置向导：
sudo mysql_secure_installation
```



- [](https://blog.csdn.net/w3045872817/article/details/77334886)
- [](https://blog.csdn.net/chudongfang2015/article/details/52154903)