#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用这个代码导入需要的库    pip install DrissionPage tabulate  DataRecorder  progress
# 代码版本低于4.0.0，请升级DP库，至少要4.0.0以上    pip install DrissionPage --upgrade

# 原DP库 使用文档地址 http://g1879.gitee.io/drissionpagedocs/whatsnew/4_0/
# 骚神库网址 https://gitee.com/haiyang0726/SaossionPage

# 导入必要的库
from sao import *
from progress.bar import Bar
import sys
import time

# 初始化 彩色字体
init()

if __name__ == "__main__":
    # 连接浏览器
    browser = Browser(Config.Chrome_path, config='忽略证书错误 无头')

    # 从命令行获取参数作为搜索关键词
    kw = sys.argv[1] if len(sys.argv) > 1 else 'rar'  # 获取搜索关键词，默认为 'rar'

    url = fr'https://pc.qq.com/search.html#!keyword={kw}'

    browser.open(url)
    
    tab = browser.page.get_tab(0)
    
    # tab.actions.wait(2)

    # 显示搜索进度条
    with Bar('软件搜索中...', max=20) as bar:
        for _ in range(20):
            time.sleep(0.1)  # 模拟任务
            bar.next()

    # 获取搜索结果信息
    info = tab.ele('x:/html/body/div[3]/div/div[2]/ul/li[1]')
    
    txt = str(info.text)[:-5]
    
    print('搜索到下面的软件：')
    print(f'\n {Fore.GREEN}{txt}{Fore.RESET}  \n')

    # 确认是否下载
    if input('是否下载？[y/n]') in ['y', '1', 'Y', '是']:
        tab('.search-install-fast J_qq_download').click()        
        tab.set.download_path('.')
        # tab.set.download_file_name('123')
        tab('直接下载').click()
        data = tab.wait.download_begin(cancel_it=True)
        tab.download(data.url)

        
