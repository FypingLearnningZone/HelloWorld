manjaro

```
chromium fcitx-im fcitx-configtool fcitx-googlepinyin shadowsocks-qt5 firefox npm evince cool-retro-term eclipse-cpp code mysql
```



deepin 

```
sudo vim /etc/apt/sources.list  deb [by-hash=force] http://mirrors.ustc.edu.cn/deepin panda main contrib non-free

sudo apt update
sudo apt-get upgrade

sudo apt install deepin-fpapp-org.deepin.flatdeb.shadowsocks-qt5 fcitx-googlepinyin git code remmina

sudo apt-get install mysql-server 
sudo mysql_secure_installation

sudo apt-get install libmysqlclient-dev python-dev

sudo apt install python3-pip
python3 -m pip install --upgrade pip
python3 -m pip install jupyter

配置mysql
ERROR 1698 (28000): Access denied for user 'root'@'localhost'
select user, plugin from mysql.user;
update mysql.user set authentication_string=PASSWORD('newPwd'), plugin='mysql_native_password' where user='root';
sudo service mysql restart

配置git 全局代理
全局代理，写入配置
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'
清除配置
git config --global --unset http.proxy

配置pip tuna
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
临时使用
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

sudo apt-get install -y nodejs npm
npm install -g cnpm --registry=https://registry.npm.taobao.org

git clone https://github.com/junkrango/junkrango.github.io.git

add /etc/hosts 0.0.0.0 account.jetbrains.com
https://github.com/junkrango/junkrango.github.io/blob/master/coding/TIPS/pycharm_%E6%B3%A8%E5%86%8C.md

typora pycharm tor 源码
```



