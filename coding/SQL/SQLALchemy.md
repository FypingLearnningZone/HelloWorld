- 安装

  ```bash
  pip install sqlalchemy
  ```

- 配置

  ```python
  from sqlalchemy import *
  from sqlalchemy.ext.declarative import declarative_base
  from sqlalchemy.orm import relation, sessionmaker
  Base = declarative_base()
  
  
  class Movie(Base):
      __tablename__ = 'movies'
   
      id = Column(Integer, primary_key=True)
      title = Column(String(255), nullable=False)
      year = Column(Integer)
      directed_by = Column(Integer, ForeignKey('directors.id'))
   
      director = relation("Director", backref='movies', lazy=False)
   
      def __init__(self, title=None, year=None):
          self.title = title
          self.year = year
      def __repr__(self):
          return "Movie(%r, %r, %r)" % (self.title, self.year, self.director)
   
  class Director(Base):
      __tablename__ = 'directors'
   
      id = Column(Integer, primary_key=True)
      name = Column(String(50), nullable=False, unique=True)
   
      def __init__(self, name=None):
          self.name = name
   
      def __repr__(self):
          return "Director(%r)" % (self.name)
          
  ```

  

- 连接

  ```python
  engine = create_engine('mysql+pymysql://root:rango.lzp@127.0.0.1:3306/test?charset=utf8', echo=True)
  Base.metadata.create_all(engine)
  ```

  ```python
  不同数据库的连接
  
  MySQL-Python
  mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
  
  pymysql
  mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
  
  MySQL-Connector
  mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
  ```

  

- 增删改查

     ```
     
     ```



参考

- https://blog.ansheng.me/article/python-full-stack-way-sqlalchemy

