### Python遍历文件夹

##### 递归深度优先

```python
import os
def gci(filepath):
#遍历filepath下所有文件，包括子目录  
    files = os.listdir(filepath)  
    for fi in files:    
        fi_d = os.path.join(filepath,fi)    
        if os.path.isdir(fi_d):
            print(os.path.join(filepath, fi_d))
            gci(fi_d)    
        else:      
            print(os.path.join(filepath,fi_d))#递归遍历/root目录下所有文件
gci('f:\\test')
```

##### 递归广度优先

```python
import os.path
rootdir = 'f:\\test'                                   # 指明被遍历的文件夹
def gci(rootdir):
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for dirname in  dirnames:                       #输出文件夹信息
            #print("parent is:" + parent)
            #print("dirname is:" + dirname)
            #print("the full name of the file is:" + os.path.join(parent, dirname))  # 输出文件夹路径信息
            print(os.path.join(parent, dirname))  # 输出文件夹路径信息

        for filename in filenames:  # 输出文件信息
            #print("parent is:" + parent)
            #print("filename is:" + filename)
            #print("the full name of the file is:" + os.path.join(parent, filename))  # 输出文件路径信息
            print(os.path.join(parent, filename))  # 输出文件路径信息
gci(rootdir)
```





