# MTV
Django的MTV模式本质上与MVC模式没有什么差别，也是各组件之间为了保持松耦合关系，只是定义上有些许不同，Django的MTV分别代表：

​       Model(模型)：负责业务对象与数据库的对象(ORM)

​       Template(模版)：负责如何把页面展示给用户

​       View(视图)：负责业务逻辑，并在适当的时候调用Model和Template

​       此外，Django还有一个url分发器，它的作用是将一个个URL的页面请求分发给不同的view处理，view再调用相应的Model和Template

# MVC
MVC 模式同时提供了对 HTML、CSS 和 JavaScript 的完全控制。

Model（模型）是应用程序中用于处理应用程序数据逻辑的部分。
　　通常模型对象负责在数据库中存取数据。
View（视图）是应用程序中处理数据显示的部分。
　　通常视图是依据模型数据创建的（前端网页）。
Controller（控制器）是应用程序中处理用户交互的部分。
　　通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据（映射，模式渲染等）。