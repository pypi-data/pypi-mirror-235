#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
current_directory = os.path.dirname(os.path.abspath(__file__))

class colors:
    """定义一些ANSI转义序列来表示不同的颜色和样式"""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def red(text):
    print(colors.RED + str(text) + colors.END)

def green(text):
    print(colors.GREEN + str(text) + colors.END)
# 使用颜色打印文本
# print(colors.GREEN + "这段文本是绿色的" + colors.END)
# print(colors.YELLOW + "这段文本是黄色的" + colors.END)
# print(colors.RED + "这段文本是红色的" + colors.END)
#
# # 使用样式打印文本
# print(colors.BOLD + "这段文本是粗体的" + colors.END)