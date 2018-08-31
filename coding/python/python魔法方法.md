```
__eq__(self, other) 定义了等号的行为, == 

__ne__(self, other) 定义了不等号的行为, != 

__lt__(self, other) 定义了小于号的行为， < 

__gt__(self, other) 定义了大于等于号的行为， >= 

__str__(self) 定义当 str() 调用的时候的返回值 
__repr__(self) 定义 repr() 被调用的时候的返回值
__unicode__(self) 定义当 unicode() 调用的时候的返回值
unicode() 和 str() 很相似，但是返回的是unicode字符串
__hash__(self) 定义当 hash() 调用的时候的返回值，它返回一个整形，用来在字典中进行快速比较 __nonzero__(self) 定义当 bool() 调用的时候的返回值。本方法应该返回True或者False，取决于你想让它返回的值。
当一个内存对象的引用计数降为0，即没有被变量引用时，解释器的垃圾回收机制才会回收这块内存。只有当内存被真正回收时，__del__方法才会被调用
__getattr__(self, name): 访问不存在的属性时调用

__getattribute__(self, name)：访问存在的属性时调用（先调用该方法，查看是否存在该属性，若不存在，接着去调用①）

__setattr__(self, name, value)：设置实例对象的一个新的属性时调用

__delattr__(self, name)：删除一个实例对象的属性时调用
```

