#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用这个代码导入需要的库    pip install DrissionPage tabulate  DataRecorder
#  代码版本低于4.0.0，请升级DP库，至少要4.0.0以上    pip install DrissionPage --upgrade


# 原DP库 使用文档地址 http://g1879.gitee.io/drissionpagedocs/whatsnew/4_0/
# 骚神库网址 https://gitee.com/haiyang0726/SaossionPage


# ----------------导入库----------------
import os,re
import random
import time

from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from colorama import Fore, init
from tabulate import tabulate
from DataRecorder import Filler
# --------------配置类---------------
from  .Config import Config

# 数据类型判断
from DrissionPage.items import SessionElement
from DrissionPage.items import ChromiumElement
from DrissionPage.items import ShadowRoot
from DrissionPage.items import NoneElement
from DrissionPage.items import ChromiumTab
from DrissionPage.items import WebPageTab
from DrissionPage.items import ChromiumFrame










# -------------浏览器类 ----------
class Browser:

    def __init__(self, browser_path="", config="",plugin_path=''):
        self.browser_path = browser_path   


        self.config_browser(config)
        # 加载插件
        if len(plugin_path)>5:
            # [self.co.add_extension(plugin_path)  for f in os.scandir(plugin_path) if f.is_dir()]
            subfolders = [f.path for f in os.scandir(plugin_path) if f.is_dir()]
            for f in subfolders:
                self.co.add_extension(f)
                print('加载插件目录 ',f)
            # self.co.add_extension(plugin_path)   

        self.page = ChromiumPage(addr_or_opts=self.co)

        self.tabs = []
        
        




    def config_browser(self, config):
        self.co = ChromiumOptions()

        if len(self.browser_path)>3:
            self.co.set_browser_path(self.browser_path)
        self.co.set_argument("--hide-crash-restore-bubble")
        co_list = config.split(" ")
        if "多开" in config:
            self.co.auto_port()
        if "无头" in config:
            self.co.headless(True)
        if "无图" in config:
            self.co.no_imgs(True)
        if "无js" in config:
            self.co.no_js(True)
        if "静音" in config:
            self.co.mute(True)
     

        if "匿名" in config:
            self.co.incognito(True)
        if "安卓" in config:
            self.co.set_user_agent(Config.UA_Android)
        if "苹果" in config:
            self.co.set_user_agent(Config.UA_apple)
        if "忽略证书错误" in config:
            self.co.ignore_certificate_errors(True)
        if "最大化" in config:
            self.co.set_argument("--start-maximized")
        if "最小化" in config:
            self.co.set_argument("--start-minimized")
        for i in co_list:
            if i.startswith("超时"):
                self.co.set_timeouts(base=i[2:])
        for i in co_list:
            if i.startswith("端口"):
                self.co.set_local_port(i[2:])
                print("已连接端口为", i[2:])

                
        for i in co_list:
            if i.startswith("代理"):
                self.co.set_proxy(i[2:])

    def open(self, url):
        self.tabs.append(self.page.new_tab(url))
        return self

    def ac(self, ele: ChromiumElement):
        return Actions(ele)

    def upload(
        self,
        tag: str,
        file_path: str,
    ):
        """
        上传文件到指定标签页

        参数:
        tag (str): 标签的定位语法
        file_path (str): 上传文件的具体路径

        返回:
        self
        """
        tab = self.newest_page
        tab.set.upload_files(file_path)
        # 定位元素并点击
        tab.ele(tag).click()
        tab.wait.upload_paths_inputted()
        return self



    @property
    def newest_page(self):
        #t=self.page.get_tab[0]
        return self.page.get_tab(self.page.latest_tab)

    def download_path(self, path):
        self.page.set.download_path(path)
        return self
    def load_js(self, js:str):
        js=Config.current_path()+'\\'+js
        self.newest_page.run_js(js,as_expr=True)
        return self
    
    def temporary_manual_mode(self):
        self.newest_page.add_ele(outerHTML=Config.add_button)
        self.load_js('Tool.js')
        self.newest_page.run_js('setHoverStyle();')
        while True:
            if not  self.newest_page.ele('#randomButton',timeout=0.2):
                break
            time.sleep(0.2)
        return self
    def god_button(self,name='test',onclick='random()'):
        tab=self.newest_page
        div=tab.ele('#god',timeout=0.3)
        if not div:
            tab.add_ele(outerHTML=Config.god_div)
            tab.add_ele(outerHTML=Config.god_css,insert_to=Config.head)
            div=tab.ele('#god',timeout=0.3)

        out_html=Config.god_button.replace('__按钮',name).replace('__onclick',onclick)
        tab.add_ele(outerHTML=out_html,insert_to=div)
        curr_path=os.path.dirname(os.path.abspath(__file__))
        print(curr_path)
        tab.run_js(curr_path+'\\Tool.js',as_expr=True)
        
        # tab.run_js('setHoverStyle();')
    
         

        return self
    def get_current_file_path(self):
        # 获取当前文件的绝对路径
        current_file = os.path.abspath(__file__)
        # 获取当前文件所在的目录路径
        current_dir = os.path.dirname(current_file)
        
        return current_dir

    def download(self, url):
        self.page.download(url)
        return self

    def show_title(self):
        print(self.tab.title)
        return self

    def max(self):
        self.page.set.window.max()
        return self

    def min(self):
        self.page.set.window.mini()
        return self

    def hide(self):
        self.page.set.window.hide()
        return self

    def show(self):
        self.page.set.window.show()
        return self

    def wait(self, num: int):
        time.sleep(num)
        return self
    def quit(self,close_all=False):
        
        if close_all:
            if 'y' in  input('当前模式会关闭所有浏览器进程，包括你自己手动打开的浏览器，是否继续？(y/n)?: '):
                Config.close_chrome()
            else:
                print('已取消')
        else:
            self.page.quit()
        

    def vip_open(self, url, port: int = 0):
        """
        打开vip页面

        :param url: 要访问的页面链接
        :param port: 端口号，默认为0,范围是0-12
        :return: 返回当前对象
        """
        self.page.get(Config.jiekou[port] + url)
        self.page.wait(2)
        if self.page.ele("/html/body"):
            self.page.ele("/html/body").click()

        return self

    def help(self, keyword):
        h = Help()
        h.doc(keyword=keyword)
        return self

    @property
    def gpt(self):
        return GPT(self.page)

    @property
    def jquery(self):
        return Jquery(self)

    def elements(self, k: str, v: str):
        ele = self.tab.eles(f"@{k}={v}")
        return ele

    @staticmethod
    def read_file(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
        return content

    def run(self, script_file: str):
        _page = self.newest_page
        _page.run_js(Browser.read_file(script_file))

    def loadjQuery(self):
        if self.newest_page.ele("#jq", timeout=0.2):
            print("jQuery 已经加载")
        else:
            self.newest_page.run_js(r'.\LoadJquery.js')
            print("jQuery 成功加载入页面...")

    @property
    def tab(self):  # 返回最新的标签页
        return self.page.get_tab(self.page.latest_tab)

    def download_all_img(self, tag):
        """
        从给定的标签中下载所有图片。

        参数:
        self: 当前对象
        tag: 包含要下载图片的标签对象

        返回值:
        self: 返回当前对象
        """
        for i in tag.eles("t:img"):
            for j in ["png", "jpg", "jpeg", "webp", "gif", "tiff"]:
                if j in i.link:
                    self.page.download(i.link)

        return self


# ----------------jQuery 类----------------
class Jquery:
    cmd2 = """

                    $('.m_slider').css({ 'left': '266px', 'pointer-events': 'none' });
                    $('.flx_v_sildbobx').css({ 'background-color': '#EAFCE4', });
                    $('.m_t_txt').css('display', 'none');
                    $('.m_t_txt_sucess').css('display', 'inline-block');
                    sliderFlag = true;
                    """

    def __init__(self, browser: Browser):
        self.b = browser
        self.cmd = r"""
                    function loadjQuery() {
                  // 创建一个 script 元素
                  var script = document.createElement('script');
                
                  // 设置 script 元素的 src 属性为 jQuery 的 CDN 地址
                  script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
                  script.id = 'jq';
                
                  // 将 script 元素添加到文档的头部或 body 中
                  document.head.appendChild(script);
                  // 或者使用 document.body.appendChild(script);
                }
                loadjQuery();
                """

        self.load_jquery()

    def load_jquery(self):
        if self.b.newest_page.ele("#jq"):
            print("jQuery 已经加载")
        else:
            self.run(self.cmd)
            print("jQuery 成功加载入页面...")

    def run(self, js_str: str):
        self.b.newest_page.run_js(js_str)
        return self

    def exe(self, js_str: str):  # 有返回值
        return self.b.newest_page.run_js(js_str)






# ------------工具类----------
class Tool:
    @staticmethod
    def get_random_element(input_list) -> ChromiumElement:
        """
        从输入列表中随机选择一个元素并返回。

        :param input_list: 输入的列表
        :return: 随机选择的元素
        """
        if not input_list:
            return None  # 返回 None，如果列表为空

        return random.choice(input_list)

    @staticmethod
    def sniff_and_download_video(
        page, kw: str = 'x://*[@id="post"]/article/div[3]/div'
    ):
        player = page.ele(kw)
        page.actions.wait(2).click(player)
        player.drag(50, 50, 2)
        player.click.at(40, 70)
        print("视频下载中.......")

    @staticmethod
    def sniff_and_download_videos(ele: ChromiumElement):
        # 执行嗅探并下载视频
        player = ele  # 定义变量player，表示ChromiumElement对象

        time.sleep(2)  # 等待2秒
        player.drag(50, 50, 2)  # 拖动player对象到坐标(50, 50)并移动2像素
        player.click.at(40, 70)  # 在坐标(40, 70)处单击player对象
        print("视频下载中.......")  # 打印提示信息"视频下载中......."

    @staticmethod
    def download_img(page):
        for picture in page("@itemprop=articleBody").eles("t:img"):
            picture.save(path=page.title)
            print("saving the picture..." + str(picture.tag))

    @staticmethod
    def click_next(page):
        page.ele("text:下一篇").click()
        time.sleep(3)

    @staticmethod
    def screenshot(ele, name="viewer"):
        ele.get_screenshot(name=name, scroll_to_center=True)

    @staticmethod
    def trees(ele_or_page):
        """把页面或元素对象DOM结构打印出来
        :param ele_or_page: 页面或元素对象
        :return: None
        """
        def _tree(obj, last_one=True, body=''):
            list_ele = obj.children()
            length = len(list_ele)
            body_unit = '    ' if last_one else '│   '
            tail = '├───'
            new_body = body + body_unit

            if length > 0:
                new_last_one = False
                for i in range(length):
                    if i == length - 1:
                        tail = '└───'
                        new_last_one = True
                    e = list_ele[i]

                    attrs = ' '.join([f"{k}='{v}'" for k, v in e.attrs.items()])
                    print(f'{new_body}{tail}<{e.tag} {attrs}>'.replace('\n', ' '))

                    _tree(e, new_last_one, new_body)

        ele = ele_or_page.s_ele()
        attrs = ' '.join([f"{k}='{v}'" for k, v in ele.attrs.items()])
        print(f'<{ele.tag} {attrs}>'.replace('\n', ' '))
        _tree(ele)
    

    @staticmethod
    def tree(ele):
        init()
        e = ele
        print(f"{Fore.BLUE}{Fore.CYAN}<{e.tag}>  {Fore.RESET}{e.attrs}")
        Tool.__tree(e)

    @staticmethod
    def __tree(ele: any, layer=7, has_next_brother=True, body=""):
        if ele.tag == "iframe":
            # ele = page.get_frame(ele)
            ele = ele("x:/html")
            # print(ele.html)
            # print(ele.children())
        try:
            list_ele = ele.children(timeout=0.1)
        except:
            list_ele = []
            print(ele)
            print("无法获取该元素子元素")

        length = len(list_ele)
        body_unit = "│   " if has_next_brother else "    "
        tail = "├───"
        new_body = body + body_unit

        if length > 0 and layer >= 1:
            has_next_brother2 = True
            for i in range(length):
                if i == length - 1:
                    tail = "└───"
                    has_next_brother2 = False
                e = list_ele[i]
                all_body = f"{Fore.BLUE}{new_body}{tail}{Fore.RESET}"

                print(f"{all_body}{Fore.CYAN}<{e.tag}>{Fore.RESET} ")
                Tool.tree_attr(e, all_body, has_next_brother2, layer)

                Tool.__tree(e, layer - 1, has_next_brother2, new_body)

    @staticmethod
    def tree_attr(ele, body, has_next_brother=True, layer=3):
        e: dict = ele.attrs
        has_child = True if ele.tag == "iframe" or ele.child(timeout=0.2) else False

        if layer == 1:
            has_child = False

        part1 = "│" if has_next_brother else " "
        part2 = "│" if has_child else " "
        replace_part = part1 + "   " + part2
        new_body = body.replace("├───", replace_part).replace("└───", replace_part)

        text = "" if ele.tag == "iframe" else ele.text.split("\n")[0]
        if len(text) >= 1:
            e["inner_txt"] = text if len(text) < 150 else text[0:150] + "......"

        if len(e) > 0:
            e["xpath"] = ele.xpath

            max_k_len = max([len(key) for key in e.keys()])
            head = "┌" + "─" * max_k_len + "┐"
            tail = "└" + "─" * max_k_len + "┘"
            print(new_body, head)

            for k, v in e.items():
                key = Fore.GREEN + str(k).ljust(max_k_len) + Fore.RESET + "│"
                content = f"{key}: {v}"

                print(new_body, "│" + key, v)

            print(new_body, tail)


# ---------------------FormFill 类-----------------------------


class FormFill:
    def __init__(self):
        pass

    @staticmethod
    def open_xl_list(file_name, sort_key=None):
        """
        打开excel, 表头只占一行, 数据从第二行开始, 返回排序好的字典列表

        :param file_name: Excel文件名，必须为xlsx格式，文件后缀可写可不写
        :param sort_key: 排序关键字，默认为行号
        :return: 排序好的字典列表
        """
        if ".xls" not in file_name:
            file_name += ".xlsx"

        # 使用 datarecorder 的 Filler dict_keys
        data_list = Filler(file_name).dict_keys

        # 根据排序关键字对列表进行排序
        return sorted(data_list, key=lambda x: x[sort_key or "row"])

    @staticmethod
    def form_fill(form_ele, data_dict):
        """
        传入 form 元素对象和内容字典，将 form 中相匹配的 name 或 id 的 value 填入，优先使用 name，无 name 则使用id。

        :param form_ele: form 元素
        :param data_dict: 内容字典
        """
        for ele in form_ele.eles("t:input"):
            if ele.attr("name") in data_dict:
                ele.input(data_dict[ele.attr("name")])
            elif ele.attr("id") in data_dict:
                ele.input(data_dict[ele.attr("id")])


# -----------动作链类----------------------------
class Actions:
    def __init__(self, ele: ChromiumElement) -> None:
        self.e = ele
        pass

    def go_right(self, kw, duration=2, mode="0"):
        if "%" in kw:
            for i in range(20):
                self.e.run_js(
                    rf' this.style.left="{i*5*self.__percentage_to_float(kw)}%" '
                )
                time.sleep(duration / 20)
        else:
            for i in range(20):
                self.e.run_js(rf' this.style.left="{int(kw)/20*i}px" ')
                time.sleep(duration / 20)

        return self

    def go_left(self, kw, duration=2):
        if "%" in kw:
            for i in range(20):
                self.e.run_js(
                    rf' this.style.right="{i*5*self.__percentage_to_float(kw)}%" '
                )
                time.sleep(duration / 20)
        else:
            for i in range(20):
                self.e.run_js(rf' this.style.right="{int(kw)/20*i}px" ')
                time.sleep(duration / 20)

        return self

    def __percentage_to_float(self, percentage):
        value = float(percentage.strip("%")) / 100
        return value
    
# 工具类

class Use:
    @staticmethod
    def extract_text(s):
        # 直接使用正则表达式提取并返回结果
        return ''.join(re.findall(r'(?<=>)(.+?)(?=<)', s))

    @staticmethod
    def extract_attrs_value(input_string):
        # 直接返回匹配结果
        return re.findall(r'"[^"]+"', input_string)

    @staticmethod
    def extract_attrs_name(input_string):
        # 改进正则表达式以更精确地匹配属性名
        return re.findall(r'\b\w+(?==")', input_string)

    @staticmethod
    def extract_innertext(input_string):
        # 使用正则表达式简化内部文本提取
        match = re.search(r'>(.*?)<', input_string)
        return match.group(1) if match else ''

    @staticmethod
    def raw(input_str):
        input_str = input_str.strip()
        tag_name_match = re.match(r'<(\w+)', input_str)
        tag_name = tag_name_match.group(1) if tag_name_match else ''
        
        tag_attr_values = Use.extract_attrs_value(input_str)
        tag_attr_names = Use.extract_attrs_name(input_str)
        
        attr_all = ''.join([f'@@{name}={value}' for name, value in zip(tag_attr_names, tag_attr_values)])
        attr_all = attr_all.replace('"', '')
        
        txt = Use.extract_text(input_str)
        tag_txt = f'@@text()={txt}' if txt else ''
        
        transformed_str = f'tag:{tag_name}{attr_all}{tag_txt}'
        print(transformed_str)
        return transformed_str
   
# ---------------- 下面的是测试代码-------------------
if __name__ == '__main__':
    browser1 = Browser(config=' 忽略证书错误  多开   ')
    browser1.open("http://www.baidu.com")
    browser1.page.set.window.location(0,0)


    browser2 = Browser(config=' 忽略证书错误  多开   ')
    browser2.open("https://gitee.com/about_us")
    browser2.page.set.window.location(400,200)

    #退出所有浏览器
    browser1.quit(close_all=True)
    


