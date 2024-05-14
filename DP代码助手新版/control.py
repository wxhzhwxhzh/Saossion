
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 示例下载 https://www.pytk.net/blog/1702564569.html
# 导入UI 将 Controller 的属性 ui 类型设置成 Win
from datetime import datetime

import pyperclip
from ui import Win
import threading
from tkinter import BooleanVar,StringVar,IntVar,END,font
from tkinter.messagebox import showinfo

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
        self.配置()        
        self.updateTime()
        self.绑定()
        
        # TODO 组件初始化 赋值操作
    def 配置(self):
        self.ui.tk_select_box_set_ua.current(0)
        self.ui.tk_select_box_监听类型选择.current(0)
        self.ui.tk_input_监听关键词.configure(textvariable=self.config.监听关键词)
        self.ui.tk_input_监听网址输入框.config(textvariable=self.config.监听网址)

        
        
        self.ui.tk_check_button_忽略.config(variable=self.config.忽略证书错误)
        self.ui.tk_check_button_无头.config(variable=self.config.无头)
        self.ui.tk_check_button_无图.config(variable=self.config.无图)
        self.ui.tk_label_时间.config(textvariable=self.config.更新时间,font=("Arial", 15))

        self.ui.tk_text_代码文本区.configure(font=('consolas',10))
        self.ui.tk_text_代码文本区.insert(END,self.config.初始代码)
        # self.ui.tk_table_监听列表.column('url',width='auto')


    def 绑定(self):
        self.ui.tk_button_开始监听.config(command=self.open_browser)
        self.ui.tk_button_执行上面代码.config(command=self.do)
        self.ui.tk_button_停止监听.config(command= self.stop_listening)
        self.ui.tk_button_复制被选中的行.config(command=self.copy_treeview_to_clipboard)
        self.ui.tk_button_美化监听窗口.config(command=self.adjust_columns_width)

    def copy_treeview_to_clipboard(self):
        selected_item = self.ui.tk_table_监听列表.selection()[0]  # 获取被选中的项
        print(selected_item)
        item_text = self.ui.tk_table_监听列表.item(selected_item, 'values')  # 获取项的文本
        print(item_text,' 已复制')
        pyperclip.copy(item_text[3])  # 将文本复制到剪贴板
        showinfo('已复制',item_text[3])

    def adjust_columns_width(self):
        tree=self.ui.tk_table_监听列表
        for column in tree["columns"]:
            # 获取列标题的宽度
            header_width = font.Font().measure(tree.heading(column)["text"])
            
            # 获取该列中最长字符的宽度
            max_width = max(
                font.Font().measure(tree.set(child, column))
                for child in tree.get_children("")
            )
            
            # 设置列的宽度为标题宽度和最长字符宽度中较大的那个
            tree.column(column, width=max(header_width, max_width+2),anchor='w')    

    def stop_listening(self):
        self.config.停止监听 = True
        print(self.config.停止监听)
        self.page.quit()

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
            self.config.停止监听=False
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
        self.page=page
        tab=page.new_tab()



        #-打开网址
        num=0
        keyword=self.config.监听关键词.get()
        url=self.config.监听网址.get()
        

        tab.listen.start(targets=keyword)
        tab.get(url)
        tab.wait(3)
        for packet in tab.listen.steps():
            if self.config.停止监听:
                page.quit()
                break
            else:    
                r_url=packet.url

                print(r_url)
                
                self.updateListenList((num+1,keyword,self.getTime(),r_url))
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
            self.监听网址=StringVar(value='https://www.baidu.com/')
            self.监听关键词=StringVar(value='.png')
            self.停止监听=False
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





        
