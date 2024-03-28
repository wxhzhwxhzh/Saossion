#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用这个代码导入需要的库    pip install DrissionPage tabulate  DataRecorder  progress
# 代码版本低于4.0.0，请升级DP库，至少要4.0.0以上    pip install DrissionPage --upgrade

# 原DP库 使用文档地址 http://g1879.gitee.io/drissionpagedocs/whatsnew/4_0/
# 骚神库网址 https://gitee.com/haiyang0726/SaossionPage

# 导入必要的库
# import sys
# sys.path.insert(0, '.')https://www.ckplayer.vip/jiexi/?url=https%3A%2F%2Fwww.bilibili.com%2Fbangumi%2Fplay%2Fep785525%3Fspm_id_from%3D333.337.0.0%26from_spmid%3D666.25.episode.0


from sao import *



import os




if __name__ == '__main__':
    browser = Browser(Config.twinkstar_path,config=' 忽略证书错误  端口9999 ')
    browser.open("https://www.bilibili.com/video/BV1mt421H7PV/?spm_id_from=333.1007.tianma.1-1-1.click")
    time.sleep(2)
    


    #开启万能按钮模式，向网页注入js代码 并绑定相关按钮，实现了类似油猴插件的功能
    browser.god_button(name='翻译网页',onclick="makeTextTo('red')")
    browser.god_button(name='解析网盘',onclick="makeTextTo('blue')")

    browser.god_button(name='文字变色',onclick="makeTextTo('blue')")
    browser.god_button(name='背景切换',onclick="toggleBackgroundColor()")
    browser.god_button(name='自动翻页',onclick="scrollDownSlowly()")
    browser.god_button(name='Github增强',onclick="to_top()")

    browser.god_button(name='解析视频',onclick="parse_vip()")
    browser.god_button(name='js解密',onclick="parse_js()")
    browser.god_button(name='暂停脚本',onclick="parse_vip()")
    
    
    

  


    
    


    
    

    browser.wait(550)