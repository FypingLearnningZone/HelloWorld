| 前缀                                   | 解释                              |
| -------------------------------------- | --------------------------------- |
| get_sensor_name_传感器                 | 传感器字段                        |
| control_mod_name_控制模式              | 控制模式                          |
| 自动模式 _ option_name _ 自动模式 选项 | 自动模式 选项 溶氧 光照 温度 湿度 |
| 自动模式 选项_up_mark _name            | 自动 上限                         |
| 自动模式 选项_down_mark _name          | 自动 下限                         |
| 自动模式 选项_float_mark _name         | 自动 浮动值                       |
| 定时模式_hb_mark_name                  | 时 开始                           |
| 定时模式_he_mark_name                  | 时 结束                           |
| 定时模式_mb_mark_name                  | 分 开始                           |
| 定时模式_me_mark_name                  | 分 结束                           |
| 手动模式_on_mark_name                  | 手动模式 开                       |
| 手动模式_off_mark_name                 | 手动模式 关                       |
| 手动模式_onandoff_mark_name            | 手动模式 开关同一个继电器         |

##### 命名规范

1. 采用 前缀+name
2. 前缀 采用 动词+名词+注释

| 种类                    | 解释                                                         |
| ----------------------- | ------------------------------------------------------------ |
| name                    | 控制实例                                                     |
| 传感器                  | 温度,湿度,光照,风向                                          |
| 控制模式                | 自动模式,手动模式,定时模式                                   |
| 控制选项                | 溶氧 光照 温度 湿度                                          |
| 自动 光照 温度 湿度溶氧 | 每个控制实例都有 上限下限浮动值                              |
| 定时模式                | 每个控制实例都有 时 开始, 时 结束, 分 开始 ,分 结束          |
| 手动模式                | 控制实例有两种可能 1.一个实例拥有两个继电器,2.一个实例拥有一个继电器 |
|                         |                                                              |

```python
click 控制界面
for i in database:
    取出所有 匹配为 control_mod_name_控制模式 的字段,取出控制模式得到控制模式的列表
    
click 模式
for i in database:
    if 模式 == 自动模式：
        取出所有 匹配为 自动模式 _ option_name_自动模式选项 取出所有 自动模式选项 的列表
        if == 自动模式 选项:
            取出所有 匹配为 自动模式 选项_up_mark _name 取出所有 name 的列表
            [{"name":{"up":"自动模式 选项_up_mark _name"}...}]
    if 模式 == 手动模式:
        取出所有 匹配为 手动模式_on_mark_name 取出所有 name 的列表
        if 匹配 手动模式_on_mark_name && 手动模式_off_mark_name
           [{"name":{"on":"手动模式_on_mark_name","off":"手动模式_off_mark_name"}}]
        elif 
           [{"name":{"on":"手动模式_onandoff_mark_name","off":"手动模式_onandoff_mark_name"}}]
            
    if 模式 == 定时模式:
        取出所有 匹配为 定时模式_hb_mark_name 取出所有 name 的列表
        [{"name":{"hb":"定时模式_hb_mark_name"}...}]
```



自动点击广告

代理软件























