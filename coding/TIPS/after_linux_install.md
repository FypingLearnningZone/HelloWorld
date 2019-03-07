```
生成源文件
sudo pacman-mirrors -i -c China -m rank

ifconfig：找不到命令
pacman -S net-tools dnsutils inetutils iproute2

修改 mac address

sudo ifconfig wlp2s0 down
sudo ifconfig wlp2s0 hw ether a6:b7:00:a6:a7:a8
sudo ifconfig wlp2s0 up

中文输入法
   fcitx-im
   fcitx-configtool
   fcitx-googlepinyin
   如果你使用的是较新版本的GNOME，使用 Wayland 显示管理器，则请在/etc/environment中加入：
   export GTK_IM_MODULE=fcitx
   export QT_IM_MODULE=fcitx
   export XMODIFIERS=@im=fcitx

解决pyenv依赖
https://github.com/pyenv/pyenv/wiki/Common-build-problems

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev

```

```
google-chrome
chromium
firefox
filezilla
virtual box
https://www.jetbrains.com/pycharm/download/#section=linux
https://www.virtualbox.org/wiki/Linux_Downloads
https://typora.io/#linux
shadowsokcs-qt5
sudo apt install fcitx-googlepinyin
mysql
redis
```

```
全局代理，写入配置
git config --global http.proxy 'socks5://127.0.0.1:1086'
git config --global https.proxy 'socks5://127.0.0.1:1086'
清除配置
git config --global --unset http.proxy
git config --global --unset https.proxy
临时代理
ALL_PROXY=socks5://127.0.0.1:8888 git clone https://github.com/some/one.git
```

