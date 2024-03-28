from DrissionPage import ChromiumPage

page = ChromiumPage()

page.listen.start('jd.com')  # 开始监听，指定获取包含该文本的数据包
page.get('https://www.jd.com/')  # 访问网址，这行产生的数据包不监听
for packet in page.listen.steps():
    data1=packet.request.url  # 打印数据包url
    print('\n'*5)
    print(data1)
    data2=packet.url

    
    if type(data2)==dict:
        for k,v in data2.items():
            print(k,' ',v)
    else:
        print(data2)


    # page('@rel=next').click()  # 点击下一页
    