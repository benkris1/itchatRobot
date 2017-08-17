# itchatRobot

基于itchat 实现的微信聊天机器人



### 环境准备

基于python 2x 开发，使用的是图灵聊天机器人

如果需要在docker跑的话 首先要根据项目Dockerfile build镜像

```shell
$ docker build -t itchat_robot:0.1 .
```

然后执行

```
$ ./start.sh
```

启动成功后执行

```shell
$ docker logs itchatRobot
```



![bifrost3](http://csqncdn.maxleap.cn/NTgwZDdiZTQ3ZTJjNzkwMDA3NDVhOWQ3/qn-a13aa181-f2b9-44cc-8176-0d5bea4d5b02.MOV)

扫描二维码登录

### 使用

默认聊天机器人是关闭的，如果需要开启自动回复功能需要在微信中 找到自己并输入up。如果启动成功则会返回

`up success` 

ok，现在你的微信可以自动回复了



支持指令

- up 开启微信聊天机器人
- down 关闭
- gp 开启群聊功能
- gd 关闭群聊



如果出现回复内容为 `当天请求次数已用完` 说明需要换`图灵` API key。代码在MyRobot.py中







