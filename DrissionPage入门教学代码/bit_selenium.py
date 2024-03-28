from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bit_api import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service

# /browser/open 接口会返回 selenium使用的http地址，以及webdriver的path，直接使用即可
bb=createBrowser()
res = openBrowser(bb)
driverPath = res['data']['driver']
debuggerAddress = res['data']['http']

print(driverPath)
print(debuggerAddress)


# # selenium 连接代码
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", debuggerAddress)

# chrome_service = Service(driverPath)
# driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# driver.get('https://www.baidu.com/')
# print(driver.title)
