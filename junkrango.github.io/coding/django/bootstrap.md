影响元素之间的间距是可以通过style的margin或padding属性来实现，但这两个属性本意并不相同；margin影响的是本元素与相邻外界元素之间的距离，这里简称外边距；padding影响的元素本身与其内部子元素之间的距离，简称为内填充。

bootstrap4提供了简写的class名，名称分别以m-开头和p-开头的类。

一、影响距离大小的值有

0,1,2,3,4,5,auto

(1)、margin值有

| class名 | 等价的style                       |
| ------- | --------------------------------- |
| m-0     | 等价于{margin:0 !important}       |
| m-1     | 等价于{margin:0.25rem !important} |
| m-2     | 等价于{margin:0.5rem !important}  |
| m-3     | 等价于{margin:1rem !important}    |
| m-4     | 等价于{margin:1.5rem !important}  |
| m-5     | 等价于{margin:3rem !important}    |
| m-auto  | 等价于{margin:auto !important}    |

(2)、padding值有

 

| class名 | 等价的style                        |
| ------- | ---------------------------------- |
| p-0     | 等价于{padding:0 !important}       |
| p-1     | 等价于{padding:0.25rem !important} |
| p-2     | 等价于{padding:0.5rem !important}  |
| p-3     | 等价于{padding:1rem !important}    |
| p-4     | 等价于{padding:1.5rem !important}  |
| p-5     | 等价于{padding:3rem !important}    |
| p-auto  | 等价于{padding:auto !important}    |

二、调整某一侧的边距

有几个缩写,t,b,l,r,x,y含义分别是top,bottom,left,right,left和right,top和bottom

（1）、margin例子，距离大小可以0-5与auto,这里只用期中一个值来说明含义

 

| class名 | 等价的style                                                  |
| ------- | ------------------------------------------------------------ |
| mt-2    | {margin-top: 0.5rem !important}                              |
| mb-2    | {margin-bottom: 0.5rem !important}                           |
| ml-2    | {margin-left: 0.5rem !important}                             |
| mr-2    | {margin-right: 0.5rem !important}                            |
| mx-2    | {margin-right: 0.5rem !important;margin-left: 0.5rem !important} |
| my-2    | {margin-top: 0.5rem !important;margin-bottom: 0.5rem !important} |

(2)padding例子

| class名 | 等价的style                                                  |
| ------- | ------------------------------------------------------------ |
| pt-2    | {padding-top: 0.5rem !important}                             |
| pb-2    | {padding-bottom: 0.5rem !important}                          |
| pl-2    | {padding-left: 0.5rem !important}                            |
| pr-2    | {padding-right: 0.5rem !important}                           |
| px-2    | {padding-right: 0.5rem !important;margin-left: 0.5rem !important} |
| py-2    | {padding-top: 0.5rem !important;margin-bottom: 0.5rem !important} |

 

参考地址：  [ https://v4.bootcss.com/docs/4.0/utilities/spacing/](https://v4.bootcss.com/docs/4.0/utilities/spacing/)