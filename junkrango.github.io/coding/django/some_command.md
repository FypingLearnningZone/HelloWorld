title: some_command
date: 2018/1/1 12:12:12
---
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

<<<<<<< HEAD
创建超级用户

```
=======
```
#创建超级用户
>>>>>>> 6613047094c3d4c168b3f7a7bced236130d204bd
python manage.py createsuperuser
```

