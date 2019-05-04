# 1.对缺省参数的理解。给出代码

缺省参数在python中是与函数绑定在一起的。
 也就是说，一个函数中定义了一个缺省参数，那么这个参数会随着被调用而改变。

```
def extendList(val, list=[]):
    list.append(val)
    return list
list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')
print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)
结果为：
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
```

## 解释说明：

许多人会错误的认为 list1 应该等于 [10] 以及 list3 应该等于 ['a']。认为 list 的参数会在 extendList 每次被调用的时候会被设置成它的默认值 []。
 尽管如此，实际发生的事情是，新的默认列表list仅仅只在函数被定义时创建一次。随后当 extendList 没有被指定的列表参数调用的时候，其使用的是同一个列表list。
 因此，list1 和 list3 是操作的相同的列表（也就是[]对象的引用相同，id值也就相同）。而list2是操作它创建独立的列表（通过传递它自己的空列表作为list参数的值）
 所以这一点一定要切记切记.

下面代码，我们把list置为None就可以避免一些麻烦了

```
def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list
结果为：
list1 = [10]
list2 = [123]
list3 = ['a']
```

None是一个常量， 是一个不可变对象， 每次调用myfunc()时value都是None。
 但是id值每次都是不同的，每次 list都是一个新的 list，因此每次 id(value) 都不一样。

# 2.对装饰器的理解。给出代码

## 1. 函数

在python中，函数通过def关键字、函数名和可选的参数列表定义。通过return关键字返回值。我们举例来说明如何定义和调用一个简单的函数：

```
def foo():
     return 1
foo()
1
```

方法体（当然多行也是一样的）是必须的，通过缩进来表示，在方法名的后面加上双括号()就能够调用函数

## 2. 作用域

在python中，函数会创建一个新的作用域。
 python开发者可能会说函数有自己的命名空间，差不多一个意思。
 这意味着在函数内部碰到一个变量的时候函数会优先在自己的命名空间里面去寻找。让我们写一个简单的函数看一下 本地作用域 和 全局作用域有什么不同：

```
a_string = "This is a global variable"
def foo():
     print locals()
print globals() # doctest: +ELLIPSIS
{, 'a_string': 'This is a global variable'}
foo() # 2
{}
```

内置的函数globals返回一个包含所有python解释器知道的变量名称的字典（为了干净和洗的白白的，我省略了python自行创建的一些变量）。在#2我调用了函数 foo 把函数内部本地作用域里面的内容打印出来。我们能够看到，函数foo有自己独立的命名空间，虽然暂时命名空间里面什么都还没有。

## 3. 变量解析规则

当然这并不是说我们在函数里面就不能访问外面的全局变量。在python的作用域规则里面，创建变量一定会在当前作用域里创建一个变量，但是访问或者修改变量时会先在当前作用域查找变量，没有找到匹配变量的话会依次向上在闭合的作用域里面进行查找。所以如果我们修改函数foo的实现让它打印全局的作用域里的变量也是可以的：

```
a_string = "This is a global variable"
def foo():
     print a_string # 1
foo()
This is a global variable
```

在#1处，python解释器会尝试查找变量a_string，当然在函数的本地作用域里面是找不到的，所以接着会去上层的作用域里面去查找。
 但是另一方面，假如我们在函数内部给全局变量赋值，结果却和我们想的不一样：

```
a_string = "This is a global variable"
def foo():
     a_string = "test" # 1
     print locals()
foo()
{'a_string': 'test'}
a_string # 2
'This is a global variable'
```

我们能够看到，全局变量能够被访问到（如果是可变数据类型(像list,dict这些)甚至能够被更改）但是赋值不行。在函数内部的#1处，我们实际上新创建了一个局部变量，隐藏全局作用域中的同名变量。我们可以通过打印出局部命名空间中的内容得出这个结论。我们也能看到在#2处打印出来的变量a_string的值并没有改变。

## 4. 变量生存周期

值得注意的一个点是，变量不仅是生存在一个个的命名空间内，他们都有自己的生存周期，请看下面这个例子：

```
def foo():
     x = 1
foo()
print x # 1
Traceback (most recent call last):
 
NameError: name 'x' is not defined
#1处发生的错误不仅仅是因为作用域规则导致的（尽管这是抛出了NameError的错误的原因）它还和python以及其它很多编程语言中函数调用实现的机制有关。在这个地方这个执行时间点并没有什么有效的语法让我们能够获取变量x的值，因为它这个时候压根不存在！函数foo的命名空间随着函数调用开始而开始，结束而销毁。
```

## 5. 函数参数

python允许我们向函数传递参数，参数会变成本地变量存在于函数内部。

```
def foo(x):
     print locals()
foo(1)
{'x': 1}
```

在Python里有很多的方式来定义和传递参数，完整版可以查看 python官方文档。我们这里简略的说明一下：函数的参数可以是必须的位置参数或者是可选的命名参数（也叫默认参数）或者可变参数或者关键字参数。

```
def foo(x, y=0): # 1
     return x - y
foo(3, 1) # 2
2
foo(3) # 3
3
foo() # 4
Traceback (most recent call last):
 
TypeError: foo() takes at least 1 argument (0 given)
foo(y=1, x=3) # 5
2
```

在#1处我们定义了函数foo,它有一个位置参数x和一个命名参数y。
 在#2处我们能够通过常规的方式来调用函数，尽管有一个命名参数，但参数依然可以通过位置传递给函数。在调用函数的时候，对于命名参数y我们也可以完全不管就像#3处所示的一样。如果命名参数没有接收到任何值的话，python会自动使用声明的默认值也就是0。需要注意的是我们不能省略第一个位置参数x, 否则的话就会像#4处所发生错误。

目前还算简洁清晰吧， 但是接下来可能会有点令人困惑。python支持函数调用时的命名参数（个人觉得应该是命名实参）。看看#5处的函数调用，我们传递的是两个命名实参，这个时候因为有名称标识，参数传递的顺序也就不用在意了。

当然相反的情况也是正确的：函数的第二个形参是y，但是我们通过位置的方式传递值给它。在#2处的函数调用foo(3,1)，我们把3传递给了第一个参数x，把1传递给了第二个参数y，尽管第二个参数是一个命名参数。

桑不起，感觉用了好大一段才说清楚这么一个简单的概念：函数的参数可以有名称和位置。这意味着在函数的定义和调用的时候会稍稍在理解上有点儿不同。我们可以给只定义了位置参数的函数传递命名参数（实参），反之亦然！如果觉得不够可以查看官方文档

## 6. 嵌套函数

Python允许创建嵌套函数。这意味着我们可以在函数里面定义函数而且现有的作用域和变量生存周期依旧适用。

```
def outer():
     x = 1
     def inner():
         print x # 1
     inner() # 2
 
outer()
1
```

这个例子有一点儿复杂，但是看起来也还行。
 想一想在#1发生了什么：python解释器需找一个叫x的本地变量，查找失败之后会继续在上层的作用域里面寻找，这个上层的作用域定义在另外一个函数里面。对函数outer来说，变量x是一个本地变量，但是如先前提到的一样，函数inner可以访问封闭的作用域（至少可以读和修改）。在#2处，我们调用函数inner，非常重要的一点是，inner也仅仅是一个遵循python变量解析规则的变量名，python解释器会优先在outer的作用域里面对变量名inner查找匹配的变量.

## 7. 函数是python世界里的一级类对象

显而易见，在python里函数和其他东西一样都是对象。（此处应该大声歌唱）啊！包含变量的函数，你也并不是那么特殊！

```
issubclass(int, object) # all objects in Python inherit from a common baseclass
True
def foo():
     pass
foo.__class__ # 1
<type 'function'>
issubclass(foo.__class__, object)
True
```

你也许从没有想过，你定义的函数居然会有属性。没办法，函数在python里面就是对象，和其他的东西一样，也许这样描述会太学院派太官方了点：在python里，函数只是一些普通的值而已和其他的值一毛一样。这就是说你可以把函数当参数一样传递给其他的函数或者说从函数里面返回函数！如果你从来没有这么想过，那看看下面这个例子：

```
def add(x, y):
     return x + y
def sub(x, y):
     return x - y
def apply(func, x, y): # 1
     return func(x, y) # 2
apply(add, 2, 1) # 3
3
apply(sub, 2, 1)
1
```

这个例子对你来说应该不会很奇怪。add和sub是非常普通的两个python函数，接受两个值，返回一个计算后的结果值。
 在#1处你们能看到准备接收一个函数的变量只是一个普通的变量而已，和其他变量一样。在#2处我们调用传进来的函数：“()”代表着调用的操作并且调用变量包含的值。
 在#3处，你们也能看到传递函数并没有什么特殊的语法。
 函数的名称只是与其他变量一样的标识符而已。

你们也许看到过这样的行为：“python把频繁要用的操作变成函数作为参数进行使用，想通过传递一个函数给内置排序函数的key参数，从而来自定义排序规则。”

那把函数当做返回值回事这样的情况呢：

```
def outer():
     def inner():
         print "Inside inner"
     return inner # 1
 
foo = outer() #2
foo # doctest:+ELLIPSIS
<function inner at 0x>
foo()
Inside inner
```

这个例子看起来也许会更加的奇怪。在#1处我把恰好是函数标识符的变量inner作为返回值返回出来。这并没有什么特殊的语法：”把函数inner返回出来，否则它根本不可能会被调用到。“还记得变量的生存周期吗？每次函数outer被调用的时候，函数inner都会被重新定义，如果它不被当做变量返回的话，每次执行过后它将不复存在，也就是没有变量来接收返回的值。

在#2处我们捕获住返回值 – 函数inner，将它存在一个新的变量foo里。
 我们能够看到，当对变量foo进行求值，它确实包含函数inner，而且我们能够对他进行调用。初次看起来可能会觉得有点奇怪，但是理解起来并不困难是吧。坚持住，因为奇怪的转折马上就要来了

## 8. 闭包

我们先不急着定义什么是闭包，先来看看一段代码，仅仅是把上一个例子简单的调整了一下：

```
def outer():
     x = 1
     def inner():
         print x # 1
     return inner
foo = outer()
foo.func_closure 
(<cell at 0x: int object at 0x>,)
```

在上一个例子中我们了解到，inner作为一个函数被outer返回，保存在一个变量foo，并且我们能够对它进行调用foo()。不过它会正常的运行吗？我们先来看看作用域规则。

所有的东西都在python的作用域规则下进行工作：“x是函数outer里的一个局部变量。当函数inner在#1处打印x的时候，python解释器会在inner内部查找相应的变量，当然会找不到，所以接着会到封闭作用域里面查找，并且会找到匹配。

但是从变量的生存周期来看，该怎么理解呢？我们的变量x是函数outer的一个本地变量，这意味着只有当函数outer正在运行的时候才会存在。根据我们已知的python运行模式，我们没法在函数outer返回之后继续调用函数inner，在函数inner被调用的时候，变量x早已不复存在，可能会发生一个运行时错误。

万万没想到，返回的函数inner居然能够正常工作。Python支持一个叫做函数闭包的特性，用人话来讲就是，嵌套定义在非全局作用域里面的函数能够记住它在被定义的时候它所处的封闭命名空间。
 这能够通过查看函数的(py2是func_closure，py3是-closure-)属性得出结论，这个属性里面包含封闭作用域里面的值（只会包含被捕捉到的值（或者叫被引用的值），比如x，如果在outer里面还定义了其他的值，封闭作用域里面是不会有的)

记住，每次函数outer被调用的时候，函数inner都会被重新定义。现在变量x的值不会变化，所以每次返回的函数inner会是同样的逻辑，假如我们稍微改动一下呢？

```
def outer(x):
     def inner():
         print x # 1
     return inner
print1 = outer(1)
print2 = outer(2)
print1()
1
print2()
2
```

从这个例子中你能够看到闭包 – 被函数记住的封闭作用域 – 能够被用来创建自定义的函数，本质上来说是一个硬编码的参数。事实上我们并不是传递参数1或者2给函数inner，我们实际上是创建了能够打印各种数字的各种自定义版本。

闭包单独拿出来就是一个非常强大的功能， 在某些方面，你也许会把它当做一个类似于面向对象的技术：outer像是给inner服务的构造器，x像一个私有变量。

不过，我们现在不会用闭包做这么low的事(⊙o⊙)…！相反，让我们再爽一次，写一个高大上的装饰器!

## 9. 装饰器

装饰器其实就是一个闭包，把一个函数当做参数然后返回一个替代版函数。我们一步步从简到繁来瞅瞅：

```
def outer(some_func):
     def inner():
         print "before some_func"
         ret = some_func() # 1
         return ret + 1
     return inner
def foo():
     return 1
decorated = outer(foo) # 2
decorated()
before some_func
2
```

仔细看看上面这个装饰器的例子。们定义了一个函数outer，它只有一个some_func的参数，在他里面我们定义了一个嵌套的函数inner。inner会打印一串字符串，然后调用some_func，在#1处得到它的返回值。在outer每次调用的时候some_func的值可能会不一样，但是不管some_func的值如何，我们都会调用它。最后，inner返回some_func() + 1的值 – 我们通过调用在#2处存储在变量decorated里面的函数能够看到被打印出来的字符串以及返回值2，而不是期望中调用函数foo得到的返回值1。

我们可以认为变量decorated是函数foo的一个装饰版本，一个加强版本。事实上如果打算写一个有用的装饰器的话，我们可能会想愿意用装饰版本完全取代原先的函数foo，这样我们总是会得到我们的”加强版“foo。想要达到这个效果，完全不需要学习新的语法，简单的赋值给变量foo就行了：

```
foo = outer(foo)
foo # doctest: +ELLIPSIS
<function inner at 0x>
```

现在，任何怎么调用都不会牵扯到原先的函数foo，都会得到新的装饰版本的foo，现在我们还是来写一个有用的装饰器。

想象我们有一个库，这个库能够提供类似坐标的对象，也许它们仅仅是一些x和y的坐标对。不过可惜的是这些坐标对象不支持数学运算符，而且我们也不能对源代码进行修改，因此也就不能直接加入运算符的支持。我们将会做一系列的数学运算，所以我们想要能够对两个坐标对象进行合适加减运算的函数，这些方法很容易就能写出：

```
class Coordinate(object):
     def __init__(self, x, y):
         self.x = x
         self.y = y
     def __repr__(self):
         return "Coord: " + str(self.__dict__)
def add(a, b):
     return Coordinate(a.x + b.x, a.y + b.y)
def sub(a, b):
     return Coordinate(a.x - b.x, a.y - b.y)
one = Coordinate(100, 200)
two = Coordinate(300, 200)
add(one, two)
Coord: {'y': 400, 'x': 400}
```

如果不巧我们的加减函数同时也需要一些边界检查的行为那该怎么办呢？搞不好你只能够对正的坐标对象进行加减操作，任何返回的值也都应该是正的坐标。所以现在的期望是这样：

```
one = Coordinate(100, 200)
two = Coordinate(300, 200)
three = Coordinate(-100, -100)
sub(one, two)
Coord: {'y': 0, 'x': -200}
add(one, three)
Coord: {'y': 100, 'x': 0}
```

我们期望在不更改坐标对象one, two, three的前提下one减去two的值是{x: 0, y: 0}，one加上three的值是{x: 100, y: 200}。与其给每个方法都加上参数和返回值边界检查的逻辑，我们来写一个边界检查的装饰器！

```
def wrapper(func):
     def checker(a, b): # 1
         if a.x < 0 or a.y < 0:
             a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
         if b.x < 0 or b.y < 0:
             b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
         ret = func(a, b)
         if ret.x < 0 or ret.y < 0:
             ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
         return ret
     return checker
add = wrapper(add)
sub = wrapper(sub)
sub(one, two)
Coord: {'y': 0, 'x': 0}
add(one, three)
Coord: {'y': 200, 'x': 100}
```

这个装饰器能想先前的装饰器例子一样进行工作，返回一个经过修改的函数，但是在这个例子中，它能够对函数的输入参数和返回值做一些非常有用的检查和格式化工作，将负值的x和 y替换成0。

显而易见，通过这样的方式，我们的代码变得更加简洁：将边界检查的逻辑隔离到单独的方法中，然后通过装饰器包装的方式应用到我们需要进行检查的地方。另外一种方式通过在计算方法的开始处和返回值之前调用边界检查的方法也能够达到同样的目的。但是不可置否的是，使用装饰器能够让我们以最少的代码量达到坐标边界检查的目的。事实上，如果我们是在装饰自己定义的方法的话，我们能够让装饰器应用的更加有逼格。

## 10. 使用 @ 标识符将装饰器应用到函数

Python支持使用标识符@将装饰器应用在函数上，只需要在函数的定义前加上@和装饰器的名称。在上一节的例子里我们是将原本的方法用装饰后的方法代替:

```
add = wrapper(add)
```

这种方式能够在任何时候对任意方法进行包装。但是如果我们自定义一个方法，我们可以使用@进行装饰：

```
@wrapper
def add(a, b):
     return Coordinate(a.x + b.x, a.y + b.y)
```

需要明白的是，这样的做法和先前简单的用包装方法替代原有方法是一毛一样的， python只是加了一些语法糖让装饰的行为更加的直接明确和优雅一点。

## 11. *args and **kwargs

我们已经完成了一个有用的装饰器，但是由于硬编码的原因它只能应用在一类具体的方法上，这类方法接收两个参数，传递给闭包捕获的函数。如果我们想实现一个能够应用在任何方法上的装饰器要怎么做呢？再比如，如果我们要实现一个能应用在任何方法上的类似于计数器的装饰器，不需要改变原有方法的任何逻辑。这意味着装饰器能够接受拥有任何签名的函数作为自己的被装饰方法，同时能够用传递给它的参数对被装饰的方法进行调用。

非常巧合的是Python正好有支持这个特性的语法。可以阅读 Python Tutorial 获取更多的细节。当定义函数的时候使用了*，意味着那些通过位置传递的参数将会被放在带有*前缀的变量中， 所以：

```
def one(*args):
     print args # 1
one()
()
one(1, 2, 3)
(1, 2, 3)
def two(x, y, *args): # 2
     print x, y, args
two('a', 'b', 'c')
a b ('c',)
```

第一个函数one只是简单地讲任何传递过来的位置参数全部打印出来而已，你们能够看到，在代码#1处我们只是引用了函数内的变量args, *args仅仅只是用在函数定义的时候用来表示位置参数应该存储在变量args里面。Python允许我们制定一些参数并且通过args捕获其他所有剩余的未被捕捉的位置参数，就像#2处所示的那样。

*操作符在函数被调用的时候也能使用。意义基本是一样的。当调用一个函数的时候，一个用*标志的变量意思是变量里面的内容需要被提取出来然后当做位置参数被使用。同样的，来看个例子：

```
def add(x, y):
     return x + y
lst = [1,2]
add(lst[0], lst[1]) # 1
3
add(*lst) # 2
3
#1处的代码和#2处的代码所做的事情其实是一样的，在#2处，python为我们所做的事其实也可以手动完成。这也不是什么坏事，*args要么是表示调用方法大的时候额外的参数可以从一个可迭代列表中取得，要么就是定义方法的时候标志这个方法能够接受任意的位置参数。
```

接下来提到的**会稍多更复杂一点，**代表着键值对的参数字典，和*所代表的意义相差无几，也很简单对不对：

```
def foo(**kwargs):
     print kwargs
foo()
{}
foo(x=1, y=2)
{'y': 2, 'x': 1}
```

当我们定义一个函数的时候，我们能够用*kwargs来表明，所有未被捕获的关键字参数都应该存储在kwargs的字典中。如前所诉，args和kwargs并不是python语法的一部分，但在定义函数的时候，使用这样的变量名算是一个不成文的约定。和一样，我们同样可以在定义或者调用函数的时候使用**。

```
dct = {'x': 1, 'y': 2}
def bar(x, y):
     return x + y
bar(**dct)
3
```

## 12. 更通用的装饰器

有了这招新的技能，我们随随便便就可以写一个能够记录下传递给函数参数的装饰器了。先来个简单地把日志输出到界面的例子：

```
def logger(func):
     def inner(*args, **kwargs): #1
         print "Arguments were: %s, %s" % (args, kwargs)
         return func(*args, **kwargs) #2
     return inner
```

请注意我们的函数inner，它能够接受任意数量和类型的参数并把它们传递给被包装的方法，这让我们能够用这个装饰器来装饰任何方法。

```
@logger
def foo1(x, y=1):
     return x * y
@logger
def foo2():
     return 2
foo1(5, 4)
Arguments were: (5, 4), {}
20
foo1(1)
Arguments were: (1,), {}
1
foo2()
Arguments were: (), {}
2
```

随便调用我们定义的哪个方法，相应的日志也会打印到输出窗口，和我们预期的一样。

# 3.线程安全，互斥锁。给出代码

## 1，问题的提出

每个线程互相独立，相互之间没有任何关系。现在假设这样一个例子：有一个全局的计数num，每个线程获取这个全局的计数，根据num进行一些处理，然后将num加1。代码如下：

```
# encoding: UTF-8
import threading
import time
class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        num = num+1
        msg = self.name+' set num to '+str(num)
        print msg
num = 0
def test():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    test()
但是运行结果是不正确的：
Thread-5 set num to 2
Thread-3 set num to 3
Thread-2 set num to 5
Thread-1 set num to 5
Thread-4 set num to 4
```

问题产生的原因就是没有控制多个线程对同一资源的访问，对数据造成破坏，使得线程运行的结果不可预期。这种现象称为“线程不安全”。

## 2，互斥锁同步

上面的例子引出了多线程编程的最常见问题：数据共享。当多个线程都修改某一个共享数据的时候，需要进行同步控制。

线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁。互斥锁为资源引入一个状态：锁定/非锁定。某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。

threading模块中定义了Lock类，可以方便的处理锁定：

```
#创建锁
mutex = threading.Lock()
#锁定
mutex.acquire([timeout])
#释放
mutex.release()
```

其中，锁定方法acquire可以有一个超时时间的可选参数timeout。如果设定了timeout，则在超时后通过返回值可以判断是否得到了锁，从而可以进行一些其他的处理。
 使用互斥锁实现上面的例子的代码如下：

```
import threading
import time
class MyThread(threading.Thread):
    def run(self):
        global num 
        time.sleep(1)
        if mutex.acquire(1):  
            num = num+1
            msg = self.name+' set num to '+str(num)
            print msg
            mutex.release()
num = 0
mutex = threading.Lock()
def test():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    test()
运行结果：
Thread-3 set num to 1
Thread-4 set num to 2
Thread-5 set num to 3
Thread-2 set num to 4
Thread-1 set num to 5
```

可以看到，加入互斥锁后，运行结果与预期相符。

## 3，同步阻塞

当一个线程调用锁的acquire()方法获得锁时，锁就进入“locked”状态。每次只有一个线程可以获得锁。如果此时另一个线程试图获得这个锁，该线程就会变为“blocked”状态，称为“同步阻塞”

直到拥有锁的线程调用锁的release()方法释放锁之后，锁进入“unlocked”状态。线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁，并使得该线程进入运行（running）状态。

# 4.单例模式，至少两种。写代码

```
1.#-*- encoding=utf-8 -*-  
2.print '----------------------方法1--------------------------'  
3.#方法1,实现__new__方法  
4.#并在将一个类的实例绑定到类变量_instance上,  
5.#如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回  
6.#如果cls._instance不为None,直接返回cls._instance  
7.class Singleton(object):  
8.    def __new__(cls, *args, **kw):  
9.        if not hasattr(cls, '_instance'):  
10.            cls._instance = super(Singleton, cls).__new__(*args, **kw)  
11.        return cls._instance  
12.  
13.class MyClass(Singleton):  
14.    a = 1  
15.  
16.one = MyClass()  
17.two = MyClass()  
18.  
19.  
20.print '----------------------方法2--------------------------'  
21.#方法2,共享属性;所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)  
22.#同一个类的所有实例天然拥有相同的行为(方法),  
23.#只需要保证同一个类的所有实例具有相同的状态(属性)即可  
24.#所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)  
25.class Borg(object):  
26.    _state = {}  
27.    def __new__(cls, *args, **kw):  
28.        ob = super(Borg, cls).__new__(cls, *args, **kw)  
29.        ob.__dict__ = cls._state  
30.        return ob  
31.  
32.class MyClass2(Borg):  
33.    a = 1  
34.  
35.one = MyClass2()  
36.two = MyClass2()  
37.  
38.  
39.print '----------------------方法3--------------------------'  
40.#方法3:本质上是方法1的升级（或者说高级）版  
41.#使用__metaclass__（元类）的高级python用法  
42.class Singleton2(type):
43.    def __init__(cls, *args):
44.        super(Singleton2, cls).__init__(*args)
45.        cls._instance = None
46.
47.    def __call__(cls, *args, **kwargs):
48.        if cls._instance is None:
49.            cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)
50.        return cls._instance
51.
52.
53.class MyClass(object):
54.    __metaclass__ = Singleton2
55.  
56.one = MyClass3()  
57.two = MyClass3()  
58.  
59.  
60.print '----------------------方法4--------------------------'  
61.#方法4:也是方法1的升级（高级）版本,  
62.#使用装饰器(decorator),  
63.#这是一种更pythonic,更elegant的方法,  
64.#单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的  
65.def singleton(cls, *args, **kw):  
66.    instances = {}  
67.    def _singleton():  
68.        if cls not in instances:  
69.            instances[cls] = cls(*args, **kw)  
70.        return instances[cls]  
71.    return _singleton  
72. 
73.@singleton  
74.class MyClass4(object):  
75.    a = 1  
76.    def __init__(self, x=0):  
77.        self.x = x  
78.  
79.one = MyClass4()  
80.two = MyClass4()    
```

# 5.手写一个函数，传入一个文件路径，函数实现输出当前路径所有文件的功能。

## 第一种方法：

```
import os
def GetFileList(dir, fileList):
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
            #    continue
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList)

    return fileList

list = GetFileList('/home/xiaoke/ml_project/day01', [])
for e in list:
print(e)
```

## 第二种方法：

```
import os
def iterbrowse(path):
    for home, dirs, files in os.walk(path):
        for filename in files:
            yield os.path.join(home, filename)

for fullname in iterbrowse("/home/xiaoke/ml_project/day01"):
    print(fullname)
```

# 6.递归函数停止的条件。

## 递归定义：

递归就是在过程或函数里调用自身
 必须有一个明确的递归结束条件，称为递归出口。

## 递归需要出口条件，也就是停止

一般情况在递归内部需要一个分支判断，如：

```
def fab(n):
  if n<2:
    return 1
  else
return fab(n-1)+fab(n-2)
```

## 递归优点：

递归使代码看起来更加整洁、优雅
 可以用递归将复杂任务分解成更简单的子问题
 使用递归比使用一些嵌套迭代更容易
 递归缺点:
 递归的逻辑很难调试、跟进
 递归调用的代价高昂（效率低），因为占用了大量的内存和时间。
 过深的调用会导致栈溢出。
 案例阐述，递归函数
 我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：
 1   fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
 所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。
 于是，fact(n)用递归的方式写出来就是：

```
def fact(n):
  if n==1:
    return 1
  return n * fact(n - 1)
```

上面就是一个递归函数。可以试试：

```
>>> fact(1)
1
>>> fact(5)
120
>>> fact(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000L
如果我们计算fact(5)，可以根据函数定义看到计算过程如下：

===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
```

递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
 可以试试fact(1000)：

```
>>> fact(1000)
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "<stdin>", line 4, in fact
 ...
 File "<stdin>", line 4, in fact
RuntimeError: maximum recursion depth exceeded
```

## 案例阐述，尾递归函数

解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：

```
def fact(n):
  return fact_iter(1, 1, n)
  
def fact_iter(product, count, max):
  if count > max:
    return product
  return fact_iter(product * count, count + 1, max)
```

可以看到，return fact_iter(product * count, count + 1, max)仅返回递归函数本身，product * count和count + 1在函数调用前就会被计算，不影响函数调用。
 fact(5)对应的fact_iter(1, 1, 5)的调用如下：

```
===> fact_iter(1, 1, 5)
===> fact_iter(1, 2, 5)
===> fact_iter(2, 3, 5)
===> fact_iter(6, 4, 5)
===> fact_iter(24, 5, 5)
===> fact_iter(120, 6, 5)
===> 120
```

尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
 Python针对尾递归优化的装饰器源码
 有一个针对尾递归优化的decorator，可以参考源码：

```
def tail_call_optimized(g):
  """  This function decorates a function with tail call  optimization. It does this by throwing an exception  if it is it's own grandparent, and catching such  exceptions to fake the tail call optimization.    This function fails if the decorated  function recurses in a non-tail context.  """
  def func(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back \
        and f.f_back.f_back.f_code == f.f_code:
      raise TailRecurseException(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except TailRecurseException, e:
          args = e.args
          kwargs = e.kwargs
  func.__doc__ = g.__doc__
  return func
```

现在，只需要使用这个@tail_call_optimized装饰器，就可以顺利计算出fact(1000)

## 案例小总结

### 1，使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

### 2，针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

### 3，Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

# 7.Django创建项目的命令

django-admin startproject 项目名称
 python manage.py startapp 应用app名

# 8.Django创建项目后，项目文件夹下的组成部分以及对mvt的理解

项目文件夹下的组成部分
 manage.py是项目运行的入口，指定配置文件路径。
 与项目同名的目录，包含项目的配置文件
 ___init.py是一个空文件，作用是这个目录可以被当作包使用。
 settings.py是项目的整体配置文件。
 urls.py是项目的URL配置文件。
 wsgi.py是项目与WSGI兼容的Web服务器入口
 对MVT的理解

M全拼为Model，与MVC中的M功能相同，负责和数据库交互，进行数据处理。
 
 V全拼为View，与MVC中的C功能相同，接收请求，进行业务处理，返回应答。
 
 T全拼为Template，与MVC中的V功能相同，负责封装构造要返回的html。

# 9.记录url中间件的中间件名称

## 定义

Django中的中间件是一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，修改Django的输入或输出。中间件的设计为开发者提供了一种无侵入式的开发方式，增强了Django框架的健壮性

## 各个方法

1）初始化：无需任何参数， 服务器接收第一个请求时会被调用一次，而且只调用一次，用于确定是否启用当前中间件（也可以确定自定义的中间件是否启用）。
 def init():
 pass

2）在进行url匹配之前被调用，在每个请求上调用,返回None或HttpResponse对象。
 def process_request(request):
 pass

3）在url匹配之后，视图函数调用之前被调用，在每个请求上调用,返回None或HttpResponse对象。
 def process_view(request, view_func, view_args, view_kwargs):
 pass

4） 视图函数之后会被调用：所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象。
 def process_response(request, response):
 pass

5）异常处理：当视图函数抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象。
 def process_exception(request,exception):
 pass

# 10.Django中models利用ORM对mysql进行查表的语句

字段查询
 all():返回模型类对应表格中的所有数据。
 例：查询图书所有信息。
 BookInfo.objects.all();->select * from booktest_bookinfo;

get():返回表格中满足条件的一条数据。
 如果查到多条数据，则抛异常：MultipleObjectsReturned
 查询不到数据，则抛异常：DoesNotExist
 例：查询图书id为3的图书信息。
 BookInfo.objects.get(id=3) –> select * from booktest_bookinfo where id = 3;

filter():参数写查询条件，返回满足条件QuerySet集合数据。
 条件格式：
 **模型类属性名**__条件名=值
 注意：此处是模型类属性名，不是表中的字段名

关于filter具体案例如下：
 1.判等 exact。
 例：查询编号为1的图书。
 BookInfo.object.filter(id=1)
 BookInfo.object.filter(id__exact=1)此处的__exact可以省略

2.模糊查询 like
 例：查询书名包含'传'的图书。contains
 contains BookInfo.objects.filter(btitle__contains=’传’)
 例：查询书名以'部'结尾的图书 endswith 开头:startswith BookInfo.objects.filter(btitle__endswith=’部’)
 BookInfo.objects.filter(btitle__startswith=’天’)

3.空查询 where 字段名 isnull
 例：查询书名不为空的图书。isnull
 BookInfo.objects.filter(btitle__isnull=False)

4.范围查询 where id in (1,3,5)
 例：查询编号为1或3或5的图书。In
 BookInfo.objects.filter(id__in=[1,3,5])

5.比较查询 gt lt(less than) gte(equal) lte
 例：查询编号大于等于3的图书。
 BookInfo.objects.filter(id__gte=3)

6.日期查询
 例：查询1980年发表的图书。
 BookInfo.objects.filter(bpub_date__year = 1980)
 例：查询1980年1月1日后发表的图。
 BookInfo.objects.filter(bpub_date__gt = date(1980,1,1))

7.exclude:返回不满足条件的数据。
 例：查询id不为3的图书信息。
 BookInfo.objects.exclude(id=3)

F对象
 作用：用于类属性之间的比较条件。

使用之前需要先导入：
 from django.db.models import F
 例：查询图书阅读量大于评论量图书信息。where bread > bcomment BookInfo.objects.filter(bread__gt = F(‘bcomment’))
 例：查询图书阅读量大于2倍评论量图书信息。 BookInfo.objects.filter(bread__gt=F(‘bcomment’)*2)

Q对象
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

order_by 返回QuerySet
 作用：对查询结果进行排序。

例：查询所有图书的信息，按照id从小到大进行排序。
 BookInfo.objects.all().order_by('id')
 例：查询所有图书的信息，按照id从大到小进行排序。
 BookInfo.objects.all().order_by('-id')
 例：把id大于3的图书信息按阅读量从大到小排序显示；
 BookInfo.objects.filter(id__gt=3).order_by('-bread')

聚合函数
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

count函数
 作用：统计满足条件数据的数目。

例：统计所有图书的数目。
 BookInfo.objects.all().count()
 例：统计id大于3的所有图书的数目。
 BookInfo.objects.filter(id__gt = 3).count()

模型类关系
 1）一对多关系
 例：图书类-英雄类
 models.ForeignKey() 定义在多的类中。

2）多对多关系
 例：新闻类-新闻类型类
 models.ManyToManyField() 定义在哪个类中都可以。

3）一对一关系
 例：员工基本信息类-员工详细信息类
 models.OneToOneField() 定义在哪个类中都可以。

# 11.Django后台管理界面(admin)的了解

创建管理员的用户名和密码
 python manage.py createsuperuser
 按提示填写用户名、邮箱、密码

控制最后显示的空白表格，默认3条，设置为2条
 extra = 2
 每页显示10条数据
 list_per_page = 10
 在底部显示控制选项
 actions_on_bottom = True
 在顶部显示控制选项
 actions_on_top = False
 控制列表页显示表的哪些字段
 list_display = ['id', 'atitle', 'title', 'parent']
 侧边栏过滤框
 list_filter = ['atitle']
 搜索框
 search_fields = ['atitle']
 以下二者只能选其一
 fields = ['aParent', 'atitle']
 fieldsets = [ ('基本', {'fields':['atitle']}), ('高级', {'fields':['aParent']}) ]

# 12.对wsgi的理解

uWSGI 是一个 Web 服务器，它实现了 WSGI 协议、uwsgi协议、http 等协议。
 注意 uwsgi 是一种通信协议，它用于定义传输信息的类型，而 uWSGI 是实现 uwsgi 协议和 WSGI 协议的 Web 服务器。

uWSGI 具有超快的性能、低内存占用和多 app 管理等优点，并且搭配着 Nginx就是一个生产环境了，能够将用户访问请求与应用 app 隔离开，实现真正的部署 。相比来讲，支持的并发量更高，方便管理多进程，发挥多核的优势，提升性能。

为什么有了uWSGI为什么还需要nginx？
 因为nginx具备优秀的静态内容处理能力，然后将动态内容转发给uWSGI服务器，这样可以达到很好的客户端响应。

uwsgi 的参数：
 -M 开启Master进程
 -p 4 开启4个进程
 -s 使用的端口或者socket地址
 -d 使用daemon的方式运行, 注意, 使用-d后, 需要加上log文件地址, 比如-d /var/log/uwsgi.log
 -R 10000 开启10000个进程后, 自动respawn（复位）下
 -t 30 设置30s的超时时间, 超时后, 自动放弃该链接
 –limit-as 32 将进程的总内存量控制在32M
 -x  使用配置文件模式

# 13.启动Django服务的方法

runserver 方法是调试 Django 时经常用到的运行方式，它使用 Django 自带的
 WSGI Server 运行，主要在测试和开发中使用，并且 runserver 开启的方式也是单进程 。

# 14.python是强语言还是弱语言

## 1，Python语言的概述

1，用任何编程语言来开发程序，都是为了让计算机干活，比如下载一个MP3，编写一个文档等等，而计算机干活的CPU只认识机器指令，所以，尽管不同的编程语言差异极大，最后都得“翻译”成CPU可以执行的机器指令。而不同的编程语言，干同一个活，编写的代码量，差距也很大。
 比如，完成同一个任务，C语言要写1000行代码，Java只需要写100行，而Python可能只要20行。

3，用Python可以做什么？可以做日常任务，比如自动备份你的MP3；可以做网站，很多著名的网站包括YouTube就是Python写的；可以做网络游戏的后台，很多在线游戏的后台都是Python开发的。国内的话，豆瓣、知乎用python写的

4，Python当然也有不能干的事情，比如写操作系统，这个只能用C语言写；写手机应用，只能用Swift/Objective-C（针对iPhone）和Java（针对Android（Kotlin））;写3D游戏，最好用C或C++。

5，Python是一种解释型语言。这就是说，与C语言和C的衍生语言不同，Python代码在运行之前不需要编译。

6，Python是动态类型语言，指的是你在声明变量时，不需要说明变量的类型。你可以直接编写类似x=111和x="I'm a string"这样的代码，程序不会报错。

7，Python非常适合面向对象的编程（OOP），因为它支持通过组合（composition）与继承（inheritance）的方式定义类（class）。Python中没有访问说明符（access specifier，类似java中的public和private），这么设计的依据是“大家都是成年人了”。
 在Python语言中，函数是第一类对象（first-class objects）。这指的是它们可以被指定给变量，函数既能返回函数类型，也可以接受函数作为输入。类（class）也是第一类对象。

8，Python代码编写快，但是运行速度比编译语言通常要慢。好在Python允许加入基于C语言编写的扩展，因此我们能够优化代码，消除瓶颈，这点通常是可以实现的。numpy就是一个很好地例子，它的运行速度真的非常快，因为很多算术运算其实并不是通过Python实现的。

9，Python用途非常广泛——网络应用，自动化，科学建模，大数据应用，等等。它也常被用作“胶水语言”，帮助其他语言和组件改善运行状况。

## 2，强弱语言之分

·  动态类型语言：在运行期进行类型检查的语言，也就是在编写代码的时候可以不指定变量的数据类型，比如Python和Ruby

·  静态类型语言：它的数据类型是在编译期进行检查的，也就是说变量在使用前要声明变量的数据类型，这样的好处是把类型检查放在编译期，提前检查可能出现的类型错误，典型代表C/C++和Java

·  强类型语言，一个变量不经过强制转换，它永远是这个数据类型，不允许隐式的类型转换。举个例子：如果你定义了一个double类型变量a,不经过强制类型转换那么程序int b = a无法通过编译。典型代表是Java。

·  弱类型语言：它与强类型语言定义相反,允许编译器进行隐式的类型转换，典型代表C/C++。

### 简单的记忆如下：

弱类型：语言在运行时会隐式的做数据类型转换
 强类型：语言运行时确保不会发生未授意类型转换
 静态类型：编译期进行数据类型检查
 动态类型：运行期才做类型检查

# 15.python的垃圾回收机制

## 一、对象的引用计数机制

python内部使用引用计数，来保持追踪内存中的对象，所有对象都有引用计数。
 引用计数增加的情况：
 1，一个对象分配一个新名称
 2，将其放入一个容器中（如列表、元组或字典）
 引用计数减少的情况：
 1，使用del语句对对象别名显示的销毁
 2，引用超出作用域或被重新赋值
 sys.getrefcount( )函数可以获得对象的当前引用计数
 多数情况下，引用计数比你猜测得要大得多。对于不可变数据（如数字和字符串），解释器会在程序的不同部分共享内存，以便节约内存。

## 二、垃圾回收和分代收集

1，当一个对象的引用计数归零时，它将被垃圾收集机制处理掉。
 2，当两个对象a和b相互引用时，del语句可以减少a和b的引用计数，并销毁用于引用底层对象的名称。然而由于每个对象都包含一个对其他对象的应用，因此引用计数不会归零，对象也不会销毁。（从而导致内存泄露）。为解决这一问题，解释器会定期执行一个循环检测器，搜索不可访问循环的对象并删除它们。也就是分代收集技术（三代）。

## 三、内存池机制

Python的内存机制以金字塔行，-1，-2层主要由操作系统进行操作，
 　　第0层是C中的malloc，free等内存分配和释放函数进行操作；
 　　第1层和第2层是内存池，有Python的接口函数PyMem_Malloc函数实现，当对象小于256个字节时有该层直接分配内存；
 第3层是最上层，也就是我们对Python对象的直接操作；如整数，浮点数和List，都有其独立的私有内存池，对象间不共享他们的内存池。也就是说如果你分配又释放了大量的整数，用于缓存这些整数的内存就不能再分配给浮点数。

在 C 中如果频繁的调用 malloc 与 free 时,是会产生性能问题的.再加上频繁的分配与释放小块的内存会产生内存碎片.

Python 在这里主要干的工作有:
 如果请求分配的内存在-5~256字节之间就使用自己的内存管理系统,否则直接使用 malloc.
 　　这里还是会调用 malloc 分配内存,但每次会分配一块大小为256k的大块内存.
 　　经由内存池登记的内存到最后还是会回收到内存池,并不会调用 C 的 free 释放掉.以便下次使用.对于简单的Python对象，例如数值、字符串，元组（tuple不允许被更改)采用的是复制的方式(深拷贝)，也就是说当将另一个变量B赋值给变量A时，虽然A和B的内存空间仍然相同，但当A的值发生变化时，会重新给A分配空间，A和B的地址变得不再相同

# 16，赋值，浅拷贝，深拷贝的区别

赋值（=），就是创建了对象的一个新的引用，修改其中任意一个变量都会影响到另一个。

浅拷贝：创建一个新的对象，但它包含的是对原始对象中包含项的引用（如果用引用的方式修改其中一个对象，另外一个也会改变）{1,完全切片方法；2，工厂函数，如list()；3，copy模块的copy()函数}

深拷贝：创建一个新的对象，并且递归的复制它所包含的对象（修改其中一个，另外一个不会改变）{copy模块的deep.deepcopy()函数}

# 17，生成器和迭代器

Iterables（迭代器）
 当你创建了一个列表,你可以一个一个的读取它的每一项,这叫做iteration:

所有你可以用在for...in...语句中的都是可迭代的:比如lists,strings,files...因为这些可迭代的对象你可以随意的读取所以非常方便易用,但是你必须把它们的值放到内存里,当它们有很多值时就会消耗太多的内存.

Generators（生成器）
 生成器也是迭代器的一种,但是你只能迭代它们一次.原因很简单,因为它们不是全部存在内存里,它们只在要调用的时候在内存里生成:

生成器和迭代器的区别就是用()代替[],还有你不能用for i in mygenerator第二次调用生成器:首先计算0,然后会在内存里丢掉0去计算1,直到计算完4.

yield
 yield的用法和关键字return差不多
 要理解Yield你必须先理解当你调用函数的时候,函数里的代码并没有运行.函数仅仅返回生成器对象,这就是它最微妙的地方。
 然后呢,每当for语句迭代生成器的时候你的代码才会运转.

现在,到了最难的部分:
 当for语句第一次调用函数里返回的生成器对象,函数里的代码就开始运作,直到碰到yield,然后会返回本次循环的第一个返回值.所以下一次调用也将运行一次循环然后返回下一个值,直到没有值可以返回.一旦函数运行并没有碰到yeild语句就认为生成器已经为空了.原因有可能是循环结束或者没有满足if/else之类的.

yield 简单说来就是一个生成器，生成器是这样一个函数，它记住上一次返回时在函数体中的位置。对生成器函数的第二次（或第n 次）调用,跳转至该函数上次yield返回值的位置接着往下执行，而上次调用的所有局部变量都保持不变。

理解迭代的内部机制
 迭代是可迭代对象(对应**iter**()方法)和迭代器(对应**next**()方法)的一个过程.
 可迭代对象就是任何你可以迭代的对象.
 迭代器就是可以让你迭代可迭代对象的对象。

另外一种通俗的解释：
 （ 1）迭代器是一个更抽象的概念，对任何类如果它有 next
 方法和 iter 方法返回自己本身 。对于 string、list、dict、tuple
 等这类容器对象，使用 for 循环遍历是很方便的。在后台 for 语句对容器象调用 iter()函数， iter()是 python 的内置函数。
 iter()会返回一个定义 next()方法的迭代器对象，它在容器中逐个访问容器内元素， next()也是 python 的内置函数。在没有后续元素时，next()会 抛出一个 StopIter 异常

（ 2）生成器（ Generator）是创建迭代器的简单而强大工具。它们写起来就像是正规的函数，只在需要返回数据时候使用 yield 语句。每次 next()被调用，生成器会返回它脱离的位置，记忆语句最后一次执行和所有数据。

区别：生成器能做到迭代的所有事 ,而且因为自动创建了**iter**()和 next()方法 ,生成器显得特别简洁 ,而且生成器也是高效的 ，使用生成器表 达式取代列表解析式可以同时节省 内存。除了创建和保存程序状态的自动方法,当发生器终结时 ,还会自动抛出StopIteration 异常。

# 18，对不定长参数的理解。

用*args和**kwargs只是为了方便并没有强制使用它们. 当你不确定你的函数里将要传递多少参数时你可以用*args.例如,它可以传递任意数量的参数:
 相似的,**kwargs允许你使用没有事先定义的参数名:

你也可以混着用.命名参数首先获得参数值然后所有的其他参数都传递给*args和**kwargs.命名参数在列表的最前端.例如: def table_things(titlestring, kwargs) args和kwargs可以同时在函数的定义中,但是args必须在**kwargs前面. 当调用函数时你也可以用*和**语法.

就像你看到的一样,它可以传递列表(或者元组)的每一项并把它们解包.注意必须与它们在函数里的参数相吻合.当然,你也可以在函数定义或者函数调用时用*.

# 19,基础的数据结构有哪些？

集合、线性结构、树形结构、图状结构
 集合结构:除了同属于一种类型外，别无其它关系
 线性结构:元素之间存在一对一关系常见类型有: 数组,链表,队列,栈,它们之间在操作上有所区别.例如:链表可在任意位置插入或删除元素,而队列在队尾插入元素,队头删除元素,栈只能在栈顶进行插入,删除操作.
 树形结构:元素之间存在一对多关系,常见类型有:树(有许多特例:二叉树、平衡二叉树、查找树等)
 图形结构:元素之间存在多对多关系,图形结构中每个结点的前驱结点数和后续结点多个数可以任意

# 20,基本的算法有哪些，怎么评价一个算法的好坏？

①时间复杂度：同样的输入规模（问题规模）花费多少时间
 ②空间复杂度：同样的输入规模花费多少空间（主要是内存）
 以上两点越小越好
 ③稳定性：不会因为输入的不同而导致不稳定的情况发生
 ④算法思路是否简单：越简单越容易实现越好

# 21,如何查找并修正一条慢sql？

如何在mysql查找效率慢的SQL语句呢？这可能是困然很多人的一个问题，MySQL通过慢查询日志定位那些执行效率较低的SQL 语句，用--log-slow-queries[=file_name]选项启动时，mysqld 会写一个包含所有执行时间超过long_query_time 秒的SQL语句的日志文件，通过查看这个日志文件定位效率较低的SQL 。
 MySQL数据库有几个配置选项可以帮助我们及时捕获低效SQL语句

1，slow_query_log
 这个参数设置为ON，可以捕获执行时间超过一定数值的SQL语句。

2，long_query_time
 当SQL语句执行时间超过此数值时，就会被记录到日志中，建议设置为1或者更短。

3，slow_query_log_file
 记录日志的文件名。

4，log_queries_not_using_indexes
 这个参数设置为ON，可以捕获到所有未使用索引的SQL语句，尽管这个SQL语句有可能执行得挺快。

# 22,写一个邮箱地址的正则表达式和手机号码的正则表达式

## 邮箱：

^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9_-]+)+$

## 手机号：

^1[3|4|5|7|8][0-9]{9}$

# 23,找出二叉树中最远结点的距离？

```
class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        max_dia_left = self.diameterOfBinaryTree(root.left)
        max_dia_right = self.diameterOfBinaryTree(root.right)
        # max: 1.当前结点最大距离；2.左、右子结点的最大距离
        max_dia = max(self.get_depth(root.left) + self.get_depth(root.right), max_dia_left, max_dia_right)
        return max_dia

    # 计算以当前结点为根时，树的最大深度；
    def get_depth(self, root):
        if not root:
            return 0
        else:
            return max(1 + self.get_depth(root.left), 1 + self.get_depth(root.right))
```

# 24,写一个匿名函数，例如求两个数的和。

g = lambda x, y: x + y
 print(g(1, 2))

# 25,面向对象中的类方法和静态方法和实例方法

Python其实有3个方法,即静态方法(staticmethod),类方法(classmethod)和实例方法,如下:
 def foo(x):
 print "executing foo(%s)"%(x)

class A(object):
 def foo(self,x):
 print "executing foo(%s,%s)"%(self,x)

```
@classmethod
def class_foo(cls,x):
    print "executing class_foo(%s,%s)"%(cls,x)

@staticmethod
def static_foo(x):
    print "executing static_foo(%s)"%x
```

a=A()
 这个self和cls是对实例或者类的绑定,
 对于一般的函数来说我们可以这么调用foo(x),这个函数就是最常用的,它的工作跟任何东西(类,实例)无关.
 对于实例方法,我们知道在类里每次定义方法的时候都需要绑定这个实例,就是foo(self, x),为什么要这么做呢?因为实例方法的调用离不开实例,我们需要把实例自己传给函数,调用的时候是这样的a.foo(x)(其实是foo(a, x)).
 类方法一样,只不过它传递的是类而不是实例,A.class_foo(x).注意这里的self和cls可以替换别的参数,但是python的约定是这俩,还是不要改的好.
 对于静态方法其实和普通的方法一样,不需要对谁进行绑定,唯一的区别是调用的时候需要使用a.static_foo(x)或者A.static_foo(x)来调用.

|\      |实例方法  |类方法        |静态方法   |
 |a = A()  |a.foo(x)   |a.class_foo(x)   |a.static_foo(x)|
 |A      |不可用   |A.class_foo(x)   |A.static_foo(x)|

# 26,写一个列表生成式 例如产生一个公差为1的等差数列

li = [x for x in range(100)]
 print(li)

# 27,解释一下什么是锁，有哪几种锁

## 一、全局解释器锁（GIL）

1、什么是全局解释器锁
 　　　　　　在同一个进程中只要有一个线程获取了全局解释器（cpu）的使用权限，那么其他的线程就必须等待该线程的全局解释器（cpu）使用权消失后才能使用全局解释器（cpu）,即使多个线程直接不会相互影响，在同一个进程下也只有一个线程使用cpu，这样的机制称为全局解释器锁（GIL）。
 　　2、全局解释器锁的好处
 　　　　　　1、避免了大量的加锁解锁的好处
 　　　　　　2、使数据更加安全，解决多线程间的数据完整性和状态同步
 　　3、全局解释器的缺点
 　　　　　　多核处理器退化成单核处理器，只能并发不能并行。
 4、如图所示
 　
 看图可知：同一时刻的某个进程下的某个线程只能被一个cpu所处理，所以在GIL锁下的线程只能被并发，不能被并行。
 5，实例

```
import time
import threading
num = 100
li = []

def sub():
    global num  # 声明为全局变量
    num = num - 1
    time.sleep(2)

for i in range(100):  # 开100线程
    t = threading.Thread(target=sub, args=())
    t.start()
    li.append(t)

# 给每个线程都加上join，只要子线程都运行完后主线程才能运行
for i in li:
    print(i)
    i.join()

print(num)
```

由打印结果可知：当第一个线程拿到cpu后，其他线程只能等待，2秒后剩下的线程都并发执行

## 二、互斥锁（Lock）同步线程

1、什么是互斥锁？
 　　　　同一时刻的一个进程下的一个线程只能使用一个cpu，要确保这个线程下的程序在一段时间内被cpu执行，那么就要用到互斥锁同步线程。
 　　2、为什么用互斥锁锁？
 　　　　因为有可能当一个线程在使用cpu时，该线程下的程序可能会遇到io操作，那么cpu就会切到别的线程上去，这样就有可能会影响到该程序结果的完整性。
 　　3、怎么使用互斥锁？
 　　　　只需要在对公共数据的操作前后加上，上锁和释放锁的操作即可。

```
lock = threading.Lock()
lock.acquire()
dosomething……
lock.release()
```

4，实例

```
import time
import threading
num = 100
li = []
th = threading.Lock()

def sub():
    global num
    th.acquire()  # 加锁，相当于调用对象下的函数
    num1 = num
    time.sleep(1)
    num = num1 - 1
    th.release()
    time.sleep(2)

for i in range(100):  # 开100线程
    t = threading.Thread(target=sub, args=())
    t.start()
    li.append(t)

# 给每个线程都加上join，只要子线程都运行完后主线程才能运行
for i in li:
    print(i)
    i.join()

print(num)
```

由打印结果看出：100线程每隔1秒顺序的打印出来

5，额外知识：
 　　　　1、GIL的作用：多线程情况下必须存在资源的竞争，GIL是为了保证在解释器级别的线程唯一使用共享资源（cpu）。
 　　　　2、互斥锁的作用：为了保证解释器级别下的自己编写的程序唯一使用共享资源

## 三、递归锁(可重用锁RLock)和死锁

1、什么是死锁？
 　　　　指两个或两个以上的线程或进程在执行程序的过程中，因争夺资源而相互等待的一个现象，如图所示。

```
import threading
import time
class MyThread1(threading.Thread):
    def run(self):
        # 对mutexA上锁
        if mutexA.acquire():
            print(self.name + '----mutexA上锁----')
            time.sleep(1)

            if mutexB.acquire():
                print(self.name + '----mutexA中mutexB上锁----')
                mutexB.release()
            mutexA.release()


class MyThread2(threading.Thread):
    def run(self):
        # 对mutexB上锁
        if mutexB.acquire():
            print(self.name + '----mutexB上锁----')
            time.sleep(1)
            if mutexA.acquire():
                print(self.name + '----mutexB中mutexA上锁----')
                mutexA.release()
            mutexB.release()

mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# 死锁的结果如下： 
# Thread-1----mutexA上锁---- 
# Thread-2----mutexB上锁---- 
# 我手写的：一直停留在这里不动 
```

2、什么是递归锁？
 　　　　在Python中为了支持同一个线程中多次请求同一资源，Python提供了可重入锁。这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。直到一个线程所有的acquire都被release，其他的线程才能获
 得资源。

```
import threading
import time
class MyThread1(threading.Thread):
    def run(self):
        # 对mutexA上锁
        if mutex.acquire():
            print(self.name + '----mutexA上锁----')
            time.sleep(1)

            if mutex.acquire():
                print(self.name + '----mutexA中mutexB上锁----')
                mutex.release()
            mutex.release()


class MyThread2(threading.Thread):
    def run(self):
        # 对mutexB上锁
        if mutex.acquire():
            print(self.name + '----mutexB上锁----')
            time.sleep(1)
            if mutex.acquire():
                print(self.name + '----mutexB中mutexA上锁----')
                mutex.release()
            mutex.release()

mutex = threading.RLock()

if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # RLock递归锁的结果如下：
    # Thread-1----mutexA上锁----
    # Thread-1----mutexA中mutexB上锁----
    # Thread-2----mutexB上锁----
    # Thread-2----mutexB中mutexA上锁----
```

## 四、信号量

信号量：是指同时开几个线程并发。比如厕所有5个坑，那最多只允许5个人上厕所，后面的人只能等里面的5个人都出来了，才能再进去。

```
import threading, time


class myThread(threading.Thread):
    def run(self):
        # 加把锁，可以放进去多个（相当于5把锁，同时有5个线程）
        if semaphore.acquire():
            print(self.name)
            time.sleep(3)
            semaphore.release()

if __name__ == "__main__":
    # 同时能有几个线程进去（设置为5就是一次5个线程进去）
    semaphore = threading.Semaphore(5)

    thread_list = []  # 空列表
    for i in range(200):  # 200个线程
        thread_list.append(myThread())  # 加线程对象

    for t in thread_list:
        t.start()  # 分别启动
```

# 28,什么是僵尸进程和孤儿进程以及怎么避免僵尸进程

孤儿进程指的是在其父进程执行完成或被终止 后仍继续运行的一类进程。

在类UNIX系统中，僵尸进程是指完成执行（通过 exit 系统调用，或运行时发生致命错误或收到终止信号所致）但在操作系统的进程表中仍然有一个表项（进程控制块PCB），处于"终止状态 "的进程。

守护进程（英语：daemon，英语发音：/ˈdiːmən/或英语发音：/ˈdeɪmən/）是一種在后台执行的电脑程序。 此类程序会被以进程的形式初始化。 守护进程程序的名称通常以字母“d”结尾：例如，syslogd就是指管理系统日志的守护进程。

更详细的解释如下：
 1、一般情况下，子进程是由父进程创建，而子进程和父进程的退出是无顺序的，两者之间都不知道谁先退出。正常情况下父进程先结束会调用 wait 或者 waitpid 函数等待子进程完成再退出，而一旦父进程不等待直接退出，则剩下的子进程会被init(pid=1)进程接收，成会孤儿进程。（进程树中除了init都会有父进程）。
 2、如果子进程先退出了，父进程还未结束并且没有调用 wait 或者 waitpid 函数获取子进程的状态信息，则子进程残留的状态信息（ task_struct 结构和少量资源信息）会变成僵尸进程。
 3、守护进程（ daemon) 是指在后台运行，没有控制终端与之相连的进程。它独立于控制终端，通常周期性地执行某种任务 。 守护进程脱离于终端是为了避免进程在执行过程中的信息在任何终端上显示并且进程也不会被任何终端所产生的终端信息所打断 。

危害：
 孤儿进程结束后会被 init 进程善后，并没有危害，而僵尸进程则会一直占着进程号，操作系统的进程数量有限则会受影响。

解决：
 一般僵尸进程的产生都是因为父进程的原因，则可以通过 kill 父进程解决，这时候僵尸进程就变成了孤儿进程，被 init 进程接收

守护进程的编写：
 在不同Unix环境下，守护进程的具体编程细节并不一致。但所幸的是，守护进程的编程原则其实都一样，区别仅在于具体的实现细节不同，这个原则就是要满足守护进程的特性。

# 29,谈一下什么是解释性语言什么是编译性语言

简单一句话的意思就是：
 编译型语言要先编译再运行，而解释性语言直接“运行”源代码。

## 1.编译型语言和解释性语言

编译型语言：在执行之前需要一个专门的编译过程，把程序编译成为机器语言的文件，运行时不需要重新翻译，直接使用编译的结果就行了。程序执行效率高，依赖编译器，跨平台性差些。如C、C++、Delphi等
 解释性语言：源代码不是直接翻译成机器语言，而是先翻译成中间代码，再由解释器对中间代码进行解释运行。比如Python/JavaScript / Perl /Shell等都是解释型语言。所以运行速度相对于编译型语言要慢

## 2.python运行方式

Python解释器：运行Python的程序
 Python字节码：Python程序编译后的所得到的底层形式，Python自动将字节码保存为名为.pyc的文件。
 Python没有build和make的步骤，代码写好后立即运行。
 Python是解释型语言，运行的时候将程序翻译成机器语言，所以运行速度相对于编译型语言要慢其速度介于编译语言和解释语言之间）

## 3，python运行过程

录入的源码转换为字节码->字节码在PVM（Python虚拟机）中运行->代码自动被编译

# 30,谈一下http协议以及协议头部中表示数据类型的字段

Accept
 　　例子中的Accept字段是这样子的：Accept:text/html,a pplication/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8。意思是：浏览器支持的MIME类型分别是text/html、application/xhtml+xml、application/xml和*/*，优先顺序是它们从左到右的排列顺序。
 　　Accept表示浏览器支持的 MIME 类型；
 　　MIME的英文全称是 Multipurpose Internet Mail Extensions（多功能 Internet 邮件扩充服务），它是一种多用途网际邮件扩充协议，在1992年最早应用于电子邮件系统，但后来也应用到浏览器。
 　　text/html,application/xhtml+xml,application/xml 都是 MIME 类型，也可以称为媒体类型和内容类型，斜杠前面的是 type（类型），斜杠后面的是 subtype（子类型）；type 指定大的范围，subtype 是 type 中范围更明确的类型，即大类中的小类。
 　　Text：用于标准化地表示的文本信息，文本消息可以是多种字符集和或者多种格式的；
 　　text/html表示 html 文档；
 　　Application：用于传输应用程序数据或者二进制数据；
 　　application/xhtml+xml表示 xhtml 文档；
 application/xml表示 xml 文档。

Cache-Control
 　　Cache-Control指定请求和响应遵循的缓存机制。在请求消息或响应消息中设置Cache-Control并不会影响到另一个消息处理过程中的缓存处理过程。
 　　请求时的缓存指令包括：no-cache, no-store, max-age, max-stale, min-fresh, only-if-cached。
 　　响应消息中的指令包括：public, private, no-cache, no-store, no-transform, must-revalidate, proxy-revalidate, max-age。
 　　各个指令的含义：
 　　Public：指示响应可被任何缓存区缓存。

Private：指示对于单个用户的整个或部分响应消息，不能被共享缓存处理。这允许服务器仅仅描述当前用户的部分响应消息，此响应消息对于其他用户的请求无效。
 　　no-cache：指示请求或响应消息不能缓存
 　　no-store：用于防止重要的信息被无意的发布。在请求消息中发送将使得请求和响应消息都不使用缓存。
 　　max-age：指示客户机可以接收生存期不大于指定时间（以秒为单位）的响应。
 　　min-fresh：指示客户机可以接收响应时间小于当前时间加上指定时间的响应。
 　　max-stale：指示客户机可以接收超出超时期间的响应消息。如果指定max-stale消息的值，那么客户机可以接收超出超时期指定值之内的响应消息。

User-Agent
 　　User-Agent的值是：用户使用的客户端的一些必要信息，比如操作系统、浏览器及版本、浏览器渲染引擎等。

Transfer-Encoding
 transfer-encoding的可选值有：chunked,identity，从字面意义可以理解，前者指把要发送传输的数据切割成一系列的块数据传输，后者指传输时不做任何处理，自身的本质数据形式传输。举个例子，如果我们要传输一本“红楼梦”小说到服务器，chunked方式就会先把这本小说分成一章一章的，然后逐个章节上传，而identity方式则是从小说的第一个字按顺序传输到最后一个字结束。

# 31,浏览器发送一个请求到返回一个页面的具体过程

## 第一步，解析域名，找到IP

（1）浏览器会缓存DNS一段时间，一般2-30分钟不等。如果有缓存，直接返回IP，否则下一步。
 （2）缓存中无法找到IP，浏览器会进行一个系统调用，查询hosts文件。如果找到，直接返回IP，否则下一步。（在计算机本地目录etc下有一个hosts文件，hosts文件中保存有域名与IP的对应解析，通常也可以修改hosts科学上网或破解软件。）
 （3）进行了（1）（2）本地查询无果，只能借助于网络。路由器一般都会有自己的DNS缓存，ISP服务商DNS缓存，这时一般都能够得到相应的IP。如果还是无果，只能借助于DNS递归解析了。
 （4）这时，ISP的DNS服务器就会开始从根域名服务器开始递归搜索，从.com顶级域名服务器，到baidu的域名服务器。

到这里，浏览器就获得了IP。在DNS解析过程中，常常会解析出不同的IP。比如，电信的是一个IP，网通的是另一个IP。这是采取了智能DNS的结果， 降低运营商间访问延时，在多个运营商设置主机房，就近访问主机。电信用户返回电信主机IP，网通用户返回网通主机IP。当然，劫持DNS，也可以屏蔽掉一 部分网点的访问，某防火长城也加入了这一特性。

## 第二步，浏览器与网站建立TCP连接

浏览器利用IP直接与网站主机通信。浏览器发出TCP（SYN标志位为1）连接请求，主机返回TCP（SYN，ACK标志位均为1）应答报文，浏览器收到 应答报文发现ACK标志位为1，表示连接请求确认。浏览器返回TCP（）确认报文，主机收到确认报文，三次握手，TCP链接建立完成。

## 第三步，浏览器发起默认的GET请求

浏览器向主机发起一个HTTP-GET方法报文请求。请求中包含访问的URL，也就是[http://www.baidu.com/](https://link.jianshu.com?t=http://www.baidu.com/) ，还有User-Agent用户浏览器操作系统信息，编码等。值得一提的是Accep-Encoding和Cookies项。Accept- Encoding一般采用gzip，压缩之后传输html文件。Cookies如果是首次访问，会提示服务器建立用户缓存信息，如果不是，可以利用 Cookies对应键值，找到相应缓存，缓存里面存放着用户名，密码和一些用户设置项。

## 第四步，显示页面或返回其他

返回状态码200 OK，表示服务器可以相应请求，返回报文，由于在报头中Content-type为“text/html”，浏览器以HTML形式呈现，而不是下载文件。

但是，对于大型网站存在多个主机站点，往往不会直接返回请求页面，而是重定向。返回的状态码就不是200 OK，而是301,302以3开头的重定向码，浏览器在获取了重定向响应后，在响应报文中Location项找到重定向地址，浏览器重新第一步访问即可。
 补充一点的就是，重定向是为了负载均衡或者导入流量，提高SEO排名。利用一个前端服务器接受请求，然后负载到不同的主机上，可以大大提高站点的业务并发 处理能力；重定向也可将多个域名的访问，集中到一个站点；由于[baidu.com](https://link.jianshu.com?t=http://baidu.com)，[www.baidu.com](https://link.jianshu.com?t=http://www.baidu.com)会被搜索引擎认为是两个网站，照成每个的链 接数都会减少从而降低排名，永久重定向会将两个地址关联起来，搜索引擎会认为是同一个网站，从而提高排名。

## 与python结合的过程

### 1、先从网络模型层面：

client （浏览器）与 server 通过 http 协议通讯，http 协议属于应用层协议，http 基于 tcp 协议，所以 client 与 server 主要通过 socket 进行通讯；
 而 tcp 属于传输层协议、如果走 https 还需要会话层 TLS、SSL 等协议；
 传输层之下网络层，这里主要是路由协议 OSPF 等进行路由转发之类的。
 再向下数据链路层主要是 ARP、RARP 协议完成 IP 和 Mac 地址互解析，再向下到最底层物理层基本就是 IEEE 802.X 等协议进行数据比特流转成高低电平的的一些定义等等；
 当浏览器发出请求，首先进行数据封包，然后数据链路层解析 IP 与 mac 地址的映射，然后上层网路层进行路由查表路由，通过应用层 DNS 协议得到目标地址对应的 IP ，在这里进行 n 跳的路由寻路；而传输层 tcp 协议可以说下比较经典的三次握手、四次分手的过程和状态机，这里放个图可以作为参考：

### 2、应用层方面：

数据交换主要通过 http 协议， http 协议是无状态协议，这里可以谈一谈 post、get 的区别以及 RESTFul 接口设计，然后可以讲服务器 server 模型 epoll、select 等，接着可以根据实际经验讲下 server 处理流程，
 比如我： server 这边 Nginx 拿到请求，进行一些验证，比如黑名单拦截之类的，然后 Nginx 直接处理静态资源请求，其他请求 Nginx 转发给后端服务器，这里我用 uWSGI, 他们之间通过 uwsgi 协议通讯，uWSGI 拿到请求，可以进行一些逻辑， 验证黑名单、判断爬虫等，根据 wsgi 标准，把拿到的 environs 参数扔给 Django ，Django 根据 wsgi 标准接收请求和 env， 然后开始 start_response ，先跑 Django 相关后台逻辑，Django 拿到请求执行 request middleware 内的相关逻辑，然后路由到相应 view 执行逻辑，出错执行 exception middleware 相关逻辑，接着 response 前执行 response middleware 逻辑，最后通过 wsgi 标准构造 response， 拿到需要返回的东西，设置一些 headers，或者 cookies 之类的，最后 finish_response 返回，再通过 uWSGI 给 Nginx ，Nginx 返回给浏览器。



作者：晓可加油

链接：https://www.jianshu.com/p/1f8df5d3c066

來源：简书

简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。