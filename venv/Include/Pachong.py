import requests
from bs4 import BeautifulSoup
import csv
import time
import random


class Pachong:

    def __init__(self, neirong, wenjianming):
        self.neirong = neirong
        self.wenjianming = wenjianming

    def displayEmployee(self):
        print(self.neirong,self.wenjianming)

    def get_content(self,url):
        # url = "https://s.weibo.com/weibo?q=python&nodup=1"
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'SINAGLOBAL=622406699918.1987.1639454708166; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWKn3e9vi8QjA5f7TjYTVwA5JpX5KMhUgL.Fo-NS0zpS0BNe052dJLoI0MLxKqL1-BLBKnLxKqL1-BLBKnLxKqL1-BLBKnLxK-L1hnLB-zLxK.L1K-LB.qLxKBLB.2L1h9A; ALF=1678071124; SSOLoginState=1646535127; SCF=AuRwYbofVjSMSGoDsLdlSDMS6c26XF6a7L42b0aN3xCYqK7Xl4YycxsZga3DEkDo7ZFK1bDNBnz_-I3QyYk6wgg.; SUB=_2A25PIFGHDeRhGeNJ7FAQ9yrLyDyIHXVsVMRPrDV8PUNbmtB-LRj6kW9NS7x1PQYR3290ZwgqpmiO1-L6j50k3UVh; _s_tentry=weibo.com; Apache=5204524980882.534.1646535141815; ULV=1646535141839:5:1:1:5204524980882.534.1646535141815:1645769052152',
            'Host': 's.weibo.com',
            'Referer': 'https://s.weibo.com/weibo?q=python&page=2',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        html = BeautifulSoup(response.content, 'lxml')
        conetnt = html.find_all('div', class_="card-wrap")  # ??????CALSS ???????????????
        for ct in conetnt:
            # print(ct)
            user_info = ct.find_all('a', class_="name")
            if user_info != []:
                user_name = user_info[0].text  # ????????????
                user_index = "https:" + user_info[0]['href']  # ????????????
                user_from = str(ct.find('p', class_="from").text).replace(' ', '').replace('\n', '')  # ?????????????????????????????????
                weibo_content = str(ct.find('p', class_="txt").text).replace(' ', '').replace('\n', '')  # ????????????
                data = [weibo_content, user_name, user_from, user_index]
                self.saveCsv(f'data/csvdata/{self.wenjianming}', data)

    def runx(self):
        #title = input("????????????????????????")
        n = 0
        for x in range(1, 5):
            print(f"???????????????{x}?????????")
            n += 1
            url = f"https://s.weibo.com/weibo?q={self.neirong}&nodup=1&page={x}"
            t = random.randint(2, 5)  # ???????????? 2-5??????
            print(f"{t} ??????????????????")
            time.sleep(t)
            if n % 5 == 0:
                t = random.randint(5, 10)  # ???????????? 5-10??????
                print(f"{t} ??????????????????")
                time.sleep(t)  # ???????????????????????????????????????
            self.get_content(url)

    def saveCsv(self,filename, content):
        fp = open(f"{filename}.csv", 'a+', encoding='utf-8-sig', newline='')
        csv_fp = csv.writer(fp)
        csv_fp.writerow(content)
        fp.close()
        print(f"???????????????{content}")

    def action(self):
        col = ['????????????', '???????????????', '????????????????????????', '???????????????']
        self.saveCsv(f'data/csvdata/{self.wenjianming}', col)
        self.runx()


#pachong1 = Pachong("??????","??????")
#pachong1.action()