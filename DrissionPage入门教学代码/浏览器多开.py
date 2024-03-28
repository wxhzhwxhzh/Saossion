#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用这个代码导入需要的库 需要提前安装谷歌浏览器   pip install DrissionPage
#  库版本低于4.0.0，请升级DP库，至少要4.0.0以上    pip install DrissionPage --upgrade


# 原DP库 使用文档地址 http://g1879.gitee.io/drissionpagedocs/whatsnew/4_0/

# 骚神库网址 https://gitee.com/haiyang0726/SaossionPage  欢迎各位网友点个star


from  sao  import *





if __name__ == '__main__':
    browser1 = Browser(config=' 忽略证书错误  多开   ')
    browser1.open("http://www.baidu.com")
    browser1.page.set.window.location(0,0)


    browser2 = Browser(config=' 忽略证书错误  多开   ')
    browser2.open("https://gitee.com/about_us")
    browser2.page.set.window.location(400,200)
    browser1

    #退出所有浏览器
    browser1.quit(close_all=True)
