#### xinje命名 方式

接口位置 http://www.xinje.net:904/view/pc/indexpc.aspx?action=get_a_device_a_view&device_ID=xxx&view_name=xxx

| 前缀                                   | 解释                              | 例子                            |
| -------------------------------------- | --------------------------------- | --------------------------------- |
| get_sensor_type_传感器             | 传感器字段                        | get_sensor_温度 _温度1 |
| control_mod_name_控制模式              | 控制模式                          | control_mod_name_自动模式   |
| 自动模式 _ option_name _ 自动模式 选项 | 自动模式 选项 溶氧 光照 温度 湿度 | 自动模式 _ option_name _ 温度 |
| 自动模式 选项_up_mark _实例            | 自动 上限                         | 温度_up_mark _内遮阳 |
| 自动模式 选项_down_mark _实例          | 自动 下限                         |                          |
| 自动模式 选项_float_mark _实例         | 自动 浮动值                       |                        |
| 定时模式  _hb _mark _ 实例       | 时 开始                           | 定时模式  _hb _mark _ 内遮阳    |
| 定时模式_he_mark _实例                 | 时 结束                           |                            |
| 定时模式_mb_mark _实例               | 分 开始                           |                            |
| 定时模式_me_mark _实例               | 分 结束                           |                            |
| 手动模式_on_mark _实例                | 手动模式 开                       | 手动模式_on_mark _内遮阳    |
| 手动模式_off_mark _实例               | 手动模式 关                       |                        |
| 手动模式_onandoff_mark _实例          | 手动模式 开关同一个继电器         | 手动模式_onandoff_mark _内遮阳 |



#### ~~rs命名方式~~

接口位置 

~~2.5 获取设备继电器 状态接口~~
~~2.2获取设备信息及实时数据接口~~

| ~~前缀~~                         | ~~解释~~                      | ~~例子~~                           |
| -------------------------------- | ----------------------------- | ---------------------------------- |
| ~~get_sensor_type_传感器~~       | ~~传感器字段~~                | ~~get_sensor_温度 _温度1~~         |
| ~~手动模式_on_mark _实例~~       | ~~手动模式 开~~               | ~~手动模式_on_mark _内遮阳~~       |
| ~~手动模式_off_mark _实例~~      | ~~手动模式 关~~               |                                    |
| ~~手动模式_onandoff_mark _实例~~ | ~~手动模式 开关同一个继电器~~ | ~~手动模式_onandoff_mark _内遮阳~~ |



##### 命名规范

1. 采用 前缀+字段

2. 前缀 采用 动词+名词+注释

3. 英文部分为框架,汉字部分为自定义


| 种类          | 解释                                                         |
| ------------- | ------------------------------------------------------------ |
| 实例          | 控制实例 名称不可重复                                        |
| 传感器        | 温度,湿度,光照,风向 名称不可重复                             |
| 控制模式      | 自动模式,手动模式,定时模式 名称不可重复                      |
| 自动模式 选项 | 溶氧 光照 温度 湿度   选项名称为 本设备所有传感器类型 集合 不可重复 |
| 定时模式      | 控制实例 时 开始, 时 结束, 分 开始 ,分 结束 名称不可重复     |
| 手动模式      | 控制实例有两种可能 1.一个实例拥有两个继电器,2.一个实例拥有一个继电器 名称不可重复 |
|               |                                                              |


#### 前端控制逻辑

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



#### 数据抓取逻辑

获取内容

1. 所有设备 (即含有传感器,继电器的上一层级的字段)在当前平台主账号下的树中的路径
2. 相关设备的 传感器的路径 继电器的路径
3. 设备的经纬度
4. 传感器的实时数据 固定时间间隔 入库



```python
数据抓取架构逻辑
1.数据第一次获取
2.接口中设备被删除,但数据库中的记录未删除  数据同步问题
数据同步

删除后对应其他表

为减少数据库的查询和复杂度可以一次把某一个平台 或是某一个设备的所有 相关数据都放到一种字典中

{"real_device":123,
 "real_sensor_list":[],
 "real_relay_list":[],
 "auto_option_list":[]} 
传感器
继电器 控制实例
设备 删除后对应其他表 摄像头
分组 路径里的每一级 都需要 数据同步 不变 更新 删除

需要更新的东西 路径 以及结构


def get_xinje_data():
    '''
    '''
    登录用户,获取json
    遍历树获取设备路径
    获取设备下的 传感器 路径 继电器路径
    根据字符串匹配 自动生成 控制模式名 控制选项名 控制实例名 及各个名称要绑定的继电器
    获取get_sensor_type_传感器字段中的type
    
    
    
    
def get_rs_data():
    登录用户,获取json
    遍历树获取设备路径
    获取设备下的 传感器 路径 继电器路径
    生成的控制实例 对应一个继电器
    

while:
    get_xinje_data()
    get_rs_data()
    sleep(time)
    

    
def get_xinje_history():
    登录用户,获取json
    取出数据库中所有xinje平台的传感器
    根据传感器的路径获取json对应位置的数据

def get_rs_history():
    登录用户,获取json
    取出数据库中所有rs平台的传感器
    根据传感器的路径获取json对应位置的数据
    
    
while:
    get_xinje_history()
    get_rs_history()
    写入数据时跟传感器上下限对比是否报警,确定写入的记录是是否是报警记录
    sleep()
    
    
1.平台的统一性
2.可扩展性
3.可维护性
4.安全性
	
```



#### 后台推送逻辑

```python
1.使用的常量使用配置文件记录 或是在数据库中记录
2.确定推送的循环 
  是单线程(所有的报警间隔都是相同) 
  还是多线程(根据用户配置的值为用户自定义不同的线程时间)

thread_1

def get_wechat_token()
    wechat_token = get_token()
    
while:
    get_wechat_token()
    #微信 access_token的有效期目前为2个小时
    sleep(1.9*60*60)
    
thread_2

#推送有app 个推推送 ,微信推送。失败邮件报警

def app_push(user_id):
    app 个推推送
    
def wechat_push(user_id):
    微信推送

def msg_push(device_id):
    短信推送
    
def mail_push():
    失败邮件报警
    1.报警推送失败
    2.定时控制失败
    
    邮件失败 写入日志
    
def check_xinje_sensor():
    检查xinje平台的传感器是否报警
    if 报警:
        if user_id报警总开关:
            if app推送开启:
                app_push()
            if 微信推送开启:
                wechat_push()
        if 短信报警开启：
        	msg_push(device_id）
            
def check_rs_sensor():
    检查rs平台的传感器是否报警
    
while:
    check_xinje_sensor()
    check_rs_sensor()
    
    


```



#### 后续平台接入

```
1.添加数据抓取逻辑
2.数据推送逻辑

尽量 总平台与分平台 逻辑解耦合
```



















