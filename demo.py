# -*- coding: utf-8 -*-
import os
import sys
# 该文件所在位置：D:\第1层\第2层\第3层\第4层\第5层\test11.py
BASE_DIR = os.path.abspath(__file__)
print("当前运行脚本的相对路径(ABSPATH) BASE_DIR:"+BASE_DIR)


path1 = os.path.dirname(__file__)
print("当前运行的脚本的绝对路径 path1:" + path1)  # 获取当前运行脚本的绝对路径

path2 = os.path.dirname(os.path.dirname(__file__))
print("获取当前运行脚本的绝对路径（去掉最后一个路径）path2:"+path2)  # 获取当前运行脚本的绝对路径（去掉最后一个路径）

path3 = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print("获取当前运行脚本的绝对路径（去掉最后2个路径）path3:"+path3)  # 获取当前运行脚本的绝对路径（去掉最后2个路径）path3:

path4 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print("获取当前运行脚本的绝对路径（去掉最后3个路径）path4:"+path4)  # 获取当前运行脚本的绝对路径（去掉最后3个路径）

path5 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
print("获取当前运行脚本的绝对路径（去掉最后4个路径）" +path5)  # 获取当前运行脚本的绝对路径（去掉最后4个路径）

path6 = os.__file__                  #获取os所在的目录
print("获取OS所在的目录 path6:"+path6)

print("sys的路径"+sys.path[0])