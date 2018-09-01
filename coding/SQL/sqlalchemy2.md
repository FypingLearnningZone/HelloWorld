```
from sqlalchemy import create_engine
from pymysql import install_as_MySQLdb
install_as_MySQLdb()

engine = create_engine("mysql://xeanyu:xeanyu@127.0.0.1/test")

con = engine.connect() # 去连接数据库，返回一个连接后的实例
raw = con.execute("select * from User") # 注意，使用Python去操作数据库，写Sql命令时可以不带分号。

for i in raw: # 这里会返回一个raw，raw中每个元素是每行值所组成的的元组(tuple)
    print(i)
```



第2~4行**：其中create_engine 是用于连接数据库的，它会返回一个实例，但是这个时候并未连接。而第二行中的install_as_MySQLdb是一个处理包的函数，原本Mysqldb是不支持Python3的，后来有了Pymysql，但是还有很多模块需要Mysqldb，所以就在这里进行了包上的处理，第三行所执行的函数，就是可以让那些需要Mysqldb的模块可以获取到Mysqldb包。**

 

第6行: **这里需要重点讲下，这里的create_engine 连接数据库的格式是**

> dialect+driver://username:password@host:port/database_name

其中 `dialect` 指的是数据库程序，比如我用mysql，或者其他数据库名称，比如sqllite，postgersql等等。

其中`driver` 是数据库程序的驱动，如果不指定，Sqlalchemy默认会是**Mysqldb，这也是我为什么要用 install_as_MySQLdb 的原因。**

其中`username` 是数据库用户名，比如我们创建的 xeanyu 这个用户，xeanyu就是用户名

其中 `password` 是用户密码

其中`host` 和 `port` 是数据库地址和端口，其中`port`不指定则默认根据`dialect` 去默认。

其中`database_name` 是数据库名称

所以我们根据以上格式，我们去连接数据库。

 

第8行: **我们根据create_engine给我们返回给我们的实例去连接数据库，进行connect()**

 

第9行: **我们又根据connect() 返回给我们的连接实例，去进行数据库的操作, select \* from User 其中不必带上分号，它会返回一个迭代器，我们把这个迭代器赋值给raw**

 

第11~12行: **我们输出我们查询的东西。**



###### Reference

- https://cuiqingcai.com/6158.html