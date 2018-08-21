class A(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        # 判断__instance是否有None
        if cls.instance is None:
            # 若为None，则new一个对象写入到该变量
            cls.instance = object.__new__(cls, *args, **kwargs)

        # 返回该变量中的对象
        return cls.instance


a = A()
a.value = 2

b = A()
print(b.value)

print(a is b)
print(A.instance)