作者：坏蛋

  


链接：https://www.zhihu.com/question/20607351/answer/275661602

  


来源：知乎

  


著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

  





今天心血来潮给大家写个新手到黑客入门的路径图【附全部学习资料下载】！

写在前面，这是我重新发布的一次，我的回答被举报删除了，不知道谁举报的，但是希望不要用恶意的心态去看待分享这件事情，我分享都是能够帮助到大家的，如果再被举报删除，那我也无话可说。

**入门介绍：**

说到黑客大家可能觉得很神秘，其实我们说的的黑客是白帽子黑客，就是去寻找网站、系统、软件等漏洞并帮助厂商修复的人，刚入门的黑客大部分从事渗透工作，而渗透大部分属于web安全方向，就是利用漏洞来取得一些数据或达到控制，让对方程序崩溃等效果。

**一些常用的名词解释：**

挖洞的话，就相当于在程序中查找漏洞，举一个不大恰当但容易理解的比喻，就像韩非子说所的那个自相矛盾的故事：楚国有个人自称自己的矛是世界上最锋利的矛，没有什么盾牌它刺不破，同时又说自己的盾是世界上最坚固的盾，没有什么矛能刺破它，虽然两句话在语法上并没有什么不妥，但却有个致命的逻辑漏洞，因为用他的矛刺他的盾，将导致“不可预知”的结果，当然了，在程序中这种“不可预知”的结果往往会导致各种问题，崩溃或执行非预期功能都有可能，这个就是漏洞了。

再来说说后门，这个很好比喻，就像是警匪片中的卧底或者是笑傲江湖中的岳不群，表面上做一套，背地里做另一套。在软件中就是这个软件提供给你了你需要的功能，但在背后它可能偷偷摸摸地干了一些你不想他干的事，例如窃取你电脑上的文件。

0day和挖洞是相关的，漏洞发布后，厂商一般不能说马上把漏洞填补了，那么这段时间这个漏洞是可利用的，久而久之，我们把那些刚发布的漏洞（或者说根本没发布自己偷偷用的漏洞）叫做0day，当然了，它的杀伤力较一些老的漏洞往往大的多。

肉鸡的话我们可以直接理解为已经中了木马受我们控制的傀儡计算机，我们可以控制傀儡机做一些我们不直接做的事情。Web安全必须要了解Web方面的一些基础知识做为铺垫的去的去学习这门技术，因为不是人人都可以直接先渗透在进行编程等方面学习的、所以为了更好的入门的Web安全必须要先掌握一些基础知识，相比对逆向方面的入门Web安全真的不难，逆向要是想了解一个简单的什么叫jmp esp溢出需要的基础知识不是一点点，如果是计算机专业的还好，不然通过自己去学习真的不是那么简单，不说太多，下面我就给大家推荐一个前期学习知识的路径和资源链接。

## 进入学习阶段：

首先是我给大家推荐的是前端的html/css/js + php进行学习，前端的这些都是肯定需要学习的知识，至于后端的编程语言我建议还是php，主要是因为入门学习快、目的呢就是更快的接触到php+mysql开发，这样前前后后的知识加起来才能在知识链上完整构成一个网站，这样做的好处的就是快速了解一个网站如何开发，什么是前端和后端？什么是http？什么是数据库，网站的数据都存储在哪？

当然不怕枯燥的话从C语言开始学起更佳，相比于C语言这种学习了半载一年还不一定有什么成果的玩意，直接用工具按照教程来达到目的会容易且有趣的多，但学习C语言在很多的时候，往往能够学习到C语言之外的东西，对程序的运行，内存的分配与管理，数据结构甚至是编程的书写习惯，都有非常大的好处，可以说，C语言学会后再学习其它大部分的语言都会快得多。

  


**第一部分资源链接如下（解压密码在回答底部）：**

这套PHP的教程包含了html/css/js和php+mysql保证一天看一课时的一个月就可以掌握，文件中的“就业班”的文件夹包括了一些后续的jquery+ajax+xml等等， 在前期的学习过程中这些后续知识可以选择性学习

链接: [https://pan.baidu.com/s/1pMZqRaF](http://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1pMZqRaF) 密码：st4m

  


下面这个链接是HTTP协议的教程来源自燕十八php教程中，我觉得这个http讲解的非常好

链接: [https://pan.baidu.com/s/1pNgIyNp](http://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1pNgIyNp) 密码：kfi7

  


在学习了上面教程恭喜你已经简单的入门了Web，接下来了就是进行安全的学习，这方面我给大家推荐一个教程就是我朋友黑无常的，网络上的教程个人觉得都不太适 合入门，除了个别的不错，大部分都是直入主题之家讲怎么利用，不适合学习！

**诚殷网络WEB渗透测试培训（基础篇）**

**链接:**[https://pan.baidu.com/s/1nwnrM2X](http://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1nwnrM2X)

**密码：**uehm

作者本人也非常擅长做教学，大家有兴趣可以加他好友，黑无常QQ：974168625（注明来自知乎）

  


在学习完成以上知识后就可以在各大漏洞平台或SRC平台找一些目标来实际的挖洞一下，前期肯定是花大量的时间也不一定的够挖到，所以可以加i春秋的QQ群问问群里的管理们：[556040588](tel:533191896)

**两个重要的思维导图：**

[情报收集思维图](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-29156-1-1.html)

[漏洞挖掘思维图](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-28641-1-1.html)

注释：SRC是各大互联网厂商的安全部门，负责审核你挖掘的漏洞并提供奖励。

**挖洞时一定首要学习前期的信息收集，俗称：踩点**

![](https://pic1.zhimg.com/v2-12dc29ea5c9327f5941a19056f7420ea_b.jpg)

**新手必看：**

[漫谈前期信息收集](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-27820-1-1.html%3Ffrom%3Dzh)

[信息收集系列之一--搜索引擎](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-13012-1-1.html)

[信息收集系列之二--轻量级信息收集工具](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-16018-1-1.html)

[信息收集系列之三-重量级信息收集工具](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-18453-1-1.html)

[工具\|手把手教你信息收集之子域名收集器](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-29420-1-1.html)

  


**注：挖洞只为提交漏洞，维护网络安全，请勿做出违法行为，网络安全法规已出。**

[你是如何看待网络安全法的出台的？它会对你造成什么影响？](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-14963-1-1.html)

[谈网络安全法的一些想法](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-23452-1-1.html)

  


**第二部分资源链接如下：**

好了，在学习上面的教程中已经可以算是安全入门了，不过接下来还需要在一部进行学习

这部分是没有什么教程的，需要自己去百度学习，学习的内容就是2003、2008操作系统听着很简单对不对？

我需要大家使用以上的操作系统使用网上的已有的CMS\(如:discuz,WordPress,phpcms,dedecms等\)大家一个站点，从在服务器上安装和配置php+apache+mysql等环 境开始，不要使用集成工具偷懒，去体会一个网站的搭建流程，知道是什么ftp，什么是空间，在网上买的虚拟主机和服务器，vps是个什么区别？什么是CMS目标站点？

我建议是自行在空间商购买一个服务器，价格一个月在100以内就可以了！

注：如果是不能购买那么请学习安装虚拟机本地使用镜像搭建服务器环境

以上的内容的最好通过百度自己完成，这些小问题都是百度都可以解决，要学会使用百度，不要什么问题都去问别人！！！

![](https://pic3.zhimg.com/v2-7ad4d3c7c4d31eac634c2e5c84f16c7d_b.jpg)

  


接下来肯定是一部分的linux知识学习了

是一个在线的教程

[http://study.163.com/course/courseMain.htm?courseId=983014](http://link.zhihu.com/?target=http%3A//study.163.com/course/courseMain.htm%3FcourseId%3D983014)

  


接着可以学习一门可以方便我们写exploit利用工具的编程语言，首选肯定是python 优点：入门快，网络编程拥有强大的各种库做支持，更易编写工具

一套的简易的在线教程，来自于中谷python，学习完毕后写一些简单的GET/POST型工具练练手不是问题

[http://www.icoolxue.com/album/show/113](http://link.zhihu.com/?target=http%3A//www.icoolxue.com/album/show/113)

[Python大法从入门到编写POC](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/forum.php%3Fmod%3Dcollection%26action%3Dview%26ctid%3D96)

  


**注：**第二部分的同样的很重要，了解网站的搭建构成，什么是CMS，对渗透很有帮助，现在大多数的网站基本上都是使用的CMS建站，因为安全，方便，模板样式也多，通常在渗透过程中我们对目标的信息收集就要着重关注这些程序的版本是不是最新的？如果不是有没有漏洞呢？

  


**第三部分资源链接如下：**

这部分是一大块，我不打算在细分了，之前的内容几个月就可以完成，下面的内容能1年内完成都可以说是很不错的！

这部分我认为应该需要掌握TCP/IP原理以及进一步的提升编程技术。

  


教主的TCP/IP教程

链接: [https://pan.baidu.com/s/1dEMM8t7](http://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1dEMM8t7)密码：ybmm

  


传智的前端的教程，非常推荐学习！

链接: [https://pan.baidu.com/s/1bqy18Ur](http://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1bqy18Ur) 密码：hsyf

  


传智的的Java教程，选择性学习，如果感兴趣Java的可以学习。如果不学习也可以看看里面的oracle数据库教程！

链接: [https://pan.baidu.com/s/1mhQA4hM](http://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1mhQA4hM) 密码：kx29

  


有两套Python的教程，都是系统的pythonWeb开发，选择一套学习即可

链接: [https://pan.baidu.com/s/1jJJmbDc](http://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1jJJmbDc) 密码: r7tb

  


**完成基础的姿势学习后，一定要多看看其他白帽黑客的实战思路，对你的实践是非常有帮助的，知识是死的，思路是活的。**

[白帽子分享挖洞技术/思路的实战内容【建议收藏】](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/forum-59-1.html%3Ffrom%3Dzh)

  


**挖洞小帮手：**

[AG安全团队2017大型工具包](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-21457-1-1.html%3Ffrom%3Dzh)

![](https://pic1.zhimg.com/v2-2a2436e088f727d54d7a0a18c0c1da06_b.jpg)

**进阶了解/学习：**

[汇编基础视频+天草逆向视频](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-30349-1-1.html%3Ffrom%3Dzh)

[逆向/破解/病毒分析实战分享【经常更新，建议收藏】](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/forum-60-1.html%3Ffrom%3Dzh)

  


**社会工程学也是必不可少的一项技能：**

[社工盒子 最全面的社会工程学工具](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-25409-1-1.html%3Ffrom%3Dzh)

[常见社工方法以及如何防社工](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-29654-1-1.html%3Ffrom%3Dzh)

[社工之经度纬度定位-50米以内](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-23489-1-1.html%3Ffrom%3Dzh)

[阐述网络上所有定位方法-超高精确定位](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/thread-25000-1-1.html%3Ffrom%3Dzh)

  


**资源不够的话可以去这里搜一下**

[超级多的白帽黑客工具/源码类集合【经常更新，建议收藏】](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/forum-65-1.html%3Ffrom%3Dzh)

[超级多的白帽黑客视频/书籍教程集合【经常更新，建议收藏】](http://link.zhihu.com/?target=https%3A//bbs.ichunqiu.com/forum-42-1.html%3Ffrom%3Dzh)

## **结语：**

其实在接触了Web安全1年之后大家都自己也能知道自己以后的学习目标，第三部分主要还是推荐些好的资源！

学习过程中，尤其是前期学习千万不要放弃，三天两头的进行学习，同时学习的过程中要记录图文并茂的笔试，最重要的进行实践，实践，实践！

在实践中发现问题，解决问题！安全非一朝一夕之事。

**注：解密密码请看压缩包注释**

【解压密码直接放出来吧：复制这个网址粘贴解密，[www.lthack.com/php](http://link.zhihu.com/?target=http%3A//www.lthack.com/php)

不用点击，复制这个网址就行，非广告，无用的网址。】

![](https://pic1.zhimg.com/v2-e59948c4947f01347dbadc64c6731ecc_b.jpg)

  





**最后的最后，这么多干货学习资源，别光顾着收藏啊，点个赞+关注合情合理吧**

![](https://pic4.zhimg.com/v2-c71fb618a67e503a602445299b708c4b_b.jpg)

  


**最后的最后，这么多干货学习资源，别光顾着收藏啊，点个赞+关注合情合理吧**

![](https://pic4.zhimg.com/v2-c71fb618a67e503a602445299b708c4b_b.jpg)

