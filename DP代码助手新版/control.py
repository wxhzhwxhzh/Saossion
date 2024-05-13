
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 示例下载 https://www.pytk.net/blog/1702564569.html
# 导入UI 将 Controller 的属性 ui 类型设置成 Win
from datetime import datetime
from ui import Win
import threading
from tkinter import BooleanVar,StringVar,IntVar,END

from DrissionPage import ChromiumPage,ChromiumOptions


class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win
    
    def __init__(self):
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        self.config=Config()     

        self.ui.tk_select_box_set_ua.current(0)
        self.ui.tk_select_box_监听类型选择.current(0)

        
        
        self.ui.tk_check_button_忽略.config(variable=self.config.忽略证书错误)
        self.ui.tk_check_button_无头.config(variable=self.config.无头)
        self.ui.tk_check_button_无图.config(variable=self.config.无图)
        self.ui.tk_label_时间.config(textvariable=self.config.更新时间,font=("Arial", 15))
        self.updateTime()

        self.ui.tk_text_代码文本区.configure(font=('consolas',10))
        self.ui.tk_text_代码文本区.insert(END,self.config.初始代码)

        
        self.绑定()
        
        # TODO 组件初始化 赋值操作

    def 绑定(self):
         self.ui.tk_button_开始监听.config(command=self.open_browser)
         self.ui.tk_button_执行上面代码.config(command=self.do)



    def updateTime(self):
        # 获取当前日期时间
        current_datetime = datetime.now()        
        # 将日期时间对象格式化为字符串
        datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        self.config.更新时间.set(datetime_str)
        self.ui.after(1000,self.updateTime)

    def getTime(self):
          # 获取当前日期时间
        current_datetime = datetime.now()        
        # 将日期时间对象格式化为字符串
        datetime_str = current_datetime.strftime("%H:%M:%S")
        return datetime_str
    def do(self):
        try:
            txt=self.ui.tk_text_代码文本区.get("1.0", "end-1c")
            exec(txt)
        except:
            print('执行出错！！')    
    
         
    def updateListenList(self,t:tuple):
          self.ui.tk_table_监听列表.insert("", "end", text="2", values=t) 

    def open_browser(self):
        try:
            threading.Thread(target=self._open_browser).start()
        except:
            print('浏览器关闭或者出错')    
        

    def _open_browser(self):
        co=ChromiumOptions()

        #-启动配置
        co.set_local_port(7878)
        co.ignore_certificate_errors(True)

        #-创建浏览器
        page = ChromiumPage(co)
        tab=page.new_tab()



        #-打开网址
        num=0

        tab.listen.start(targets='-web.douyinvod.com')
        tab.get('https://www.douyin.com/')
        tab.wait(3)
        for packet in tab.listen.steps():
            r_url=packet.url

            if 'video_mp4' in  r_url:
                print(r_url)
                # url_list.append(r_url)
                self.updateListenList((num+1,'video',self.getTime(),r_url))
                num=num+1
                
                print(tab.title)














class Config():
        def __init__(self):
            self.忽略证书错误= BooleanVar(value=True)
            self.无头= BooleanVar(value=False)
            self.无图= BooleanVar(value=False)
            self.静音= BooleanVar(value=False)
            self.多开= BooleanVar(value=False)
            self.无js= BooleanVar(value=False)
            self.最小化= BooleanVar(value=False)
            self.加载插件= BooleanVar(value=False) 
            self.更新时间= StringVar(value='...')
            self.初始代码="""
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# DrissionPage 库 文档地址 https://www.drissionpage.cn/

#-导入库
from DrissionPage import ChromiumPage,ChromiumOptions

#-导入数据类型判断
from DrissionPage.items import SessionElement
from DrissionPage.items import ChromiumElement
from DrissionPage.items import ShadowRoot
from DrissionPage.items import NoneElement
from DrissionPage.items import ChromiumTab
from DrissionPage.items import WebPageTab
from DrissionPage.items import ChromiumFrame

#-配置类
class Config:
    UA_android="Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36"
    UA_apple="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"


#-创建配置对象
co=ChromiumOptions()

#-启动配置

#-创建浏览器
page = ChromiumPage(addr_or_opts=co)

#-设置文件下载目录 默认是当前目录
page.set.download_path(".")

#-打开网址
page.get('http://gitee.com')

test=input('go on ?')
            """





        
