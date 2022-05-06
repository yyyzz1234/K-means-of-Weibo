#encoding：utf-8
#python: 3.6.8
#编辑器：pycharm

import requests
from bs4 import BeautifulSoup
import csv
import time
import random



def get_content(url):
    # url = "https://s.weibo.com/weibo?q=python&nodup=1"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'SUB=_2A25PEOy5DeRhGeNJ7FAQ9yrLyDyIHXVsZFlxrDV8PUNbmtAKLVjHkW9NS7x1PQ8ZxuozWg0xaaMGwCGk-1tRFyut; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWKn3e9vi8QjA5f7TjYTVwA5JpX5KzhUgL.Fo-NS0zpS0BNe052dJLoI0MLxKqL1-BLBKnLxKqL1-BLBKnLxKqL1-BLBKnLxK-L1hnLB-zLxK.L1K-LB.qLxKBLB.2L1h9A; ALF=1677054057; SSOLoginState=1645518057; _s_tentry=weibo.com; Apache=7316793089824.139.1645518019291; SINAGLOBAL=7316793089824.139.1645518019291; ULV=1645518019306:1:1:1:7316793089824.139.1645518019291:',
        'Host': 's.weibo.com',
        'Referer': 'https://s.weibo.com/weibo?q=python&page=2',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    }
    response = requests.get(url,headers=headers)
    html = BeautifulSoup(response.content,'lxml')
    conetnt = html.find_all('div',class_="card-wrap") # 这里CALSS 要加下划线
    for ct in conetnt:
        # print(ct)
        user_info = ct.find_all('a',class_="name")
        if user_info != []:
            user_name = user_info[0].text# 用户名称
            user_index = "https:"+ user_info[0]['href'] # 用户主页
            user_from = str(ct.find('p',class_="from").text).replace(' ','').replace('\n','') # 时间和发布终端设备名称
            weibo_content = str(ct.find('p',class_="txt").text).replace(' ','').replace('\n','') # 微博内容
            data = [weibo_content,user_name,user_from,user_index]
            saveCsv('微博内容111', data)

def runx():

    n = 0
    for x in range(1,5):

        print(f"正在抓取第{x}页数据")
        n +=1

        url = f"https://s.weibo.com/weibo?q=python&nodup=1&page={x}"
        t = random.randint(2,5)# 随机抽取 2-5之间
        print(f"{t} 秒后开始抓取")
        time.sleep(t)

        if n%5 == 0:
            t = random.randint(5,10) # 随机抽取 5-10之间
            print(f"{t} 秒后继续抓取")
            time.sleep(t) #这里停止上面抽取出来的数值

        get_content(url)


def saveCsv(filename,content):
    fp = open(f"{filename}.csv",'a+',encoding='utf-8-sig',newline='')
    csv_fp = csv.writer(fp)
    csv_fp.writerow(content)
    fp.close()
    print(f"成功写入：{content}")





if __name__ == '__main__':

    col = ['微博内容','发布者名称','发布时间以及设备','发布者主页']
    saveCsv('微博内容111', col)
    runx()