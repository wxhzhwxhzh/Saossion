import requests
import json

class BitBrowser:
    def __init__(self,local_manage_port="http://127.0.0.1:54345"):
        self.local_port =local_manage_port  
        self.headers = {'Content-Type': 'application/json'}
        self.info={}

    # 创建或者更新窗口
    def create_browser(self):
        json_data = {
            'name': 'bit_test',  # 窗口名称
            'remark': '112233',  # 备注
            'proxyMethod': 2,  # 代理方式 2自定义 3 提取IP
            # 代理类型  ['noproxy', 'http', 'https', 'socks5', 'ssh']
            'proxyType': 'noproxy',
            'host': '',  # 代理主机
            'port': '',  # 代理端口
            'proxyUserName': '',  # 代理账号
            "browserFingerPrint": {  # 指纹对象
                'coreVersion': '112'  # 内核版本 112 | 104，建议使用112，注意，win7/win8/winserver 2012 已经不支持112内核了，无法打开
            }
        }
        res = requests.post(f"{self.local_port}/browser/update",
                            data=json.dumps(json_data), headers=self.headers).json()
        self.browser_id = res['data']['id']
        print('浏览器id ',self.browser_id)
        return self.browser_id

    # 更新窗口
    def update_browser(self):
        json_data = {'ids': ['93672cf112a044f08b653cab691216f0'],
                     'remark': '我是一个备注', 'browserFingerPrint': {}}
        res = requests.post(f"{self.local_port}/browser/update/partial",
                            data=json.dumps(json_data), headers=self.headers).json()
        print(res)

    # 直接指定ID打开窗口
    def open_browser(self, browser_id):
        json_data = {"id": f'{browser_id}'}
        res = requests.post(f"{self.local_port}/browser/open",
                            data=json.dumps(json_data), headers=self.headers).json()
        print(res)
        for k,v in res['data'].items():
            print(k,' ',v)
        

        return res

    # 关闭窗口
    def close_browser(self, browser_id):
        json_data = {'id': f'{browser_id}'}
        requests.post(f"{self.local_port}/browser/close",
                      data=json.dumps(json_data), headers=self.headers).json()

    # 删除窗口
    def delete_browser(self, browser_id):
        json_data = {'id': f'{browser_id}'}
        print(requests.post(f"{self.local_port}/browser/delete",
              data=json.dumps(json_data), headers=self.headers).json())
        
    def auto_run_info(self):
        browser_id =self.create_browser()
        res=self.open_browser(browser_id)

        self.info['浏览器路径']=res['data']['driver']
        self.info['调试地址']=res['data']['http']
        self.info['调试端口']=self.info['调试地址'].split(':')[-1]
        
        return self.info
    
    def run_by_id_info(self,browser_id):
        res=self.open_browser(browser_id)

        self.info['浏览器路径']=res['data']['driver']
        self.info['调试地址']=res['data']['http']
        self.info['调试端口']=self.info['调试地址'].split(':')[-1]
        
        return self.info
            
        
        


if __name__ == '__main__':

    
    # info = BitBrowser().run_by_id_info(browser_id='c5071ece0b12473cb9a4eed7dc3f6657')
    info = BitBrowser().auto_run_info()

    driverPath = info['浏览器路径']
    debuggerAddress =info['调试地址']

    print('bit浏览器路径 ',driverPath)
    print('调试地址 ',debuggerAddress)
    input('go on ?')
    # bit_browser.close_browser(browser_id)
    # bb.delete_browser(browser_id)
