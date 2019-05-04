arch

```
https://wiki.archlinux.org/index.php/Installation_guide_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)

执行useradd -m yourusername创建新用户，并执行passwd yourusername设置登陆密码。
执行vim /etc/sudoers编辑sudo权限，复制一行root ALL=(ALL) ALL, 并替换其中的root为新用户名，保存并退出。


alsa-utils xf86-video-vesa intel xorg xorg-xinit 

fcitx-im fcitx-configtool fcitx-googlepinyin shadowsocks-qt5 npm mysql python python-pip konsole

i3 git openssh htop screenfetch tree wget reminna chromium firefox  evince code python 

typora pycharm tor

中英文字体
声音驱动
调整声音
截图

生成源文件
sudo pacman-mirrors -i -c China -m rank

```

xubuntu

```
konsole gedit code reminna chromium firefox  evince code pcmanfm shadowsocks-qt5  fcitx-im fcitx-configtool fcitx-googlepinyin npm mysql python python-pip
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

```
经过一天的时间折腾 终于把arch + i3装好了
遇到了很多很多的坑
但是仅仅是装好了系统

要配置的符合我的要求 那工作量不敢想象
不是我懒 而是linux的生态与起初设计原理

每次装系统都要一番折腾 一不小心弄坏了系统 只能重头再来了

包管理 让人既爱又恨  多么想要一个单文件

所有的系统组件都是拼凑起来的 各种各样的兼容性问题

系统不是一个人独自一人折腾的 而是一个生态 需要权力与资源的包裹
要引导一群人去自愿去维护一个系统
```

```
修改 mac address

sudo ifconfig wlp2s0 down
sudo ifconfig wlp2s0 hw ether a6:b7:00:a6:a7:a8
sudo ifconfig wlp2s0 up

ifconfig：找不到命令
pacman -S net-tools dnsutils inetutils iproute2

chrome 命令行启动 代理
chrome --proxy-server="socks5://127.0.0.1:1080"
```

