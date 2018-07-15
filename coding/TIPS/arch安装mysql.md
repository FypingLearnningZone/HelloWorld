title: arch安装mysql
date: 2018/1/1 12:12:12
---
Archlinux 选择的 MySQL 实现被称为 MariaDB
```
sudo pacman -S mariadb
# 安装软件包后 必须运行下面的命令
mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
systemctl start mariadb
mysql_secure_installation
systemctl restart mariadb
```

> https://wiki.archlinux.org/index.php/MySQL_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)

