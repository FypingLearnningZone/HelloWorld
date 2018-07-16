title: virtualbox中linux与宿主windwos共享文件夹设置
date: 2018/1/1 12:12:12
---
进入虚拟Ubuntu，在命令行终端下输入：
```
创建挂载文件夹
sudo mkdir /mnt/shared
```

挂载

```
sudo mount -t vboxsf share /mnt/shared
```

其中"share"是之前创建的共享文件夹的名字

要想自动挂载的话，可以在/etc/fstab中添加一项
```
share /mnt/shared vboxsf rw,gid=100,uid=1000,auto 0 0
```
卸载的话使用下面的命令：
```
sudo umount -f /mnt/shared
```