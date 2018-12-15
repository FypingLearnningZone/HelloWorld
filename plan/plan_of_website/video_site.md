
V1

### models

1. video
  - src
  - title
  - excerpt
  - views_time
  - created time
  - modified time
  - category
  - tag
2. tag
  - name
3. categorys
  - name
4. user
### views
1. home
	- tag
	- search
	- categorys
	- video
2. detail
	- video
	- more_video
	- talks
	- download
	-
3. download
	- ads
	- 验证 图片 人机
### 抓取
1. 全自动
2. 分布式
3. 多线程
4. 异步
5. 按时检测链接有效性



> 核心竞争力 客户为什么会用你的 而不去用其他的

V2

apps

- video
  - 名称
  - 描述
  - 详情
  - 作者
  - 演员
  - video_url
  - 下载链接 bt 云盘
  - image_url
  - 评论
  - 种类
  - 添加时间
- actor
    - 演员
      - 名称
      - 描述
      - 演过的影片
    - 导演
      - 名称
      - 描述
      - 演过的影片
- users

  - 用户信息 user_profile
    - 名称
    - 性别
    - 地址
    - 邮箱
    - 电话
    - 头像
    - ip
    - 位置
    - 使用设备
  - EmailVerifyRecord

    - 验证码

    - 邮箱

    - 时间
  - Banner
    - 轮播图
- operation
    - 评论 video_comments
      - 用户
      - 影片
      - 添加时间
      - 评论
    - 用户收藏 user_favorite
    	- 用户
    	- 数据id
    	- 收藏类型
    	- 添加时间
    - 用户消息 user_message
    	- 接受用户
    	- 消息内容
    	- 是否已读
    	- 添加时间
