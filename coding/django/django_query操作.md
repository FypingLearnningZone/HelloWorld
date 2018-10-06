### 字段查询
- all():返回模型类对应表格中的所有数据。
 例：查询图书所有信息。
 BookInfo.objects.all();->select * from booktest_bookinfo;

- get():返回表格中满足条件的一条数据。
 如果查到多条数据，则抛异常：MultipleObjectsReturned
 查询不到数据，则抛异常：DoesNotExist
 例：查询图书id为3的图书信息。
 BookInfo.objects.get(id=3) –> select * from booktest_bookinfo where id = 3;

- filter():参数写查询条件，返回满足条件QuerySet集合数据。
 条件格式：
 **模型类属性名**__条件名=值
 注意：此处是模型类属性名，不是表中的字段名

##### 关于filter具体案例如下：
 - 1.判等 exact。
 例：查询编号为1的图书。
 BookInfo.object.filter(id=1)
 BookInfo.object.filter(id__exact=1)此处的 __exact可以省略

- 2.模糊查询 like
 例：查询书名包含'传'的图书。contains
 contains BookInfo.objects.filter(btitle__contains=’传’)
 例：查询书名以'部'结尾的图书 endswith 开头:startswith BookInfo.objects.filter(btitle__endswith=’部’)
 BookInfo.objects.filter(btitle__startswith=’天’)

- 3.空查询 where 字段名 isnull
 例：查询书名不为空的图书。isnull
 BookInfo.objects.filter(btitle__isnull=False)

- 4.范围查询 where id in (1,3,5)
 例：查询编号为1或3或5的图书。In
 BookInfo.objects.filter(id__in=[1,3,5])

- 5.比较查询 gt lt(less than) gte(equal) lte
 例：查询编号大于等于3的图书。
 BookInfo.objects.filter(id__gte=3)

- 6.日期查询
 例：查询1980年发表的图书。
 BookInfo.objects.filter(bpub_date__year = 1980)
 例：查询1980年1月1日后发表的图。
 BookInfo.objects.filter(bpub_date__gt = date(1980,1,1))

- 7.exclude:返回不满足条件的数据。
 例：查询id不为3的图书信息。
 BookInfo.objects.exclude(id=3)

- F对象
 作用：用于类属性之间的比较条件。

使用之前需要先导入：
 from django.db.models import F
 例：查询图书阅读量大于评论量图书信息。where bread > bcomment BookInfo.objects.filter(bread__gt = F(‘bcomment’))
 例：查询图书阅读量大于2倍评论量图书信息。 BookInfo.objects.filter(bread__gt=F(‘bcomment’)*2)

- Q对象
 作用：用于查询时的逻辑条件。可以对Q对象进行&|~操作。

使用之前需要先导入：
 from django.db.models import Q
 例：查询id大于3且阅读大于30的图书的信息。
 BookInfo.objects.filter(id__gt=3, bread__gt=30)
 BooInfo.objects.filter(Q(id__gt=3) & Q(bread__gt=3))
 例：查询id大于3或者阅读大于30的图书的信息。
 BookInfo.objects.filter(Q(id__gt=3) | Q(bread__gt=30))
 例：查询id不等于3图书的信息。
 BookInfo.objects.filter(~Q(id=3))

- order_by 返回QuerySet
 作用：对查询结果进行排序。

例：查询所有图书的信息，按照id从小到大进行排序。
 BookInfo.objects.all().order_by('id')
 例：查询所有图书的信息，按照id从大到小进行排序。
 BookInfo.objects.all().order_by('-id')
 例：把id大于3的图书信息按阅读量从大到小排序显示；
 BookInfo.objects.filter(id__gt=3).order_by('-bread')

- 聚合函数
 作用：对查询结果进行聚合操作。

sum count max min avg
 aggregate：调用这个函数来使用聚合。
 使用前需先导入聚合类：
 from django.db.models import Sum,Count,Max,Min,Avg
 例：查询所有图书的数目。select count(*) from booktest_bookinfo; BookInfo.objects.aggregate(Count('id'))
 {'id__count': 5} 注意返回值类型及键名

例：查询所有图书阅读量的总和。
 BookInfo.objects.aggregate(Sum(‘bread’))
 {‘bread__sum’:120} 注意返回值类型及键名

- count函数
 作用：统计满足条件数据的数目。

例：统计所有图书的数目。
 BookInfo.objects.all().count()
 例：统计id大于3的所有图书的数目。
 BookInfo.objects.filter(id__gt = 3).count()

### 模型类关系
 1）一对多关系
 例：图书类-英雄类
 models.ForeignKey() 定义在多的类中。

2）多对多关系
 例：新闻类-新闻类型类
 models.ManyToManyField() 定义在哪个类中都可以。

3）一对一关系
 例：员工基本信息类-员工详细信息类
 models.OneToOneField() 定义在哪个类中都可以。

 

 

 

 

 