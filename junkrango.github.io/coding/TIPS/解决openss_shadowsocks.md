title: 解决openss_shadowsocks
date: 2018/1/1 12:12:12
---
##### 解决openssl升级到1.1.0以上版本，导致shadowsocks2.8.2启动报undefined symbol: EVP_CIPHER_CTX_cleanup错误

最近将openssl升级到了1.1.0b版本，编译之后shadowsocks无法启动，报错如下：

```python
Traceback (most recent call last):
  File "/usr/bin/ssserver", line 9, in 
    load_entry_point('shadowsocks==2.8.2', 'console_scripts', 'ssserver')()
  File "/usr/lib/python2.7/site-packages/shadowsocks/server.py", line 34, in main
    config = shell.get_config(False)
  File "/usr/lib/python2.7/site-packages/shadowsocks/shell.py", line 262, in get_config
    check_config(config, is_local)
  File "/usr/lib/python2.7/site-packages/shadowsocks/shell.py", line 124, in check_config
    encrypt.try_cipher(config['password'], config['method'])
  File "/usr/lib/python2.7/site-packages/shadowsocks/encrypt.py", line 44, in try_cipher
    Encryptor(key, method)
  File "/usr/lib/python2.7/site-packages/shadowsocks/encrypt.py", line 83, in __init__
    random_string(self._method_info[1]))
  File "/usr/lib/python2.7/site-packages/shadowsocks/encrypt.py", line 109, in get_cipher
    return m[2](method, key, iv, op)
  File "/usr/lib/python2.7/site-packages/shadowsocks/crypto/openssl.py", line 76, in __init__
    load_openssl()
  File "/usr/lib/python2.7/site-packages/shadowsocks/crypto/openssl.py", line 52, in load_openssl
    libcrypto.EVP_CIPHER_CTX_cleanup.argtypes = (c_void_p,)
  File "/usr/lib64/python2.7/ctypes/__init__.py", line 373, in __getattr__
    func = self.__getitem__(name)
  File "/usr/lib64/python2.7/ctypes/__init__.py", line 378, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: /usr/local/ssl/lib/libcrypto.so.1.1: undefined symbol: EVP_CIPHER_CTX_cleanup
shadowsocks start failed
```

这个问题是由于在openssl1.1.0版本中，废弃了EVP_CIPHER_CTX_cleanup函数，如[官网](https://www.openssl.org/docs/man1.1.0/crypto/EVP_EncryptInit.html#HISTORY)中所说：

> EVP_CIPHER_CTX was made opaque in OpenSSL 1.1.0. As a result, EVP_CIPHER_CTX_reset() appeared and EVP_CIPHER_CTX_cleanup() disappeared. EVP_CIPHER_CTX_init() remains as an alias for EVP_CIPHER_CTX_reset().

EVP_CIPHER_CTX_reset函数替代了EVP_CIPHER_CTX_cleanup函数 EVP_CIPHER_CTX_reset函数说明：

> EVP_CIPHER_CTX_reset() clears all information from a cipher context and free up any allocated memory associate with it, except the ctx itself. This function should be called anytime ctx is to be reused for another EVP_CipherInit() / EVP_CipherUpdate() / EVP_CipherFinal() series of calls.

EVP_CIPHER_CTX_cleanup函数说明：

> EVP_CIPHER_CTX_cleanup() clears all information from a cipher context and free up any allocated memory associate with it. It should be called after all operations using a cipher are complete so sensitive information does not remain in memory.

可以看出，二者功能基本上相同，都是释放内存，只是应该调用的时机稍有不同，所以用reset代替cleanup问题不大。



1. 用vi打开文件：`vi /usr/lib/python2.7/site-packages/shadowsocks/crypto/openssl.py`
2. 跳转到52行（shadowsocks2.8.2版本，其他版本搜索一下cleanup）
3. 进入编辑模式
4. 将第52行libcrypto.EVP_CIPHER_CTX_cleanup.argtypes = (c_void_p,)
   改为libcrypto.EVP_CIPHER_CTX_reset.argtypes = (c_void_p,)
5. 再次搜索cleanup（全文件共2处，此处位于111行），将libcrypto.EVP_CIPHER_CTX_cleanup(self._ctx)
   改为libcrypto.EVP_CIPHER_CTX_reset(self._ctx)
6. 保存并推出
7. 启动shadowsocks服务：`service shadowsocks start`

之后我们就可以继续愉快的、科学的畅游互联网了。
提示：openssl1.1.0目前兼容性很不好，大部分的软件都不支持
目前支持的有nginx-1.11.5、curl-7.50.3
不支持的有PHP-7.0.12、openssh-7.3p1
所以如果决定使用openssl1.1.0需要考虑很多兼容问题，必须保留1.0.2或1.0.1(不推荐，存在一些已知漏洞，最重要的是如果服务器要开http2，由于新版chrome必须使用ALPN的限制，只有1.0.2版本支持ALPN，所以必须升级到1.0.2)版本以便编译其他程序。



> https://blog.lyz810.com/article/2016/09/shadowsocks-with-openssl-greater-than-110/