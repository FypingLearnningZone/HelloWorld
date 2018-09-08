Q:中间件是什么?

A:中间件是django 请求响应/处理的钩子框架,用于全局的改变django的输入输出



Q:如何使用

A:

```
中间件可以被写成这样的函数：

def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
或者它可以写成一个类，它的实例是可调用的，如下：

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

```



## 激活中间件[¶](https://docs.djangoproject.com/zh-hans/2.1/topics/http/middleware/#activating-middleware)

若要激活中间件组件，请将其添加到 Django 设置中的 [`MIDDLEWARE`](https://docs.djangoproject.com/zh-hans/2.1/ref/settings/#std:setting-MIDDLEWARE) 列表中。

在 [`MIDDLEWARE`](https://docs.djangoproject.com/zh-hans/2.1/ref/settings/#std:setting-MIDDLEWARE) 中，每个中间件组件由字符串表示：指向中间件工厂的类或函数名的完整 Python 路径。例如，这里创建的默认值是 [`django-admin startproject`](https://docs.djangoproject.com/zh-hans/2.1/ref/django-admin/#django-admin-startproject)：

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Django 安装不需要任何中间件——如果您愿意的话，[`MIDDLEWARE`](https://docs.djangoproject.com/zh-hans/2.1/ref/settings/#std:setting-MIDDLEWARE) 可以为空——但是强烈建议您至少使用 [`CommonMiddleware`](https://docs.djangoproject.com/zh-hans/2.1/ref/middleware/#django.middleware.common.CommonMiddleware)。

[`MIDDLEWARE`](https://docs.djangoproject.com/zh-hans/2.1/ref/settings/#std:setting-MIDDLEWARE) 的顺序很重要，因为中间件会依赖其他中间件。例如：类 [`AuthenticationMiddleware`](https://docs.djangoproject.com/zh-hans/2.1/ref/middleware/#django.contrib.auth.middleware.AuthenticationMiddleware) 在会话中存储经过身份验证的用户；因此，它必须在 [`SessionMiddleware`](https://docs.djangoproject.com/zh-hans/2.1/ref/middleware/#django.contrib.sessions.middleware.SessionMiddleware) 后面运行 。中间件。Session中间件。请参阅 [Middleware ordering](https://docs.djangoproject.com/zh-hans/2.1/ref/middleware/#middleware-ordering) ，用于一些关于 Django 中间件类排序的常见提示。

###### Reference

- https://docs.djangoproject.com/zh-hans/2.1/topics/http/middleware/