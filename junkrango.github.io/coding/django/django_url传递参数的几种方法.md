---
title: django_url传递参数的几种方法
date: 2018/7/25 12:12:12
---



**通过传统的”?”传递参数**

url : http://127.0.0.1:8000/plist/?p1=china&p2=japan

url.py

```python
(r'^plist/$', func）
```
view.py
```python
def func(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    return HttpResponse("p1 = " + p1 + "; p2 = " + p2)
```

在view中使用request.GET.get(),来获取参数值



url.py

```python
("<int:a>/<int:b>/",view.home,name="home")
```

view.py

```python
def show(request,a,b):
    num =str(a)
    num2 = str(b)
    return HttpResponse( num2 + num)
```

