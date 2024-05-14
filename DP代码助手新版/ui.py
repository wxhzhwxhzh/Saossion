"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_tabs_lw4bs9ys = self.__tk_tabs_lw4bs9ys(self)
        self.tk_label_lw4bwp1u = self.__tk_label_lw4bwp1u( self.tk_tabs_lw4bs9ys_2)
        self.tk_label_lw4bx9mq = self.__tk_label_lw4bx9mq( self.tk_tabs_lw4bs9ys_2)
        self.tk_frame_lw4jm7v1 = self.__tk_frame_lw4jm7v1( self.tk_tabs_lw4bs9ys_0)
        self.tk_button_lw4jms1q = self.__tk_button_lw4jms1q( self.tk_frame_lw4jm7v1) 
        self.tk_input_浏览器选择框 = self.__tk_input_浏览器选择框( self.tk_frame_lw4jm7v1) 
        self.tk_frame_lw4jqp0r = self.__tk_frame_lw4jqp0r( self.tk_tabs_lw4bs9ys_0)
        self.tk_button_lw4jqp0s = self.__tk_button_lw4jqp0s( self.tk_frame_lw4jqp0r) 
        self.tk_input_lw4jqp0t = self.__tk_input_lw4jqp0t( self.tk_frame_lw4jqp0r) 
        self.tk_frame_lw4jvht3 = self.__tk_frame_lw4jvht3( self.tk_tabs_lw4bs9ys_0)
        self.tk_label_lw4jvqxx = self.__tk_label_lw4jvqxx( self.tk_frame_lw4jvht3) 
        self.tk_check_button_忽略 = self.__tk_check_button_忽略( self.tk_frame_lw4jvht3) 
        self.tk_check_button_无头 = self.__tk_check_button_无头( self.tk_frame_lw4jvht3) 
        self.tk_check_button_无图 = self.__tk_check_button_无图( self.tk_frame_lw4jvht3) 
        self.tk_frame_lw4jzfpm = self.__tk_frame_lw4jzfpm( self.tk_tabs_lw4bs9ys_0)
        self.tk_label_lw4jzfpn = self.__tk_label_lw4jzfpn( self.tk_frame_lw4jzfpm) 
        self.tk_select_box_set_ua = self.__tk_select_box_set_ua( self.tk_frame_lw4jzfpm) 
        self.tk_frame_lw4k3lt1 = self.__tk_frame_lw4k3lt1( self.tk_tabs_lw4bs9ys_0)
        self.tk_input_lw4k3lt3 = self.__tk_input_lw4k3lt3( self.tk_frame_lw4k3lt1) 
        self.tk_label_lw4k3uau = self.__tk_label_lw4k3uau( self.tk_frame_lw4k3lt1) 
        self.tk_frame_lw4k59hq = self.__tk_frame_lw4k59hq( self.tk_tabs_lw4bs9ys_0)
        self.tk_input_lw4k59hr = self.__tk_input_lw4k59hr( self.tk_frame_lw4k59hq) 
        self.tk_label_lw4k59hs = self.__tk_label_lw4k59hs( self.tk_frame_lw4k59hq) 
        self.tk_label_frame_lw4k6fji = self.__tk_label_frame_lw4k6fji( self.tk_tabs_lw4bs9ys_0)
        self.tk_button_生成更新启动代码 = self.__tk_button_生成更新启动代码( self.tk_label_frame_lw4k6fji) 
        self.tk_label_frame_lw4kkju5 = self.__tk_label_frame_lw4kkju5( self.tk_tabs_lw4bs9ys_0)
        self.tk_text_代码文本区 = self.__tk_text_代码文本区( self.tk_label_frame_lw4kkju5) 
        self.tk_button_lw4kmx1v = self.__tk_button_lw4kmx1v( self.tk_label_frame_lw4kkju5) 
        self.tk_button_执行上面代码 = self.__tk_button_执行上面代码( self.tk_label_frame_lw4kkju5) 
        self.tk_frame_lw4kr47h = self.__tk_frame_lw4kr47h( self.tk_tabs_lw4bs9ys_0)
        self.tk_input_lw4kr47i = self.__tk_input_lw4kr47i( self.tk_frame_lw4kr47h) 
        self.tk_label_lw4kr47j = self.__tk_label_lw4kr47j( self.tk_frame_lw4kr47h) 
        self.tk_label_frame_lw4najzn = self.__tk_label_frame_lw4najzn( self.tk_tabs_lw4bs9ys_1)
        self.tk_table_监听列表 = self.__tk_table_监听列表( self.tk_label_frame_lw4najzn) 
        self.tk_button_复制被选中的行 = self.__tk_button_复制被选中的行( self.tk_label_frame_lw4najzn) 
        self.tk_button_美化监听窗口 = self.__tk_button_美化监听窗口( self.tk_label_frame_lw4najzn) 
        self.tk_frame_lw4nciy3 = self.__tk_frame_lw4nciy3( self.tk_tabs_lw4bs9ys_1)
        self.tk_label_lw4ncvws = self.__tk_label_lw4ncvws( self.tk_frame_lw4nciy3) 
        self.tk_input_监听网址输入框 = self.__tk_input_监听网址输入框( self.tk_frame_lw4nciy3) 
        self.tk_frame_lw4nee06 = self.__tk_frame_lw4nee06( self.tk_tabs_lw4bs9ys_1)
        self.tk_label_监听类型 = self.__tk_label_监听类型( self.tk_frame_lw4nee06) 
        self.tk_select_box_监听类型选择 = self.__tk_select_box_监听类型选择( self.tk_frame_lw4nee06) 
        self.tk_frame_lw4norfy = self.__tk_frame_lw4norfy( self.tk_tabs_lw4bs9ys_1)
        self.tk_button_开始监听 = self.__tk_button_开始监听( self.tk_frame_lw4norfy) 
        self.tk_button_停止监听 = self.__tk_button_停止监听( self.tk_frame_lw4norfy) 
        self.tk_frame_lw4npc76 = self.__tk_frame_lw4npc76( self.tk_tabs_lw4bs9ys_1)
        self.tk_label_监听关键词 = self.__tk_label_监听关键词( self.tk_frame_lw4npc76) 
        self.tk_input_监听关键词 = self.__tk_input_监听关键词( self.tk_frame_lw4npc76) 
        self.tk_label_时间 = self.__tk_label_时间(self)
        self.tk_label_lw4m6rkd = self.__tk_label_lw4m6rkd(self)
    def __win(self):
        self.title("DP代码助手 ")
        # 设置窗口大小、居中
        width = 1215
        height = 638
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_tabs_lw4bs9ys(self,parent):
        frame = Notebook(parent)
        self.tk_tabs_lw4bs9ys_0 = self.__tk_frame_lw4bs9ys_0(frame)
        frame.add(self.tk_tabs_lw4bs9ys_0, text="启动接管")
        self.tk_tabs_lw4bs9ys_1 = self.__tk_frame_lw4bs9ys_1(frame)
        frame.add(self.tk_tabs_lw4bs9ys_1, text="数据监听")
        self.tk_tabs_lw4bs9ys_2 = self.__tk_frame_lw4bs9ys_2(frame)
        frame.add(self.tk_tabs_lw4bs9ys_2, text="关于")
        frame.place(x=10, y=14, width=1183, height=570)
        return frame
    def __tk_frame_lw4bs9ys_0(self,parent):
        frame = Frame(parent)
        frame.place(x=10, y=14, width=1183, height=570)
        return frame
    def __tk_frame_lw4bs9ys_1(self,parent):
        frame = Frame(parent)
        frame.place(x=10, y=14, width=1183, height=570)
        return frame
    def __tk_frame_lw4bs9ys_2(self,parent):
        frame = Frame(parent)
        frame.place(x=10, y=14, width=1183, height=570)
        return frame
    def __tk_label_lw4bwp1u(self,parent):
        label = Label(parent,text="骚神",anchor="center", )
        label.place(x=232, y=12, width=278, height=99)
        return label
    def __tk_label_lw4bx9mq(self,parent):
        label = Label(parent,text="后续功能更精彩，点个star不迷路",anchor="center", )
        label.place(x=119, y=144, width=487, height=30)
        return label
    def __tk_frame_lw4jm7v1(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=0, width=354, height=41)
        return frame
    def __tk_button_lw4jms1q(self,parent):
        btn = Button(parent, text="选择浏览器...", takefocus=False,)
        btn.place(x=18, y=6, width=87, height=30)
        return btn
    def __tk_input_浏览器选择框(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=121, y=6, width=220, height=30)
        return ipt
    def __tk_frame_lw4jqp0r(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=45, width=354, height=41)
        return frame
    def __tk_button_lw4jqp0s(self,parent):
        btn = Button(parent, text="选择下载目录..", takefocus=False,)
        btn.place(x=18, y=6, width=87, height=30)
        return btn
    def __tk_input_lw4jqp0t(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=121, y=6, width=220, height=30)
        return ipt
    def __tk_frame_lw4jvht3(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=89, width=384, height=41)
        return frame
    def __tk_label_lw4jvqxx(self,parent):
        label = Label(parent,text="启动前设置",anchor="center", )
        label.place(x=6, y=5, width=73, height=30)
        return label
    def __tk_check_button_忽略(self,parent):
        cb = Checkbutton(parent,text="忽略证书错误",)
        cb.place(x=94, y=5, width=96, height=30)
        return cb
    def __tk_check_button_无头(self,parent):
        cb = Checkbutton(parent,text="无头",)
        cb.place(x=191, y=5, width=71, height=30)
        return cb
    def __tk_check_button_无图(self,parent):
        cb = Checkbutton(parent,text="无图",)
        cb.place(x=265, y=5, width=80, height=30)
        return cb
    def __tk_frame_lw4jzfpm(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=131, width=257, height=41)
        return frame
    def __tk_label_lw4jzfpn(self,parent):
        label = Label(parent,text="UA设置",anchor="center", )
        label.place(x=6, y=6, width=73, height=30)
        return label
    def __tk_select_box_set_ua(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("PC","安卓","苹果")
        cb.place(x=107, y=6, width=77, height=30)
        return cb
    def __tk_frame_lw4k3lt1(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=235, width=354, height=41)
        return frame
    def __tk_input_lw4k3lt3(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=110, y=6, width=220, height=30)
        return ipt
    def __tk_label_lw4k3uau(self,parent):
        label = Label(parent,text="浏览器启动端口",anchor="center", )
        label.place(x=6, y=6, width=95, height=30)
        return label
    def __tk_frame_lw4k59hq(self,parent):
        frame = Frame(parent,)
        frame.place(x=1, y=279, width=354, height=41)
        return frame
    def __tk_input_lw4k59hr(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=110, y=6, width=220, height=30)
        return ipt
    def __tk_label_lw4k59hs(self,parent):
        label = Label(parent,text="启动网址",anchor="center", )
        label.place(x=6, y=6, width=95, height=30)
        return label
    def __tk_label_frame_lw4k6fji(self,parent):
        frame = LabelFrame(parent,text="功能",)
        frame.place(x=1, y=338, width=365, height=72)
        return frame
    def __tk_button_生成更新启动代码(self,parent):
        btn = Button(parent, text="生成更新启动代码", takefocus=False,)
        btn.place(x=18, y=6, width=119, height=30)
        return btn
    def __tk_label_frame_lw4kkju5(self,parent):
        frame = LabelFrame(parent,text="生成代码预览",)
        frame.place(x=400, y=7, width=754, height=493)
        return frame
    def __tk_text_代码文本区(self,parent):
        text = Text(parent)
        text.place(x=13, y=1, width=702, height=434)
        self.create_bar(parent, text,True, False, 13, 1, 702,434,754,493)
        return text
    def __tk_button_lw4kmx1v(self,parent):
        btn = Button(parent, text="复制上面代码", takefocus=False,)
        btn.place(x=237, y=443, width=86, height=30)
        return btn
    def __tk_button_执行上面代码(self,parent):
        btn = Button(parent, text="执行上面代码", takefocus=False,)
        btn.place(x=345, y=443, width=86, height=30)
        return btn
    def __tk_frame_lw4kr47h(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=183, width=354, height=41)
        return frame
    def __tk_input_lw4kr47i(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=107, y=5, width=220, height=30)
        return ipt
    def __tk_label_lw4kr47j(self,parent):
        label = Label(parent,text="设置代理",anchor="center", )
        label.place(x=6, y=5, width=95, height=30)
        return label
    def __tk_label_frame_lw4najzn(self,parent):
        frame = LabelFrame(parent,text="监听窗口",)
        frame.place(x=354, y=9, width=789, height=523)
        return frame
    def __tk_table_监听列表(self,parent):
        # 表头字段 表头宽度
        columns = {"序号":37,"类型":67,"时间":111,"url":373}
        tk_table = Treeview(parent, show="headings", columns=list(columns),)
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=23, y=0, width=747, height=461)
        self.create_bar(parent, tk_table,True, True,23, 0, 747,461,789,523)
        return tk_table
    def __tk_button_复制被选中的行(self,parent):
        btn = Button(parent, text="复制被选中的行", takefocus=False,)
        btn.place(x=40, y=471, width=112, height=30)
        return btn
    def __tk_button_美化监听窗口(self,parent):
        btn = Button(parent, text="美化监听窗口", takefocus=False,)
        btn.place(x=173, y=471, width=112, height=30)
        return btn
    def __tk_frame_lw4nciy3(self,parent):
        frame = Frame(parent,)
        frame.place(x=11, y=22, width=314, height=42)
        return frame
    def __tk_label_lw4ncvws(self,parent):
        label = Label(parent,text="监听网址",anchor="center", )
        label.place(x=1, y=4, width=64, height=30)
        return label
    def __tk_input_监听网址输入框(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=73, y=6, width=233, height=30)
        return ipt
    def __tk_frame_lw4nee06(self,parent):
        frame = Frame(parent,)
        frame.place(x=11, y=72, width=314, height=42)
        return frame
    def __tk_label_监听类型(self,parent):
        label = Label(parent,text="监听类型",anchor="center", )
        label.place(x=4, y=8, width=57, height=30)
        return label
    def __tk_select_box_监听类型选择(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("所有","图片","视频","音频")
        cb.place(x=79, y=8, width=150, height=30)
        return cb
    def __tk_frame_lw4norfy(self,parent):
        frame = Frame(parent,)
        frame.place(x=10, y=178, width=314, height=42)
        return frame
    def __tk_button_开始监听(self,parent):
        btn = Button(parent, text="开始监听", takefocus=False,)
        btn.place(x=10, y=4, width=66, height=30)
        return btn
    def __tk_button_停止监听(self,parent):
        btn = Button(parent, text="停止监听", takefocus=False,)
        btn.place(x=102, y=5, width=67, height=30)
        return btn
    def __tk_frame_lw4npc76(self,parent):
        frame = Frame(parent,)
        frame.place(x=10, y=127, width=314, height=42)
        return frame
    def __tk_label_监听关键词(self,parent):
        label = Label(parent,text="关键词",anchor="center", )
        label.place(x=1, y=4, width=59, height=30)
        return label
    def __tk_input_监听关键词(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=75, y=4, width=233, height=30)
        return ipt
    def __tk_label_时间(self,parent):
        label = Label(parent,text="时间更新",anchor="center", )
        label.place(x=931, y=599, width=255, height=30)
        return label
    def __tk_label_lw4m6rkd(self,parent):
        label = Label(parent,text="骚神出品",anchor="center", )
        label.place(x=18, y=599, width=85, height=30)
        return label
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_label_时间.bind('<Button-1>',self.ctl.updateTime)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()