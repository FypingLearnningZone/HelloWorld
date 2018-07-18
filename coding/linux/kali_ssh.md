安装

```
apt-get update
apt-get install openssh-server
```

配置

```
vi /etc/ssh/sshd_config
#将#PasswordAuthentication no 该行前面的#去掉，并且将NO修改为YES
#将#PermitRootLogin  without-password 该行前面的#去掉，并且将“without-password”修改为YES
```

启动服务

```
service ssh restart
```



