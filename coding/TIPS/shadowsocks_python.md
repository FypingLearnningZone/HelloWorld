title: shadowsocks_python
date: 2018/1/1 12:12:12
---
安装
```
sudo pacman -S python-pip
sudo pacman -S shadowsocks
```
创建配置文件
```
mkdir /etc/shadowsocks
vim /etc/shadowsocks/config.json （一定要在这个目录下）
```
单用户
```
{
"server":"",  ##填写服务器外网ip地址，ip也可以写内网地址，只要能转发出来即可。
"server_port":8000,
"local_address":"127.0.0.1",
"local_port":1080,
"password":"",
"timeout":300,
"method":"aes-256-cfb",
"fast_open":false
}
```
多用户
```
{
"server":"",
"local_address":"127.0.0.1",
"local_port":1080,
"port_password":{
"8000":"123456",
"8001":"123456"
},
"timeout":300,
"method":"aes-256-cfb",
"fast_open":false
}
```
启动/关闭 服务
```
ssserver -c /etc/shadowsocks/config.json -d start 后台启动
ssserver -c /etc/shadowsocks/config.json -d stop 后台停止用户
```
设置开机启动
将启动的命令加入到/etc/rc.local文件的最后

```
vi /etc/rc.local
```
设置非root用户运行ss
```
sudo useradd ssuser //添加一个ssuser用户
sudo ssserver [other options] --user ssuser //用ssuser这个用户来运行ss
```



> https://thief.one/2017/02/22/Shadowsocks%E6%8A%98%E8%85%BE%E8%AE%B0/






















