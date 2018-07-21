```
sudo gedit  /etc/apt/sources.list
打开后就可以进行编辑了
原版是：
deb [by-hash=force] http://packages.deepin.com/deepin unstable main contrib non-free
#deb-src http://packages.deepin.com/deepin unstable main contrib non-free
换成中科大的就是：
deb [by-hash=force] http://mirrors.ustc.edu.cn/deepin unstable main contrib non-free
#deb-src http://mirrors.ustc.edu.cn/deepin unstable main contrib non-free
```

