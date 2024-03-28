#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用这个代码导入需要的库    pip install DrissionPage tabulate  DataRecorder  progress
# 代码版本低于4.0.0，请升级DP库，至少要4.0.0以上    pip install DrissionPage --upgrade

# 原DP库 使用文档地址 http://g1879.gitee.io/drissionpagedocs/whatsnew/4_0/
# 骚神库网址 https://gitee.com/haiyang0726/SaossionPage

# 导入必要的库


from sao  import  *



if __name__ == '__main__':
    browser = Browser(Config.twinkstar_path,config=' 忽略证书错误   ')
    browser.open("http://g1879.gitee.io/drissionpagedocs/")
    time.sleep(2)


    #开启临时手动模式，
    browser.temporary_manual_mode()
    

    # 在网页右侧提供关闭开关 手动模式关闭后自动继续执行后面代码
    browser.newest_page.run_js('alert(123456);')


    
    


    
    

    browser.wait(550)