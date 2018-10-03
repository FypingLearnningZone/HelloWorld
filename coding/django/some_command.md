#####  some command

```
django-admin startproject mysite
```



- 建立应用

```bash
python manage.py startapp blog
```

- 迁移数据库

  ```
  python manage.py makemigrations
  ```

  Django 在 应用的 migrations\ 目录下生成了一个 0001_initial.py 文件，这个文件是 Django 用来记录我们对模型做了哪些修改的文件

  ```
  python manage.py migrate
  ```

  Django 通过检测应用中 migrations\ 目录下的文件，得知我们对数据库做了哪些操作，然后它把这些操作翻译成数据库操作语言，从而把这些操作作用于真正的数据库。

  ```
  python manage.py sqlmigrate blog 0001
  ```

  输出Django 翻译后执行的数据库语句



#### 1 新建项目 project

```
django-admin.py startproject project-name
```

特别是在 windows 上，如果报错，尝试用 django-admin 代替 [django-admin.py](http://django-admin.py/)

#### 2 新建 app

```
python manage.py startapp app-name
#或 
django-admin.py startapp app-name
```

一般一个项目有多个app, 当然通用的app也可以在多个项目中使用。

#### 3 同步数据库

```
python manage.py syncdb
 
# 注意：Django 1.7.1及以上的版本需要用以下命令
python manage.py makemigrations
python manage.py migrate
```

这种方法可以创建表，当你在models.py中新增了类时，运行它就可以自动在数据库中创建表了，不用手动创建。

`备注`：对已有的 models 进行修改，Django 1.7之前的版本的Django都是无法自动更改表结构的，不过有第三方工具 south,详见 Django 数据库迁移 一节。

#### 4 清空数据库

```
python manage.py flush
```

此命令会询问是 yes 还是 no, 选择 yes 会把数据全部清空掉，只留下`空表`。

#### 5 数据库命令行

```
python manage.py dbshell
```

Django 会自动进入在settings.py中设置的数据库，如果是 MySQL 或 postgreSQL,会要求输入数据库用户密码。

在这个终端可以执行数据库的SQL语句。如果您对SQL比较熟悉，可能喜欢这种方式。

#### 6 使用开发服务器

开发服务器，即开发时使用，一般修改代码后会自动重启，方便调试和开发，但是由于性能问题，建议只用来测试，不要用在生产环境。

```
# 默认监听 http://127.0.0.1:8000/端口
python manage.py runserver

# 监听 http://127.0.0.1:8000/端口
python manage.py runserver 8001

# 监听所有可用 ip （电脑可能有一个或多个内网ip，一个或多个外网ip，即有多个ip地址）
python manage.py runserver 0.0.0.0:8000
```

#### 7 创建超级管理员

```
# 按照提示输入用户名和对应的密码就好了邮箱可以留空，用户名和密码必填
python manage.py createsuperuser
 
# 修改 用户密码可以用：
python manage.py changepassword username
```

#### 8 导出数据 导入数据

```
python manage.py dumpdata appname > appname.json
python manage.py loaddata appname.json
```

关于数据操作 详见：数据导入数据迁移，现在了解有这个用法就可以了。

#### 9 Django 项目环境终端

```
python manage.py shell
```

如果你安装了 bpython 或 ipython 会自动用它们的界面，推荐安装 `bpython`。

这个命令和 直接运行 python 或 bpython 进入 shell 的区别是：你可以在这个 shell 里面调用当前项目的 [models.py](http://models.py/) 中的 API，对于操作数据，还有一些小测试非常方便。

#### 10 更多命令

终端上输入 python [manage.py](http://manage.py/) 可以看到详细的列表，在忘记子名称的时候特别有用。
更详细的介绍，点击对应版本去官网查看：[1.7][1] [1.10][2] [dev][3]

[1]: https://docs.djangoproject.com/en/1.7/ref/django-admin/
[2]: https://docs.djangoproject.com/en/1.10/ref/django-admin/
[3]: https://docs.djangoproject.com/en/dev/ref/django-admin/