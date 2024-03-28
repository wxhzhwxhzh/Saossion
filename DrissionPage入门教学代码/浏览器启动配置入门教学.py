#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用这个代码导入需要的库    pip install DrissionPage tabulate  DataRecorder
#  代码版本低于4.0.0，请升级DP库，至少要4.0.0以上    pip install DrissionPage --upgrade


# 原DP库 使用文档地址 http://g1879.gitee.io/drissionpagedocs/whatsnew/4_0/
# 骚神库网址 https://gitee.com/haiyang0726/SaossionPage


# ----------------导入库----------------
from sao import *

# ---------------- 下面的是测试代码-------------------
    
if __name__ == "__main__":


    # 魔法七 连接浏览器  傻瓜式自动识别配置   静音  无图  模拟苹果手机启动  设置代理
    browser = Browser( Config.twinkstar_path,config='    UA苹果  端口9999  ')

    # 打开网站 
    browser.open('https://movie.douban.com/trailer/314095/#content') 
    # browser.loadjQuery()  
     
    # browser.page.run_js('a.js',as_file=true)
