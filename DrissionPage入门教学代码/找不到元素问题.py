#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用这个代码导入需要的库 需要提前安装谷歌浏览器   pip install DrissionPage
#  库版本低于4.0.0，请升级DP库，至少要4.0.0以上    pip install DrissionPage --upgrade


# 原DP库 使用文档地址 http://g1879.gitee.io/drissionpagedocs/whatsnew/4_0/

# 骚神库网址 https://gitee.com/haiyang0726/SaossionPage  欢迎各位网友点个star




# # 
# # 问题描述： 1. 网页A切换到网页B后获取不到元素了
# #           2. 在网页里点击某个链接以后  获取不到元素了

#   原因分析：
#     # 1. 由于网页A切换到网页B后，页面对象会自动切换到网页B，所以需要重新获取页面对象
#     # 2. 在网页里点击某个链接以后，页面对象会自动切换到新网页，所以需要重新获取页面对象

#   解决办法：页面反生变化后  加一代码    page=page.get_tab(0)


# # 

from DrissionPage import ChromiumPage,ChromiumOptions
ChromiumOptions().set_p

# 创建页面对象
page = ChromiumPage()
page.get('https://book.douban.com/')

print(page.title)
#点击按钮 页面发生变化，
page.ele('电影').click()




#用下面代码重新获取最新的页面
page=page.get_tab(0)
#等待3秒
page.actions.wait(3)

print(page.title)

page.actions.wait(55)