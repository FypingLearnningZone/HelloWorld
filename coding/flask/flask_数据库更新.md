Flask数据库用到两个库：Flask-SQLAlchemy和Flask-Migrate
使用Flask-SQLAlchemy管理数据库
使用Flask-Migrate实现数据库迁移
安装：
```
pip install Flask-SQLAlchemy
pip install Flask-Migrate
```
创建数据库
进入python shell
```
python manage.py shell 
```
导入db
```
from app import db
```
导入model中User Role模型（这个很重要，要不创建出数据库后会没有表）
```
from app.models import Role,User
```
创建数据库
```
db.create_all()
```
执行完成之后，会生成一个data.sqlite文件，文件中会生成相应的表,如果上步没有引入Role,User，这里创建出来文件里会没有对应的表

数据库迁移
第一次使用
初始化:
```
python manage.py db init 
```
这个命令会在项目下创建 migrations 文件夹，所有迁移脚本都存放其中。
创建第一个版本：
```
python manage.py db migrate -m "initial migration" 
```
检查migrations\versions，会新建一个版本.py，检查里面表格及字段，此时数据库中会自动创建一个alembic_version表格，用于记录数据库版本信息
运行升级
```
python manage.py db upgrade
```
会把项目使用的数据库文件，更新为新的表格、字段，同时保留数据
数据库更新
更新表格的字段 (models.py)
再次运行一下
```
python manage.py db migrate -m "commit"
```
相当于commit 更新到/migrate目录
数据库更新
```
python manage.py db upgrade  
```
数据库会更新
数据库字段回滚
获取 History ID
```

python manage.py db history
```
回滚到某个 history
```
python manage.py db downgrade <history_id>
```
注意
数据库迁移的时候，如果manage.py里没有导入Role和User，模型对应表结构，迁移脚本拿不到模型，就会删除数据库里对应的表。这地方掉坑里好久。
在创建数据库的时候也需要导入模型Role和User
为了避免一直重复导入，我们可以做些配置，让 Flask-Script 的 shell 命令自动导入特定的对象。
所以我们干脆在manage.py文件里统一代码处理，减少出错的可能性:

导入相应文件:Shell(和python shell相关)，User, Role数据模型
```
from flask_script import Shell
from app.models import User, Role
```
此时数据库升级的时候就能拿到模型知道表结构了，可以正常升级了。还可以进一步处理在创建数据库的时候也不需要手动导入：
```
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command('shell', Shell(make_context=make_shell_context))
```
这样做了之后创建数据库时不需要这一步：
```
from app.models import Role,User
```
导入模型。
其余不变，不会再导致表丢失的问题



参考：
http://blog.csdn.net/kevin_qq/article/details/51777190


链接：https://www.jianshu.com/p/014fcac4ecf4
