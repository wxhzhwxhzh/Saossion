#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用这个代码导入需要的库     pip install DrissionPage tabulate  DataRecorder
#  pysimplegui  使用太高的库 可能会有注册登录提示   最好使用    pip install PySimpleGUI==4.60.5
#  Drissionpage 代码版本低于4.0.0，请升级DP库，至少要4.0.0以上    pip install DrissionPage --upgrade


# 原DP库 使用文档地址 http://g1879.gitee.io/drissionpagedocs/whatsnew/4_0/
# 骚神库网址 https://gitee.com/haiyang0726/SaossionPage

# ----------------导入库----------------
import webbrowser
import PySimpleGUI as sg
# import threading
import concurrent.futures
from sao import *

# 定义可用的主题列表
themes = ['LightGreen', 'DarkBlue', 'Dark', 'LightBlue']

def change_theme():
    # 随机选择一个主题
    new_theme = random.choice(themes)
    sg.theme(new_theme)

def god_button(browser):
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


# 设置窗口图标
sg.set_global_icon('./img/sao5.ico')


# 设置全局字体样式
sg.set_options(font= ('等距更纱黑体 SC', 12))
# 设置局部字体样式
f_style = ('Arial ', 10)
names=[]
# 定义布局
layout = [
    [sg.TabGroup([
        [sg.Tab('启动前配置', [
            [sg.Text('模式选择:', font=f_style), sg.Radio('ChromePage', "mode", default=True, key='mode_select'), sg.Radio('SessionPage', "mode"), sg.Radio('WebPage', "mode")],
            [sg.Text('选择浏览器:'), sg.Radio('手动指定浏览器', "Browser", default=True), sg.Radio('自动搜索浏览器', "Browser")],

            [sg.Text('默认是本地谷歌浏览器'), sg.FileBrowse('浏览器选择:')],
            [sg.Text('默认为当前目录'), sg.FolderBrowse('选择下载目录')],

            [sg.Text('启动前设置:'), sg.Checkbox('忽略证书错误', default=True, key='ignore'), sg.Checkbox('无头模式', key='wutou'), sg.Checkbox('静音', key='jingyin'), sg.Checkbox('多开', key='duokai'), sg.Checkbox('无js', key='wujs')],
            [sg.Text('UA选择:'), sg.Radio('PC端', group_id="UA", key='pc', default=True), sg.Radio('安卓端', group_id="UA", key='android'), sg.Radio('苹果端', group_id="UA", key='ios')],
            [sg.Text('启动网址:'), sg.InputText(default_text=r'http://g1879.gitee.io/drissionpagedocs/', key='first_url')],
            # [sg.Text('启用代理'), sg.Checkbox('', default=False, key='proxy_enabled')],
            [sg.Text('代理 IP:'), sg.InputText(tooltip='为空时 不走代理', key='proxy_ip', disabled=False)],
            [sg.Text('加载cookie:'), sg.InputText(key='Cookie')],
            # [sg.Text('加载插件：'), sg.InputText(key='ChaJian')],
            [sg.Text('加载插件：'), sg.FolderBrowse('选择插件目录')],
            [sg.Button('启动接管浏览器', key='启动接管浏览器', button_color='green'), sg.Button('接管已打开的浏览器', key='接管已打开的浏览器'), sg.Button('打印配置', key='打印配置')],
        ])],

        [sg.Tab('启动后操作', [
            [sg.Text('选择js文件'), sg.FileBrowse('js选择:')],
            [sg.Button('开始注入js文件', key='开始注入js文件'), sg.Button('嵌入万能按钮', key='嵌入万能按钮')],

            [sg.Text('网址:'), sg.InputText(key='网址', disabled=False), sg.Button('打开网址', key='打开网址')],
            [sg.Text('监听字段：'), sg.InputText(key='Listen', disabled=False), sg.Button('监听下载', key='监听下载')],
            [sg.Text('定位元素：'), sg.InputText(key='Listen', size=(20, 1)), sg.Combo(['xPath', 'css', '原生'], default_value='XPath'), sg.Combo(['点击', '拖拽', '其他'], default_value='点击')],
            [sg.Text('操作元素：'), sg.InputText(key='Listen2', disabled=False), sg.Button('执行', key='执行')],

            [sg.Text('按钮：'), sg.Button('启动脚本', key='启动脚本'), sg.Button('暂停操作', key='暂停操作'), sg.Button('循环操作', key='循环操作'), sg.Button('条件操作', key='条件操作')]
        ])],

        [sg.Tab('VIP下载', [
            [sg.Text('功能介绍：主要下载观看各个付费和免费的vip的视频，音乐和软件资源')],
            [sg.Text('视频网址:'), sg.InputText(key='vip_video', disabled=False), sg.Button('开始观看视频', key='开始观看视频')],
            [sg.Text('音乐网址:'), sg.InputText(key='vip_music', disabled=False), sg.Button('开始下载音乐', key='开始下载音乐')],
            [sg.Text('软件名称：'), sg.InputText(key='vip_software', disabled=False), sg.Button('扫描软件并下载', key='扫描软件并下载')],
            [sg.Text('默认为当前目录'), sg.FolderBrowse('选择下载目录', key='dl_dir')],
            [sg.Button('恢复默认配置', key='恢复默认配置')]
        ])],

        [sg.Tab('监听抓取', [
            [sg.Text('功能介绍：主要监听网页请求的资源并给出资源列表')],
            [sg.Input(size=(20, 1), font=('Arial Bold', 14), expand_x=True, key='-INPUT-'),
             sg.Button('Add'),
             sg.Button('Remove'),
             sg.Button('Exit')],
            [sg.Listbox(names, size=(20, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='-LIST-')],
            [sg.Text("", key='-MSG-', font=('Arial Bold', 14), justification='center')],
        ])],

        [sg.Tab('关于', [
            [sg.Image(filename="./img/logo.png", key='sao_logo', enable_events=True)],
            [sg.Text('SaossionPage   简称 【骚神page】 基于  Drissionpage开发的  图形化界面，内涵各种黑魔法👹 慎用🔞！')],
            [sg.Text('骚神库网址 https://gitee.com/haiyang0726/SaossionPage 后续更新更精彩功能  顺手点个star⭐')],
            [sg.Text('访问官方地址 '), sg.Text('SaossionPage', font=('黑体', 16), enable_events=True, text_color='blue')],
            [sg.Text('访问DrissionPage 地址 '), sg.Text('DrissionPage', font=('黑体', 16), enable_events=True, text_color='red')],
            [sg.Text('访问DrissionPage 学习文档 '), sg.Text('DrissionPage 文档', font=('黑体', 16), enable_events=True, text_color='yellow')],
            [sg.Image(filename="./img/logo3.png", key='sao_logo', enable_events=True)],
        ])],

    ])],
    [sg.Button('关闭浏览器', key='关闭浏览器', button_color='red')],

    [sg.Text('.......', font=f_style, text_color='yellow', key='状态')]

]



def browser_start():
    browser = Browser()
# ---------------- 下面的是测试代码-------------------
def update_ele(window):
    window.write_event_value('更新状态', '浏览器已启动...')
def update_status(window,a,b):
    window[a].update(b)
    window.refresh()


def start_browser(values):
    gui_config = " "
    if values["pc"]:
        pass
    elif values["ios"]:
        gui_config += " 苹果"
    elif values["android"]:
        gui_config += " 安卓"

    if values["ignore"]:
        gui_config += " 忽略证书错误"
    if values["wutou"]:
        gui_config += " 无头"
    if values["jingyin"]:
        gui_config += " 静音"
    if values["wujs"]:
        gui_config += "无js"
    if "http" in values["proxy_ip"]:
        gui_config += " 代理" + values["proxy_ip"]

    browser = Browser(values["浏览器选择:"], config=gui_config)
    url = values["first_url"]
    if "http" in url:
        browser.open(url)

    return browser


def download_software(browser, values):

    # 下载软件
    browser = browser
    va = values["vip_software"]
    dl = values["dl_dir"] if values["dl_dir"] else "."

    # 从命令行获取参数作为搜索关键词
    kw = (
        va if len(va) > 1 else sg.popup_get_text("请输入一个软件名", title="Textbox")
    )  # 获取搜索关键词，默认为 'rar'

    url = rf"https://pc.qq.com/search.html#!keyword={kw}"

    browser.open(url)

    tab = browser.page.get_tab(0)

    # tab.actions.wait(2)

    # 获取搜索结果信息
    info = tab.ele("x:/html/body/div[3]/div/div[2]/ul/li[1]")

    txt = str(info.text)[:-5]

    print("搜索到下面的软件：")
    print(f"\n {Fore.GREEN}{txt}{Fore.RESET}  \n")

    # 确认是否下载
    if sg.popup_yes_no(f"信息 {txt}  是否下载?", title="搜索到下面的软件：") == "Yes":
        tab(".search-install-fast J_qq_download").click()
        tab.set.download_path(dl)

        tab("直接下载").click()
        data = tab.wait.download_begin(cancel_it=True)
        tab.download(data.url)
        sg.popup_auto_close(f"{kw} 下载完成，保存在：{dl}", auto_close_duration=4)
        sg.popup_notify(f"{kw} 下载完成，保存在：{dl}")


def main():

    # 创建窗口 主题
    sg.theme("BlueMono")
    window = sg.Window("骚神库图形版 1.0", layout)

    # 事件循环
    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            break
        if event == "启动接管浏览器":
            window["状态"].update("浏览器启动中...")
            window.refresh()

            # threading.Thread(target=update_ele, args=(window), daemon=True).start()
            # threading.Thread(target=start_browser, args=(values), daemon=True).start()
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(start_browser, values)
                browser = future.result()
            sg.popup_auto_close("浏览器已打开",title="提示",auto_close_duration=1)
            update_status(window,'状态','浏览器运行中.....')     

        if event == "打印配置":
            print(values["浏览器选择:"])
            print(values)
            for k ,v in values.items():
                print(k,": ",v)

        browser.open(values["网址"]) if event == "打开网址" else None
        god_button(browser) if event == "嵌入万能按钮" else None
        webbrowser.open('https://gitee.com/haiyang0726/SaossionPage')  if event == "SaossionPage" else None
        webbrowser.open('https://gitee.com/haiyang0726/SaossionPage')  if event == "sao_logo" else None
        webbrowser.open('http://g1879.gitee.io/drissionpagedocs/history/statement')  if event == "DrissionPage 文档" else None

        if event =='proxy_ip':
            if  'http' in  window['proxy_ip']:
                window['proxy_ip'].update('http://'+window['proxy_ip'].get())

        if event == "扫描软件并下载":
            download_software(browser,values)        
        

        if event == "关闭浏览器":
            update_status(window,"状态","浏览器关闭中...")
            browser.quit()
            update_status(window,"状态","zzz...")


if __name__ == "__main__":
    main()
