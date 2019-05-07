class cat_(object):
    def __init__(self):
        self.a = 1
        self.b = 2
        
    def sub(self):
        return self.a+self.b

an = cat_()
b = an.sub()
print(b)


class animal(object):
    def __init__(self):
        self.c = 4
        self.b = 5

    def sub(self):
        return cat_().sub()
d = animal()
print(d.sub())

class dog(object):
    def __init__(self):
        self.a = 1

    def __enter__(self):
        self.num = 12
        return num

    def __exit__(self, exc_ty, exc_val, tb):
        self.a = 1

with dog as num:
    print(num)