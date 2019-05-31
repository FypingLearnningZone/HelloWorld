####  ERROR 1698 (28000): Access denied for user 'root'@'localhost'

```
mysql> select user, plugin from mysql.user;
+-----------+-----------------------+
| user      | plugin                |
+-----------+-----------------------+
| root      | auth_socket           |
| mysql.sys | mysql_native_password |
| dev       | mysql_native_password |
+-----------+-----------------------+
 root的plugin被修改成了auth_socket，用密码登陆的plugin应该是mysql_native_password
```

```
#更改字段
mysql> update mysql.user set authentication_string=PASSWORD('newPwd'), plugin='mysql_native_password' where user='root';
#重启服务
sudo service mysql stop
sudo service mysql start
```

