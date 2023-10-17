# encoding=utf-8
# 为了兼容Python 2.x，Python 3.x是不需要这个文件的

__doc__ = """core模块的作用主要是为应用层提供一些通用的能力，包括但不限于
1、应用层(handlers模块)的模块加载
2、定时任务调度
3、账号权限控制
4、全局配置和用户配置
5、事件驱动机制
6、HTML模板引擎
7、插件的加载
8、多语言支持

core模块依赖xutils模块，xutils提供更加底层的组件能力，比如数据库、文本函数库、文件操作等等。
两者的区别是：core模块是拥有业务状态的，xutils基本没有。
"""
from . import xnote_pathfix

xnote_pathfix.fix()
