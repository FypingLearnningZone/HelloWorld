title: python_virtualenv
date: 2018/1/1 12:12:12
---
##### 首先，我们用pip安装virtualenv：

```
$ pip3 install 
```

我们用pip安装virtualenv

###### 然后，假定我们要开发一个新的项目，需要一套独立的Python运行环境，可以这么做：

第一步，创建目录：


```
Mac:~ michael$ mkdir myproject
Mac:~ michael$ cd myproject/
Mac:myproject michael$
```

第二步，创建一个独立的Python运行环境，命名为venv：


```
Mac:myproject michael$ virtualenv --no-site-packages venv
Using base prefix '/usr/local/.../Python.framework/Versions/3.4'
New python executable in venv/bin/python3.4
Also creating executable in venv/bin/python
Installing setuptools, pip, wheel...done.
```
启动虚拟环境
```
Mac:myproject michael$ source venv/bin/activate
(venv)Mac:myproject michael$
```
退出虚拟环境

```
(venv)Mac:myproject michael$ deactivate 
Mac:myproject michael$
```
#### 小结

virtualenv为应用提供了隔离的Python运行环境，解决了不同应用间多版本的冲突问题。