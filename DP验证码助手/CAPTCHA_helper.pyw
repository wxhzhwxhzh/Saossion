#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用这个代码导入需要的库     pip install DrissionPage ttkbootstrap DataRecorder
#  Drissionpage 代码版本低于4.0.0，请升级DP库，至少要4.0.0以上    pip install DrissionPage --upgrade


# 原DP库 使用文档地址 http://g1879.gitee.io/drissionpagedocs/whatsnew/4_0/
# 骚神库网址 https://gitee.com/haiyang0726/SaossionPage

# ----导入库
# from concurrent.futures import thread
from threading import Thread
from tkinter import Menu,messagebox,filedialog, ttk
from ttkbootstrap import Style
import tkinter as tk
import random,os,time

from BitBrowser import BitBrowser
from sao import Browser

 
# -----主程序
class SaoCode:
    current_dir=os.path.dirname(__file__)    
    father_dir=os.path.dirname(current_dir)
    plugin_dir=current_dir+'\\plugin'
    
    def __init__(self, root):
        self.root = root
        # 窗口长和高和字体
        chang=600
        gao=400
        version=1.1 
        self.font=('宋体', 10)    #等距更纱黑体 SC   

        # 获取屏幕宽度和高度
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # 计算窗口的坐标使其显示在屏幕中心
        x = (screen_width - 539) // 2
        y = (screen_height - 680) // 2 

        # 设置窗口位置
        self.root.geometry(f"{chang}x{gao}+{x}+{y}")

        # 设置窗口标题和logo
        self.root.title(f"验证码助手 {version}-- 骚神库 ") 
        # self.root.iconbitmap(SaoCode.current_dir+'/sao5.ico')

        # 从ttkbootstrap选择一个随机主题
        self.theme_list = Style().theme_names()
        self.selected_theme = random.choice(self.theme_list)
        print(self.theme_list)
        print(self.selected_theme) 
        # self.theme_var=tk.StringVar(value='superhero')

        self.style = Style(theme=self.selected_theme,)         
        self.style.theme_use('superhero')
        

        # 设置全局字体样式
        self.style.configure('.', font=self.font)

        # 配置文件
        self.config={}
    

        # 创建和布局窗口部件
        self.create_widgets()

    def change_skin(self,event):
        t=random.choice(self.theme_list)
        print(t)
        self.style.theme_use(t)


    def open_file_dialog(self):
        file_path = filedialog.askopenfilename()
        print("Selected file:", file_path)
        self.config['浏览器选择路径'].set(file_path)
    def download_dir_dialog(self):
        file_path = filedialog.askdirectory()
        print("Selected path:", file_path)
        self.config['浏览器下载目录选择'].set(file_path)
    def plugin_ask(self):
        file_path = messagebox.showerror(title='程序运行错误！',message='请安装对应的模式的库，再运行...')
        print("Selected path:", file_path)
        self.config['插件目录选择'].set(file_path)

    def create_widgets(self):
        # 创建标签页
        notebook = ttk.Notebook(self.root)
        notebook.pack(pady=10,padx=10)

        # 在notebook里创建标签页
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="配置界面")
       
        self.tab_listen = ttk.Frame(notebook)
        # notebook.add(self.tab_listen, text="运行中操作")

        self.tab_about = ttk.Frame(notebook)
        notebook.add(self.tab_about, text="关于")
 


        # ★★★★★★★★★★启动前操作

        # ----------底部状态信息 按钮   时间显示
        close_frame=ttk.Frame(self.root)
        close_frame.pack()

        # ttk.Button(close_frame, text="关闭浏览器", command=self.close_browsers).pack(padx=10,side="left")
        

        ttk.Separator(self.root,orient="horizontal").pack(fill="x",pady=10)

        self.status_info=tk.StringVar(value="状态信息:   皮肤"+self.selected_theme)
        ttk.Label(self.root,textvariable=self.status_info,wraplength=300).pack(padx=5,side="left")

        self.config['时间']=tk.StringVar(value=" .....")
        ttk.Label(self.root,textvariable=self.config['时间']).pack(padx=10,side="right")
        self.update_time()

        #  更换皮肤按钮
        skin_label=ttk.Label(self.root, text="点我更换皮肤")
        skin_label.pack(padx=10,side="right")
        skin_label.bind("<Button-1>", self.change_skin)





        # ----------进度条
                
        self.progressbar1 = ttk.Progressbar(tab1, length=300, mode='determinate',maximum=30)
        self.progressbar1.pack(pady=10,side="bottom")
        

        # -----------模式选择
        
        radio_frame = ttk.Frame(tab1)
        radio_frame.pack(pady=5, anchor='nw')
        mode_var = tk.StringVar(value="选项1")  # 设置默认值为"选项1"

        ttk.Label(radio_frame, text="识别模式选择:").pack(padx=5, side='left')

        ttk.Radiobutton(radio_frame, text="OpenCV", variable=mode_var, value="选项1").pack(side="left", padx=5)
        ttk.Radiobutton(radio_frame, text="pytesseract", variable=mode_var, value="选项2").pack(side="left", padx=5)
        ttk.Radiobutton(radio_frame, text="Pillow", variable=mode_var, value="选项3").pack(side="left", padx=5)

        # -----------浏览器关联
        
        browser_frame = ttk.Frame(tab1)
        browser_frame.pack(pady=5,anchor='nw')

        self.config['浏览器关联'] = tk.StringVar(value="自动")
        self.config['浏览器关联提示']=tk.StringVar(value="随机检测")


        ttk.Label(browser_frame, text="验证码类型:").pack(padx=5,side='left')        
        ttk.Radiobutton(browser_frame, text="文本选择验证码", variable=self.config['浏览器关联'], value="自动").pack(side="left", padx=5)
        ttk.Radiobutton(browser_frame, text="图片选择", variable=self.config['浏览器关联'], value="手动1").pack(side="left", padx=5)
        ttk.Radiobutton(browser_frame, text="数学问题", variable=self.config['浏览器关联'], value="手动2").pack(side="left", padx=5)
        ttk.Radiobutton(browser_frame, text="图片旋转", variable=self.config['浏览器关联'], value="手动3").pack(side="left", padx=5)
        ttk.Radiobutton(browser_frame, text="符号匹配", variable=self.config['浏览器关联'], value="手动4").pack(side="left", padx=5)
        self.finger_browser_select=ttk.Combobox(browser_frame,values=['比特浏览器','紫鸟浏览器','AdsPower','ixBrowser'],width=9)
        self.finger_browser_select.current(0) 

        # ..................  指纹浏览器

        self.finger_frame = ttk.Frame(tab1)
        self.finger_frame.pack(pady=10,anchor='nw') 
        self.config['指纹浏览器id']=tk.StringVar(value="")  
          
        
 
   
        

        self.finger_label=ttk.Label(self.finger_frame,textvariable= self.config['浏览器关联提示'])
        self.finger_label.pack(side="left", padx=5)       
        
        self.finger_entry=ttk.Entry(self.finger_frame,textvariable=self.config['指纹浏览器id'],width=40) 
        self.finger_button=ttk.Button(self.finger_frame, text="接管指纹浏览器", command=self.start_finger_browser)
        
        

        

        # -----------浏览器路径选择
        
        browser_frame2 = ttk.Frame(tab1)
        browser_frame2.pack(pady=5,anchor='nw')
        self.config['浏览器选择路径'] = tk.StringVar(value=' ')

        browser_select=ttk.Label(browser_frame2,textvariable=self.config['浏览器选择路径'])
        browser_select.pack(padx=5,side='left') 

        ttk.Label(browser_frame2, text="验证码主域名地址").pack(padx=5,side='left')

        xy_entry=ttk.Entry(browser_frame2)
        xy_entry.pack(padx=5,side='left')

        button = ttk.Button(browser_frame2, text="开始监听验证码...", command=self.plugin_ask)
        button.pack()
        # -----------浏览器上传文件选择路径选择
        
        upload_frame = ttk.Frame(tab1)
        upload_frame.pack(pady=5,anchor='nw')
        self.config['浏览器上传文件选择'] = tk.StringVar(value='默认只监听')

        browser_select=ttk.Label(upload_frame,textvariable=self.config['浏览器上传文件选择'])
        browser_select.pack(padx=5,side='left') 

        button = ttk.Button(upload_frame, text="开始识别验证码")
        button.pack(padx=5,side='left')
        ttk.Button(upload_frame, text="监听并识别验证码").pack(padx=5,side='left')
        # -----------浏览器下载目录选择
        
        # download_dir_frame = ttk.Frame(tab1)
        # download_dir_frame.pack(pady=5,anchor='nw')
        # self.config['浏览器下载目录选择'] = tk.StringVar(value='默认是当前文件夹')

        # browser_select=ttk.Label(download_dir_frame,textvariable=self.config['浏览器下载目录选择'])
        # browser_select.pack(padx=5,side='left') 

        # button = ttk.Button(download_dir_frame, text="选择下载目录...", command=self.download_dir_dialog)
        # button.pack()
        # # -----------插件目录选择
        
        # plugin_dir_frame = ttk.Frame(tab1)
        # plugin_dir_frame.pack(pady=5,anchor='nw')
        # self.config['插件目录选择'] = tk.StringVar(value='默认是不加载')

        # browser_select=ttk.Label(plugin_dir_frame,textvariable=self.config['插件目录选择'])
        # browser_select.pack(padx=5,side='left') 

        # button = ttk.Button(plugin_dir_frame, text="选择插件目录...", command=self.plugin_dir_dialog)
        # button.pack()

        # # -----------启动前参数

        # before_set_frame = ttk.Frame(tab1)
        # before_set_frame.pack(pady=5,anchor='nw')
        # self.config['忽略证书错误'] = tk.BooleanVar(value=True)
        # self.config['无头'] = tk.BooleanVar(value=False)
        # self.config['静音'] = tk.BooleanVar(value=False)
        # self.config['多开'] = tk.BooleanVar(value=False)
        # self.config['无js'] = tk.BooleanVar(value=False)
        # self.config['最小化'] = tk.BooleanVar(value=False)
        # self.config['加载插件'] = tk.BooleanVar(value=False)

        # ttk.Label(before_set_frame, text="启动前设置 ").pack(padx=5,side='left')

        # ttk.Checkbutton(before_set_frame, text="忽略证书错误", variable=self.config['忽略证书错误']).pack(padx=5,side='left')       
        # ttk.Checkbutton(before_set_frame, text="无头", variable=self.config['无头']).pack(padx=5,side='left')       
        # ttk.Checkbutton(before_set_frame, text="静音", variable=self.config['静音']).pack(padx=5,side='left')
        # ttk.Checkbutton(before_set_frame, text="多开", variable=self.config['多开']).pack(padx=5,side='left')
        # ttk.Checkbutton(before_set_frame, text="无js", variable=self.config['无js']).pack(padx=5,side='left')
        # ttk.Checkbutton(before_set_frame, text="最小化", variable=self.config['最小化']).pack(padx=5,side='left')
        # ttk.Checkbutton(before_set_frame, text="加载插件", variable=self.config['加载插件'],name='333').pack(padx=5,side='left')

        # # -----------设置浏览器UA

        # UA_set_frame = ttk.Frame(tab1)
        # UA_set_frame.pack(pady=5,anchor='nw')
        # self.config['UA'] = tk.StringVar(value="PC端")
   

        # ttk.Label(UA_set_frame, text="UA设置  ").pack(padx=5,side='left')        
  

        
        # self.UA_set_box=ttk.Combobox(UA_set_frame,values=['PC端','安卓端','苹果端'],width=9,textvariable=self.config['UA'])
        # self.UA_set_box.current(0)
        # self.UA_set_box.pack(padx=5,side='left')      

        # # -----------代理ip

        # proxy_ip_frame = ttk.Frame(tab1)
        # proxy_ip_frame.pack(pady=5,anchor='nw')
        # self.config['代理ip'] = tk.StringVar(value="")

        # ttk.Label(proxy_ip_frame, text="代理地址(http://ip:port)").pack(padx=5,side='left')

        # self.proxy_entry=ttk.Entry(proxy_ip_frame,textvariable=self.config['代理ip'])
        # self.proxy_entry.pack(padx=5,side='left')

        # # -----------设置cookie

        # cookie_frame = ttk.Frame(tab1)
        # cookie_frame.pack(pady=5,anchor='nw')
        # self.config['cookie']=tk.StringVar(value='格式是 name1=value1; name2=value2; path=/; domain=.example.com')

        # ttk.Label(cookie_frame, text="Cookie ").pack(padx=5,side='left')        
        # ttk.Entry(cookie_frame,textvariable=self.config['cookie'],width=90).pack(padx=5,side='left') 
        # # -----------设置浏览器启动端口

        # port_frame = ttk.Frame(tab1)
        # port_frame.pack(pady=5,anchor='nw')
        # self.config['启动端口']=tk.StringVar(value='自动')

        # ttk.Label(port_frame, text="浏览器启动端口 ").pack(padx=5,side='left')        
        # ttk.Entry(port_frame,textvariable=self.config['启动端口']).pack(padx=5,side='left') 

        # # -----------启动网址

        # start_url_frame = ttk.Frame(tab1)
        # start_url_frame.pack(pady=5,anchor='nw')

        # self.config['启动网址']=tk.StringVar(value='https://gitee.com/g1879/DrissionPage')

        # ttk.Label(start_url_frame, text="启动网址 ").pack(padx=1,side='left')        
        # self.start_url_entry=ttk.Entry(start_url_frame,width=40,textvariable=self.config['启动网址'])
        
        # self.start_url_entry.pack(padx=1,side='left')
        # self.start_url_entry.bind("<Button-3>", self.show_menu)

        # #  右键菜单
        # self.menu = Menu(self.root, tearoff=0)
        # self.menu.add_command(label="复制", command=lambda: self.to_copy(self.start_url_entry))
        # self.menu.add_command(label="粘贴", command=lambda: self.to_paste(self.start_url_entry))
        # self.menu.add_command(label="清空", command=lambda: self.start_url_entry.delete(0, 'end'))

        # # -----------功能按钮

        # start_button_frame = ttk.Frame(tab1)
        # start_button_frame.pack(pady=5,anchor='nw')

        # ttk.Label(start_button_frame, text="按钮 ").pack(padx=5,side='left')        
        # ttk.Button(start_button_frame, text="启动或接管浏览器", command=self.start_browser).pack(padx=5,side='left')
        # ttk.Button(start_button_frame, text="关闭浏览器", command=self.close_browsers).pack(padx=5,side='left')
        # ttk.Button(start_button_frame, text="清除Cookie和缓存").pack(padx=5,side='left')
        
        # ttk.Button(start_button_frame, text="预览配置", command=lambda:self.new_window(tab1,title='配置预览',show_config=True)).pack(padx=5,side='left')

        

       



        

        # #  ★★★★★★★★★★ 关于 标签页
        # # 引入图片

        # # self.image = tk.PhotoImage(file=SaoCode.current_dir+ "/logo.png")
        # # about_frame = ttk.Frame(tab_about)
        # # about_frame.pack(pady=5,anchor='center')

        # # ttk.Label(about_frame, image=self.image,cursor='heart',text='骚神',compound="center",font=('楷体',28),foreground='white').pack(anchor='center')
        # # ttk.Separator(about_frame,orient="horizontal").pack(fill="x")
        # # ttk.Label(about_frame, text=' 骚神库官网 https://gitee.com/haiyang0726/SaossionPage ',underline=12,foreground='red').pack(pady=10,anchor='center')
        # # ttk.Label(about_frame, text='  \n\n    后续更新更精彩功能，顺手点个star⭐').pack(anchor='center')
        
        # # ttk.Label(about_frame, text='\n'*5+' DrissionPage 代码助手  -- 骚神库 ',font=('黑体',14)).pack(anchor='center')
        

        


        # # 生成代码按钮
        # ttk.Button(close_frame, text="生成启动代码", command=lambda:self.new_window(tab1,title='生成代码预览',code=CodeDemo.get_code(self.config))).pack(padx=5,side='left')

    # 显示右键菜单
    def show_menu(self, event):
        self.menu.post(event.x_root, event.y_root)

    # 粘贴
    def to_paste(self, ele):
        ele.event_generate("<<Paste>>")

    # 复制

    def to_copy(self, ele):
        ele.event_generate("<<Copy>>")
        # Listener(self).test()
        
    def print_message2(self):
        for k,v in self.config.items():
            print(k,v.get())
    

    # 启动浏览器 多线程
    def start_browser(self):
        self.status_info.set("正在启动浏览器..")
        self.progressbar1.start()
        Thread(target=self._start_browser).start() 

    def _start_browser(self):
        browser_path = self.config["浏览器选择路径"].get()
        port:str=self.config["启动端口"].get()
        if self.config["浏览器关联"].get() == "自动" or "默认" in browser_path:
            browser_path = "."

        print(browser_path)
        _config = " "
        if self.config["忽略证书错误"].get():
            _config += " 忽略证书错误"
        if self.config["无头"].get():
            _config += "  无头"
        if self.config["静音"].get():
            _config += " 静音"
        if self.config["多开"].get():
            _config += " 多开"
        if self.config["无js"].get():
            _config += " 无js"        
        if self.config["最小化"].get():
            _config += " 最小化"        
        if self.config["UA"].get()=='安卓端':
            _config += " 安卓端"        
        if self.config["UA"].get()=='苹果端':
            _config += " 苹果端"        

        if port.isdigit():
            _config += " 端口"+port
            
        print(_config)
        p_path = SaoCode.plugin_dir  if self.config["加载插件"].get()  else  ''

        browser = Browser(browser_path, config=_config,plugin_path=p_path)
        url = self.start_url_entry.get()
        if "http" in url:
            browser.open(url)
        else:
            print(url)
        # self.status_info.set("浏览器启动成功,运行中..")
        self.status_info.set(f'浏览器启动成功,运行中.. ({_config})')    

        self.progressbar1.stop()

        self.browser = browser

    # 启动指纹浏览器 多线程
    def start_finger_browser(self):
        self.status_info.set("正在启动指纹浏览器..")
        self.progressbar1.start()
        Thread(target=self._start_finger_browser).start() 

    def _start_finger_browser(self):
        id=self.config['指纹浏览器id'].get()
        if len(id)<5 :
            self.status_info.set(f'指纹浏览器  启动失败......')
        else:  

            info = BitBrowser().run_by_id_info(id)
            _config=str(info)            
            self.status_info.set(f'指纹浏览器启动成功,运行中.. ({_config})')
            self.config['启动端口'].set(info['调试端口'])   
            self.config['浏览器选择路径'].set('指纹浏览器 '+info['浏览器路径']) 
            self.start_browser()  
            #---------这里可以加后续代码！！
             


            
        self.progressbar1.stop()

    # 关闭浏览器
    def close_browsers(self):
        self.progressbar1.start()
        self.status_info.set("浏览器关闭中..")
        Thread(target=self._close_browsers).start()       

    def _close_browsers(self):        
        self.browser.quit()      
        self.status_info.set("浏览器关闭成功")
        self.progressbar1.stop()        
        


    #  实时更新的 日期和时间        
    def update_time(self):          

        self.config['时间'].set(time.strftime('%Y-%m-%d %H:%M:%S'))
        # 每秒钟更新一次时间
        self.root.after(1000, self.update_time)

    def toggle_finger_button(self):
        if self.config['浏览器关联'].get()=='指纹':
            self.config['浏览器关联提示'].set('指纹浏览器ID')
            self.finger_browser_select.pack(side="left", padx=5)
            self.finger_entry.pack(side="left", padx=5)
            self.finger_button.pack(side="left", padx=5)
        else:            
            self.config['浏览器关联提示'].set('浏览器： '+self.config['浏览器关联'].get())
                
            self.finger_entry.forget()
            self.finger_button.forget() 
            self.finger_browser_select.forget()

    def new_window(self,root,show_time=False,show_config=False,title='预览',code=''):
        # filename = filedialog.askopenfilename()  # 弹出文件选择对话框，获取用户选择的文件路径
        new_window = tk.Toplevel(root)  # 创建新窗口
        new_window.title("代码生成预览")
        new_window.geometry("1200x600")
        
        code_frame = ttk.Frame(new_window)
        code_frame.pack()

        code_label = ttk.Label(code_frame, text=title)
        code_label.pack(side='left')
        # code_Button = ttk.Button(code_frame, text='复制下面代码')
        # code_Button.pack(side='right')
        
        # 创建带有垂直滚动条的文本框
        text_frame = ttk.Frame(new_window)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 创建滚动条
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        code_text = tk.Text(text_frame, width=70, font=("Consolas", 10), yscrollcommand=scrollbar.set)        
        code_text.pack(fill=tk.BOTH, expand=True)
        
        # 设置滚动条的command为文本框的yview
        scrollbar.config(command=code_text.yview)

        # 写入数据
        code_text.insert(tk.END,code)
        # print(code)

        if show_config:
            for k,v in self.config.items():
                code_text.insert(tk.END, '\n'+k+': '+str(v.get()))  
        
        
        def update_time():          
            code_text.insert(tk.END, '\n'+time.strftime('%Y-%m-%d %H:%M:%S'))
            # 每秒钟更新一次时间
            root.after(1000, update_time)
            
        if show_time:
            update_time()          

class CodeDemo():
    file=SaoCode.current_dir+'/code_frame.txt'
    target_code=''    
    @staticmethod
    def file_content(file_path)->str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return f"{file}文件未找到，请检查文件路径是否正确。"  
        

    @staticmethod
    def get_code(c:dict):
        fc=CodeDemo.file_content(CodeDemo.file)
        browser_path=c['浏览器选择路径'].get()
        daili_ip=c['代理ip'].get()
        port=c['启动端口'].get()
        start_url=c['启动网址'].get()
        download_dir=c['浏览器下载目录选择'].get()        
        plugin_dir=c['插件目录选择'].get()        
        cookie_str=c['cookie'].get()        
        if c['忽略证书错误'].get():
            fc=fc.replace('#-启动配置','#-启动配置\n'+'co.ignore_certificate_errors(True)')
        if c['最小化'].get():
            fc=fc.replace('#-启动配置','#-启动配置\n'+'co.set_argument("--start-minimized")')
            
        if c['多开'].get():
            fc=fc.replace('#-启动配置','#-启动配置\n'+'co.auto_port()')
        else:            
            if port.isdigit() :
                fc=fc.replace('#-启动配置','#-启动配置\n'+f'co.set_local_port({port})')

        if c['无头'].get():
            fc=fc.replace('#-启动配置','#-启动配置\n'+'co.headless(True)')
        if c['静音'].get():
            fc=fc.replace('#-启动配置','#-启动配置\n'+'co.mute(True)')
        if c['UA'].get()=='安卓端':
            fc=fc.replace('#-启动配置','#-启动配置\n'+'co.set_user_agent(Config.UA_android)')
        if c['UA'].get()=='苹果端':
            fc=fc.replace('#-启动配置','#-启动配置\n'+'co.set_user_agent(Config.UA_apple)')

        if '.exe' in browser_path:
            fc=fc.replace('#-启动配置','#-启动配置\n'+f'co.set_browser_path("{browser_path}")')

        if 'http' in daili_ip:
            fc=fc.replace('#-启动配置','#-启动配置\n'+f'co.set_proxy("{daili_ip}")')


        if  len(download_dir)>2 and '默认' not in download_dir:
            fc=fc.replace('download_path(".")',f'download_path(r"{download_dir}")')

        if  len(plugin_dir)>3 and '默认' not in plugin_dir:
            fc=fc.replace('#-启动配置','#-启动配置\n'+f'co.add_extension(r"{plugin_dir}")')

        if  len(cookie_str)>3 and '格式是' not in cookie_str:
            fc=fc.replace('#-打开网址','##-打开网址\n'+f'page.set.cookies(r"{cookie_str}")')

        if 'http' in start_url:
            fc=fc.replace('http://gitee.com',start_url)
        CodeDemo.target_code=fc 
        print(fc)   

        return fc   
            

class ListenTab():
    def __init__(self,main):
        self.tab=main.tab_listen
        self.config=main.config
        self.main=main

    def test(self):
        for k,v in self.config.items():
            print(k,v.get())
    def run(self):
        tab_frame = ttk.Frame(self.tab)
        tab_frame.pack(pady=15,anchor='nw')

        ttk.Label(tab_frame,text='功能').pack(side='left')

        self.listen_button=ttk.Button(tab_frame, text="开启监听任务..",state='disabled',command=lambda:self.new_window(self.tab))
        self.listen_button.pack(padx=15,side='left')
        self.JS_button=ttk.Button(tab_frame, text="JS代码注入..",state='disabled')
        self.JS_button.pack(padx=15,side='left')
        self.switch_button()

    #循环监听 按钮状态    
    def switch_button(self):
        if not hasattr(self.main,'browser') or self.main.browser is None:
            self.listen_button.config(state='disabled')
            self.JS_button.config(state='disabled')
            # print('meiyou')
        else:
            self.listen_button.config(state='normal')
            self.JS_button.config(state='normal')
            # print('you')
        self.main.root.after(1000,self.switch_button)   


    def new_window(self,root,show_time=True):
            # self.main.start_browser()
            
            new_window = tk.Toplevel(root)  # 创建新窗口
            new_window.title("数据监听")
            new_window.geometry("1200x600")
            
            code_frame = ttk.Frame(new_window)
            code_frame.pack()

            
            ttk.Button(code_frame, text="开始监听",command=lambda:listen()).pack(padx=15,side='left')
       
                        
         
            
            # 创建带有垂直滚动条的文本框
            text_frame = ttk.Frame(new_window)
            text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            # 创建滚动条
            scrollbar = tk.Scrollbar(text_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            code_text = tk.Text(text_frame, width=70, font=("等距更纱黑体 SC", 12),background='black',foreground='green', yscrollcommand=scrollbar.set)        
            code_text.pack(fill=tk.BOTH, expand=True)
            
            # 设置滚动条的command为文本框的yview
            scrollbar.config(command=code_text.yview)

            def update_data():          
                code_text.insert(tk.END, '\n'+time.strftime('%Y-%m-%d %H:%M:%S'))
                # 每秒钟更新一次时间
                root.after(1000, update_data)
                
            # 写入数据
            def listen():
                tab=self.main.browser.page.new_tab()
                tab.listen.start('jd.com')
                tab.get('https://www.jd.com')
                for packet in tab.listen.steps():
                    data1=packet.request.url  # 打印数据包url                    
                    
                    try:
                        if code_text is not None:
                            
                            code_text.insert(tk.END, '\n'*2+time.strftime('%Y-%m-%d %H:%M:%S')+'---->'+data1)
                            code_text.yview_moveto(1.0)
                    except:
                        print('窗口关闭，监听结束')
                        tab.listen.stop() 


                    
            try:   

                Thread(target=listen).start()
            except:
                print('窗口关闭')        
                

  
                
                
                     
                
        





class AboutTab():
    def __init__(self,main):
        self.tab=main.tab_about
        
    def test(self):
        for k,v in self.config.items():
            print(k,v.get())
    def run(self):
                
        # self.image = tk.PhotoImage(file=SaoCode.current_dir+ "/logo.png")

        about_frame = ttk.Frame(self.tab)
        about_frame.pack(pady=5,anchor='center')

        ttk.Label(about_frame,cursor='heart',text='骚神',font=('楷体',34),foreground='black',anchor='center').pack(anchor='center')

        ttk.Separator(about_frame,orient="horizontal").pack(fill="x")
        ttk.Label(about_frame, text=' 骚神库官网 https://gitee.com/haiyang0726/SaossionPage ',underline=12,foreground='red').pack(pady=10,anchor='center')
        ttk.Label(about_frame, text='  \n\n    后续更新更精彩功能，顺手点个star⭐').pack(anchor='center')
        
        ttk.Label(about_frame, text='\n'*5+' 验证码助手  -- 骚神库 ',font=('黑体',14)).pack(anchor='center')



def main():
    root = tk.Tk()    
    app = SaoCode(root)
    ListenTab(app).run()
    AboutTab(app).run()
    root.mainloop()

if __name__ == "__main__":
    main()
