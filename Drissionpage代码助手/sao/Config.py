#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用这个代码导入需要的库    pip install DrissionPage tabulate  DataRecorder
#  代码版本低于4.0.0，请升级DP库，至少要4.0.0以上    pip install DrissionPage --upgrade


# 原DP库 使用文档地址 http://g1879.gitee.io/drissionpagedocs/whatsnew/4_0/
# 骚神库网址 https://gitee.com/haiyang0726/SaossionPage

import os
import psutil
import platform


class Config:
    body = "x:/html/body"
    head = "x:/html/head"
    Chrome_path = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe"
    twinkstar_path = r"C:\Program Files\Twinkstar Browser\twinkstar.exe"
    UA_Android="Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36"
    UA_apple="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"




    jiekou = [
            "https://www.ckplayer.vip/jiexi/?url=",
            "https://jx.yparse.com/index.php?url=",
            "https://www.8090g.cn/?url=",
            "https://www.ckplayer.vip/jiexi/?url=",
            "https://jx.qqwtt.com/?url=",
            "https://www.pouyun.com/?url=",
            "https://jx.m3u8.tv/jiexi/?url=",
            "https://z1.m1907.top/?jx=",
            "https://www.8090.la/8090/?url=",
            "https://www.pangujiexi.com/jiexi/?url=",
            "https://dmjx.m3u8.tv/?url=",
            "https://vip.bljiex.com/?v=",
            "https://www.mtosz.com/m3u8.php?url=",
            "https://www.playm3u8.cn/jiexi.php?url=",
            "https://www.yemu.xyz/?url=",
            "https://jx.m3u8.tv/jiexi/?url=",
            "https://api.qianqi.net/vip/?url=",
            "https://jx.playerjy.com/?url=",
            "https://jx.we-vip.com/?url=",
            "https://www.8090g.cn/jiexi/?url=",
            "https://vip.mpos.ren/v/?url=",
            "https://movie.heheda.top/?v=",
            "http://vip.wandhi.com/?v=",
            "https://jx.jsonplayer.com/player/?url=",
            "https://jx.playerjy.com/?url=",
            "https://jx.xmflv.com/?url=",
            "https://jx.xmflv.cc/?url=",
            "https://jx.yparse.com/index.php?url=",
            "https://im1907.top/?jx=",
            "https://www.8090g.cn/?url=",
            "https://api.qianqi.net/vip/?url=",
            "https://jx.yangtu.top/?url=",
            "https://www.ckplayer.vip/jiexi/?url=",
        ]
    

    

    add_button = """
                <div id="ice" style="position: fixed; bottom: 20%; left: 0%;">
            <button id="randomButton" onclick="updateRandomUrl()" style="background-color: rgba(223, 135, 20, 0.521); border-radius: 10px 0 0 10px; font-size: larger;">
                关<br>闭<br>手<br>动
            </button>
        </div>

        """
    god_div = """
                <div id="god_father" style="position: fixed; bottom: 35%; right: 0%;">
                    <div id="god" style="display: flex; flex-direction: column-reverse;">
                    </div>

                </div>
        """
    god_css = """
                <style>
                    .god_class {
                        background-color: rgba(127, 106, 219, 0.6);
                        border: none;
                        border-radius: 5px;
                        color: #fff;
                        cursor: pointer;
                        display: inline-block;
                        font-size: larger;
                        font-weight: bold;
                        margin-bottom: 10px;
                        padding: 10px 20px;
                        text-align: center;
                        text-decoration: none;
                        transition: background-color 0.3s ease;
                    }

                    .god_class:hover {
                        background-color: rgba(127, 106, 219, 1);
                    }
                </style>
        """
    god_button = """               

                    <button class="god_class" onclick="__onclick" >
                        __按钮
                    </button>                
        """
    god_button2 = """
                <div id="ice2" style="position: fixed; bottom: 30%; right: 0%;">

                    <button id="randomButton2" onclick="updateRandomUrl2()" style="background-color: rgba(223, 135, 20, 0.301); 
                    border-radius: 5px 0 0 5px; font-size: larger; display: block; margin-bottom: 10px;">
                        万能按钮
                    </button>

                    <button id="randomButton2" onclick="updateRandomUrl2()" style="background-color: rgba(223, 135, 20, 0.301); 
                    border-radius: 5px 0 0 5px; font-size: larger; display: block; margin-bottom: 10px;">
                        万能按钮
                    </button>



                </div>
        """
    myJS = """
        <script>
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

        function makeTextRed() {
            // 获取页面上的所有文本元素
            var textElements = document.getElementsByTagName('p'); // 获取所有 <p> 标签的文本
            textElements = Array.from(textElements).concat(Array.from(document.getElementsByTagName('span'))); // 获取所有 <span> 标签的文本并合并
        
            // 将所有文本元素的颜色设置为红色
            textElements.forEach(function(element) {
            element.style.color = 'red';
            });
        }
        </script>
        """
    myJS2 = """
        
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

        function makeTextRed(cc) {
            // 获取页面上的所有文本元素
            var textElements = document.getElementsByTagName('p'); // 获取所有 <p> 标签的文本
            textElements = Array.from(textElements).concat(Array.from(document.getElementsByTagName('span'))); // 获取所有 <span> 标签的文本并合并
        
            // 将所有文本元素的颜色设置为红色
            textElements.forEach(function(element) {
            element.style.color = cc;
            });
        }
        
        """
    @staticmethod
    
    def current_path()-> str:
        # 获取当前文件的绝对路径
        current_file = os.path.abspath(__file__)
        # 获取当前文件所在的目录路径
        current_dir = os.path.dirname(current_file)
        
        return str(current_dir)

    @staticmethod    

    def find_chrome_path():
        drive, path = os.path.splitdrive("C:\\")
        search_dir = os.path.join(drive, os.sep, "Program Files", "Google", "Chrome")
        if not os.path.isdir(search_dir):
            search_dir = os.path.join(drive, os.sep, "Program Files (x86)", "Google", "Chrome")
        for root, dirs, files in os.walk(search_dir):
            if "chrome.exe" in files:
                path_chrome = os.path.join(root, "chrome.exe")
                print('找到谷歌浏览器  '+path_chrome)
                return path_chrome
        return False
    
    @staticmethod
    def kill_chrome_processes():
        chrome_processes = [process for process in psutil.process_iter(attrs=['pid', 'name']) if 'chrome.exe' in process.info['name']]
        
        if chrome_processes:
            for process in chrome_processes:
                pid = process.info['pid']
                os.system(f"taskkill /F /PID {pid}")
            print("成功关闭所有谷歌浏览器进程")
        else:
            print("未找到任何谷歌浏览器进程")
    import os


    @staticmethod
    def kill_chrome_processes2():
        system_platform = platform.system()
        
        if system_platform == 'Windows':
            chrome_processes = [process for process in psutil.process_iter(attrs=['pid', 'name']) if 'chrome.exe' in process.info['name']]
            
            if chrome_processes:
                for process in chrome_processes:
                    pid = process.info['pid']
                    os.system(f"taskkill /F /PID {pid}")
                return "成功关闭谷歌浏览器进程"
            else:
                return "未找到谷歌浏览器进程"
        
        elif system_platform == 'Linux' or system_platform == 'Darwin':
            chrome_processes = [process for process in psutil.process_iter(attrs=['pid', 'name']) if 'chrome' in process.info['name']]
            
            if chrome_processes:
                for process in chrome_processes:
                    pid = process.info['pid']
                    os.system(f"kill -9 {pid}")
                return "成功关闭谷歌浏览器进程"
            else:
                return "未找到谷歌浏览器进程"
        
        else:
            return "不支持的操作系统平台"
        
    @staticmethod
    def close_chrome():
        system = platform.system()
        
        if system == "Windows":
            process_names = ["chrome.exe"]
        elif system == "Linux":
            process_names = ["google-chrome", "chrome"]
        elif system == "Darwin":
            process_names = ["Google Chrome"]
        else:
            print("不支持的操作系统平台。")
            return
        
        for proc in psutil.process_iter(['pid', 'name']):
            if any(proc.info['name'] == proc_name for proc_name in process_names):
                pid = proc.info['pid']
                process = psutil.Process(pid)
                process.terminate()
                print(f"进程 {pid} 已被终止。")

        print("所有谷歌浏览器程序已关闭。")  