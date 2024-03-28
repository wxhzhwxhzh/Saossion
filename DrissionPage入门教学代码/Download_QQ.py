#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用这个代码导入需要的库 需要提前安装谷歌浏览器   pip install DrissionPage
#  库版本低于4.0.0，请升级DP库，至少要4.0.0以上    pip install DrissionPage --upgrade


# 原DP库 使用文档地址 http://g1879.gitee.io/drissionpagedocs/whatsnew/4_0/

# 骚神库网址 https://gitee.com/haiyang0726/SaossionPage  欢迎各位网友点个star

from DrissionPage import ChromiumPage

# 创建页面对象
page = ChromiumPage()

try:
    # 访问 QQ 官方网站的 PC 版下载页面
    page.get("https://im.qq.com/pcqq/index.shtml")

    page.wait.doc_loaded()

    # 找到下载按钮，并进行点击
    
    button = page.ele('.down-btn wf QQNtDownload QQNtDownloadX64')
    print(f'找到下载按钮: {button}')
    
    page.wait(2)
    page.set.download_path('.')
    button.click()
    data = page.wait.download_begin(cancel_it=True)

    # 等待下载开始，并获取下载信息
    print('正在等待下载开始...')
    page.download(data.url)

    print(data)


except Exception as e:
    print(f'发生错误：{e}')

finally:
    # 不要忘记关闭页面
    page.quit()