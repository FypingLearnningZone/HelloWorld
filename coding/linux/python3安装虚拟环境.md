### 创建虚拟环境

在当前目录创建虚拟环境：

```
$ python -m venv dir
```

下面是"venv"的详细使用参数:

```
usage: venv [-h] [--system-site-packages] [--symlinks] [--clear]
            [--upgrade] [--without-pip] ENV_DIR [ENV_DIR ...]

Creates virtual Python environments in one or more target directories.

positional arguments:
  ENV_DIR             A directory to create the environment in.

optional arguments:
  -h, --help             show this help message and exit
  --system-site-packages Give access to the global site-packages dir to the
                         virtual environment.
  --symlinks             Try to use symlinks rather than copies, when symlinks
                         are not the default for the platform.
  --copies               Try to use copies rather than symlinks, even when
                         symlinks are the default for the platform.
  --clear                Delete the environment directory if it already exists.
                         If not specified and the directory exists, an error is
                         raised.
  --upgrade              Upgrade the environment directory to use this version
                         of Python, assuming Python has been upgraded in-place.
  --without-pip          Skips installing or upgrading pip in the virtual
                         environment (pip is bootstrapped by default)
```

### 激活虚拟环境

在Posix标准平台下：

```
$ source <venv>/bin/activate
```

在Windows cmd下：

```
C:> <venv>/Scripts/activate.bat
```

在Windows PowerShell下：

```
PS C:> <venv>/Scripts/Activate.ps1
```

 

 

 

 

 