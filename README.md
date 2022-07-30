### 项目说明
- 使用python-wechaty开发的可以查询油价&联动notion的微信机器人demo
- 建议先看[B站视频教程](https://www.bilibili.com/video/BV1r94y1D7d4)在尝鲜代码

### 项目初始化说明
- pip install -r requirement.txt
- vars/personal_vars.py 填入puppet_token
- vars/public_vars.py 填入notion_secret_token和database_id (如果不联动notion此项可不做)
- 在本机8080端口运行wechaty docker服务
- python webot.py

### 相关地址
- [配套B站视频教程](https://www.bilibili.com/video/BV1r94y1D7d4)
- [notion api文档](https://developers.notion.com/reference/intro)
- [notion postman 示例](https://www.postman.com/notionhq/workspace/5b01136d-4231-4b8d-95c8-ef9f7c779dd7/overview)
- [wecahty token申请地址](http://pad-local.com/)