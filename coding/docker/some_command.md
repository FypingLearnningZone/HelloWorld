列出本地主机上的镜像
```
docker images
```
运行镜像
```
docker run
```

- -t 在新容器内指定一个伪终端或终端。 
- -i 允许你对容器内的标准输入 (STDIN) 进行交互
- -d 以进程方式运行的容器  后台运行
- **-P: **是容器内部端口随机映射到主机的高端口  
- **-p 80:80：**将容器的80端口映射到主机的80端口
- **--name mynginx：**将容器命名为mynginx
- **-v $PWD/www:/www：**将主机中当前目录下的www挂载到容器的/www
- **-v $PWD/conf/nginx.conf:/etc/nginx/nginx.conf：**将主机中当前目录下的nginx.conf挂载到容器的/etc/nginx/nginx.conf
- **-v $PWD/logs:/wwwlogs：**将主机中当前目录下的logs挂载到容器的/wwwlogs

显示正在运行的镜像

```
docker ps
```

显示容器内的标准输出

```
docker logs CONTAINER ID:容器ID/NAMES:自动分配的容器名称
```

停止容器

```
docker stop CONTAINER ID:容器ID/NAMES:自动分配的容器名称
```



获取镜像

```

```

查找镜像

```
docker search image_name
```

获取指定容器底层信息

```
docker inspect CONTAINER ID:容器ID/NAMES:自动分配的容器名称
```

移除指定容器

```
docker rm CONTAINER ID:容器ID/NAMES:自动分配的容器名称
```

##### 容器命名

当我们创建一个容器的时候，docker会自动对它进行命名。另外，我们也可以使用--name标识来命名容器，例如：

```
runoob@runoob:~$  docker run -d -P --name runoob training/webapp python app.py
43780a6eabaaf14e590b6e849235c75f3012995403f97749775e38436db9a441
```