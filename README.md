<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# Nonebot Plugin Hammer Core

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/ArgonarioD/nonebot-plugin-hammer-core/main/LICENSE">
    <img src="https://img.shields.io/github/license/ArgonarioD/nonebot-plugin-hammer-core" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot-plugin-hammer-core">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-hammer-core.svg" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.9-blue.svg" alt="python">
  <img src="https://img.shields.io/badge/nonebot-2.0.0b4-orange" alt="nonebot2">
</p>


## 介绍
本仓库为nonebot-plugin-hammer-xxx等插件的核心依赖，其中主要内容为我本人（ArgonarioD）在开发nonebot2插件与bot时常用的轮子，本仓库在一般情况下不作为nonebot的插件而是作为插件的依赖库安装到nonebot的运行环境中

## 已经实现的轮子
 - `util/constant.py` 常量
 - `util/message_factory.py` 快速构建消息（回复消息）
 - `util/onebot_utils.get_qq_nickname_with_group` 查找QQ群员昵称字符串格式化生成（对不在本群的群员查找昵称与对应群名并格式化生成）

## 鸣谢
 - [onebot](https://github.com/botuniverse/onebot)
 - [nonebot2](https://github.com/nonebot/nonebot2)

---
~~*如果觉得有用的话求点个Star啵QwQ*~~