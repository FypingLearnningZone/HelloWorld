```
SHOW DATABASES︰列出 MySQL Server 上的資料庫。

SHOW TABLES [FROM db_name]︰列出資料庫的資料表。

SHOW TABLE STATUS [FROM db_name]︰列出資料庫的資料表，提供比較詳細的訊息。

SHOW COLUMNS FROM tbl_name [FROM db_name]︰列出資料表的欄位，同 SHOW FIELDS FROM tbl_name [FROM db_name]，DESCRIBE tbl_name [col_name]。

SHOW FULL COLUMNS FROM tbl_name [FROM db_name]︰列出資料表的欄位，提供比較詳細的訊息，同 SHOW FULL FIELDS FROM tbl_name [FROM db_name]。

SHOW INDEX FROM tbl_name [FROM db_name]︰列出資料表的索引訊息。

SHOW STATUS︰列出 Server 的狀態訊息。

SHOW VARIABLES︰列出 MySQL 系統變數的值。

SHOW PROCESSLIST︰顯示哪個執行緒正在運行。

SHOW GRANTS FOR user︰列出對一個用戶必須發出以重複授權的授權命令。

```

```
SELECT - 从数据库中提取数据
UPDATE - 更新数据库中的数据
DELETE - 从数据库中删除数据
INSERT INTO - 向数据库中插入新数据
CREATE DATABASE - 创建新数据库
ALTER DATABASE - 修改数据库
CREATE TABLE - 创建新表
ALTER TABLE - 变更（改变）数据库表
DROP TABLE - 删除表
CREATE INDEX - 创建索引（搜索键）
DROP INDEX - 删除索引
```
#### SELECT

```
SELECT column_name,column_name
FROM table_name;
```

#### SQL SELECT DISTINCT

```
SELECT DISTINCT column_name,column_name
FROM table_name;
```

#### Where 子句

搜索 empno 等于 7900 的数据：

```
Select * from emp where empno=7900;
```

##### Where +条件（筛选行）

条件：列，比较运算符，值

比较运算符包涵：= > < >= ,<=, !=,<> 表示（不等于）

```
Select * from emp where ename='SMITH';
```

例子中的 SMITH 用单引号引起来，表示是字符串，字符串要区分大小写。

##### 逻辑运算

And:与 同时满足两个条件的值。

```
Select * from emp where sal > 2000 and sal < 3000;
```

查询 EMP 表中 SAL 列中大于 2000 小于 3000 的值。

Or:或 满足其中一个条件的值

```
Select * from emp where sal > 2000 or comm > 500;
```

查询 emp 表中 SAL 大于 2000 或 COMM 大于500的值。

Not:非 满足不包含该条件的值。

```
select * from emp where not sal > 1500;
```

查询EMP表中 sal 小于等于 1500 的值。

逻辑运算的优先级：

```
()    not        and         or
```

##### 特殊条件

**1.空值判断： is null**

```
Select * from emp where comm is null;
```

查询 emp 表中 comm 列中的空值。

**2.between and (在 之间的值)**

```
Select * from emp where sal between 1500 and 3000;
```

查询 emp 表中 SAL 列中大于 1500 的小于 3000 的值。

注意：大于等于 1500 且小于等于 3000， 1500 为下限，3000 为上限，下限在前，上限在后，查询的范围包涵有上下限的值。

**3.In**

```
Select * from emp where sal in (5000,3000,1500);
```

查询 EMP 表 SAL 列中等于 5000，3000，1500 的值。

**4.like**

Like模糊查询

```
Select * from emp where ename like 'M%';
```

查询 EMP 表中 Ename 列中有 M 的值，M 为要查询内容中的模糊信息。

-  **%** 表示多个字值，**_** 下划线表示一个字符；
-  **M%** : 为能配符，正则表达式，表示的意思为模糊查询信息为 M 开头的。
-  **%M%** : 表示查询包含M的所有内容。
-  **%M_** : 表示查询以M在倒数第二位的所有内容。



****

**第一、只复制表结构到新表**

create table 新表 select * from 旧表 where 1=2

或者

create table 新表 like 旧表 

**第二、复制表结构及数据到新表**

create table新表 select * from 旧表 





## 获取服务器元数据

以下命令语句可以在 MySQL 的命令提示符使用，也可以在脚本中 使用，如PHP脚本。

| 命令               | 描述                      |
| ------------------ | ------------------------- |
| SELECT VERSION( )  | 服务器版本信息            |
| SELECT DATABASE( ) | 当前数据库名 (或者返回空) |
| SELECT USER( )     | 当前用户名                |
| SHOW STATUS        | 服务器状态                |
| SHOW VARIABLES     | 服务器配置变量            |