arch

```
https://wiki.archlinux.org/index.php/Installation_guide_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)

执行useradd -m yourusername创建新用户，并执行passwd yourusername设置登陆密码。
执行vim /etc/sudoers编辑sudo权限，复制一行root ALL=(ALL) ALL, 并替换其中的root为新用户名，保存并退出。


alsa-utils xf86-video-vesa xorg xorg-xinit 

fcitx-im fcitx-configtool fcitx-googlepinyin shadowsocks-qt5 npm mysql python python-pip konsole

i3 git openssh htop screenfetch tree wget reminna chromium firefox  evince code python 

typora pycharm tor
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



