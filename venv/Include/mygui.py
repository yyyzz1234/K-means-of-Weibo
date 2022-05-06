from tkinter import *
from Pachong import Pachong
from Clean import Clean
from TDIDF import TDIDF
from tkinter import messagebox
from K_means import K_means
from Mood import Mood
from K1 import K1
from K2 import K2
import numpy as py
import pandas as pd
import time
class Application(Frame):

    """一个经典gui程序写法"""

    def __init__(self,master=None):#构造器
        super().__init__(master)  #super代表父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):#再次创建组件
        self.label01 = Label(self,text = "功能展示",bg="lightblue",font="data/ttfdata/SimHei.ttf")
        self.label01.grid(row=0,column=0)

        self.btn01 = Button(self,text = '爬取微博内容操作',command=self.createspider)
        self.btn01.grid(row=1,column=0,pady=10)

        self.btn02 = Button(self, text='分词去停用词操作',command=self.createclean)
        self.btn02.grid(row=2, column=0,pady=10)

        self.btn03 = Button(self, text='展现词云操作',command=self.createciyun)
        self.btn03.grid(row=3, column=0,pady=10)

        self.btn04 = Button(self, text='Td-Idf操作',command=self.crtatetdidf)
        self.btn04.grid(row=4, column=0,pady=10)

        self.btn05 = Button(self, text='K-means操作',command=self.createK_means)
        self.btn05.grid(row=5, column=0,pady=10)

        self.btn06 = Button(self, text='清除',command=self.cleantext)
        self.btn06.grid(row=0, column=22)

        self.btn07 = Button(self, text='情感分析', command=self.cleanmood)
        self.btn07.grid(row=6, column=0,pady=10)

        self.btn08 = Button(self, text='k-means++算法优化',command=self.createkmeansjiajia)
        self.btn08.grid(row=7, column=0, pady=10)

        self.label02 = Label(self, text="操作", bg="lightblue",font="data/ttfdata/SimHei.ttf")
        self.label02.grid(row=0, column=5)


        self.label03 = Label(self, text="结果展示", bg="lightblue",font="data/ttfdata/SimHei.ttf")
        self.label03.grid(row=0, column=18)

        self.out_data_Text = Text(self, width=58,height=40)  # 结果框
        self.out_data_Text.grid(row=1, column=13, rowspan=13, columnspan=10,padx=10)

        # 滚动条
        self.result_data_scrollbar_y = Scrollbar(self)  # 创建纵向滚动条
        self.result_data_scrollbar_y.config(command=self.out_data_Text.yview)  # 将创建的滚动条通过command参数绑定到需要拖动的Text上
        self.out_data_Text.config(yscrollcommand=self.result_data_scrollbar_y.set) # Text反向绑定滚动条
        self.result_data_scrollbar_y.grid(row=1, column=23, rowspan=13, sticky='NS')

        self.label04 = Label(self, text="日志展示",bg="lightblue",font="data/ttfdata/SimHei.ttf")
        self.label04.grid(row=12, column=0)

        self.log_data_Text = Text(self, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)

    def createspider(self):
        self.label001=Label(self, text="请输入你想搜索的内容")
        self.label001.grid(row=2, column=5)

        neirong = StringVar()
        self.entry01 = Entry(self, textvariable=neirong)
        self.entry01.grid(row=2, column=6)

        self.label002 = Label(self, text='请输入你想保存的文件名')
        self.label002.grid(row=3, column=5)

        wenjianming = StringVar()
        self.entry02 = Entry(self, textvariable=wenjianming)
        self.entry02.grid(row=3, column=6)

        self.btnspider=Button(self,text="确定",command=self.spider)
        self.btnspider.grid(row=4, column=5)

        self.btnspiderdel = Button(self, text="取消",command=self.spiderdel)
        self.btnspiderdel.grid(row=4, column=6)

    def spider(self):
        pachong = Pachong(self.entry01.get(), self.entry02.get())
        pachong.action()
        self.write_log_to_Text()
        messagebox.showinfo("微博热点发现", "操作成功！")
        df = pd.read_csv(f"data/csvdata/{self.entry02.get()}.csv")
        for i in df['微博内容']:
            self.out_data_Text.insert(1.0, i)
            self.out_data_Text.insert(1.0, '\n')

    def spiderdel(self):#清除操作区
        self.label001.destroy()

        self.entry01.destroy()

        self.label002.destroy()

        self.entry02.destroy()

        self.btnspider.destroy()

        self.btnspiderdel.destroy()

    def createclean(self):
        self.label003 = Label(self, text="请输入你分词去停用词的文件名")
        self.label003.grid(row=2, column=5)

        chuliwenjian = StringVar()
        self.entry03 = Entry(self, textvariable=chuliwenjian)
        self.entry03.grid(row=2, column=6)

        self.btnfenci = Button(self, text="确定", command=self.clean)
        self.btnfenci.grid(row=3, column=5)

        #self.btnciyun = Button(self, text="展现词云", command=self.pltpic)
        #self.btnciyun .grid(row=3, column=6)

        self.btncleandel = Button(self, text="取消", command=self.cleandel)
        self.btncleandel.grid(row=3, column=6)

    def clean(self):
        clean = Clean(self.entry03.get())
        clean.action()
        self.write_log_to_Text()
        messagebox.showinfo("微博热点发现","操作成功！")
        path02 = str(self.entry03.get()).replace(".csv", '')
        stop=[]
        with open(f'data/txtdata/预处理后{path02}文本.txt', 'r', encoding='utf-8') as f:
            stop = f.readlines()
        for i in stop:
            self.out_data_Text.insert(1.0, i)
            self.out_data_Text.insert(1.0, '\n')

    def pltpic(self):
        clean = Clean(self.entry04.get())
        clean.picture(self.entry04.get())
        path02 = str(self.entry04.get()).replace(".txt", '')
        self.photo=PhotoImage(file=f'data/pngdata/{path02}.png')
        self.out_data_Text.image_create(1.0,image=self.photo)
        self.write_log_to_Text()
        messagebox.showinfo("微博热点发现","操作成功！")

    def cleandel(self):
        self.label003.destroy()

        self.entry03.destroy()

        self.btnfenci.destroy()

        #self.btnciyun.destroy()

        self.btncleandel.destroy()

    def createciyun(self):
        self.label004 = Label(self, text="请输入你展示词云的文件名")
        self.label004.grid(row=2, column=5)

        chuliwenjian = StringVar()
        self.entry04 = Entry(self, textvariable=chuliwenjian)
        self.entry04.grid(row=2, column=6)


        self.btnciyun = Button(self, text="确定", command=self.pltpic)
        self.btnciyun.grid(row=3, column=5)

        self.btncidel = Button(self, text="取消", command=self.cidel)
        self.btncidel.grid(row=3, column=6)

    def cidel(self):
        self.label004.destroy()

        self.entry04.destroy()

        self.btnciyun.destroy()

        self.btncidel.destroy()

    def crtatetdidf(self):
        self.label005 = Label(self, text="请输入你Td_Idf处理的文件名")
        self.label005.grid(row=2, column=5)

        tdidfwenjian = StringVar()
        self.entry05 = Entry(self, textvariable=tdidfwenjian)
        self.entry05.grid(row=2, column=6)

        self.btntdidf = Button(self, text="确定", command=self.tdidf)
        self.btntdidf.grid(row=3, column=5)

        self.btntdidfdel = Button(self, text="取消", command=self.tdidfdel)
        self.btntdidfdel.grid(row=3, column=6)

    def tdidf(self):
        tdidf1 = TDIDF(self.entry05.get())
        weight,word=tdidf1.tdidf()
        self.write_log_to_Text()
        messagebox.showinfo("微博热点发现","操作成功！")
        self.out_data_Text.insert(1.0, weight)
        '''for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
            print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
            self.out_data_Text.insert(len(weight), weight)
            for j in range(len(word)):
                print(word[j], weight[i][j])'''

    def tdidfdel(self):
        self.label005.destroy()

        self.entry05.destroy()

        self.btntdidf.destroy()

        self.btntdidfdel.destroy()

    def createK_means(self):
        self.label006 = Label(self, text="请输入你K_means处理的文件名")
        self.label006.grid(row=2, column=5)

        k_meanswenjian = StringVar()
        self.entry06 = Entry(self, textvariable=k_meanswenjian)
        self.entry06.grid(row=2, column=6)

        self.label007 = Label(self, text="你想分成几类")
        self.label007.grid(row=3, column=5)

        num = StringVar()
        self.entry07 = Entry(self, textvariable=num)
        self.entry07.grid(row=3, column=6)

        self.btnK_means = Button(self, text="确定", command=self.K_means)
        self.btnK_means.grid(row=4, column=5)

        self.btnK_meansdel = Button(self, text="取消", command=self.K_meansdel)
        self.btnK_meansdel.grid(row=4, column=6)

    def K_means(self):
        k_means = K_means(self.entry06.get(), int(self.entry07.get()))
        k_means.action()
        path = str(self.entry06.get()).replace("文本.txt", '')
        self.photo1 = PhotoImage(file=f'data/pngdata/{path}聚类.png')
        self.out_data_Text.image_create(1.0, image=self.photo1)
        self.write_log_to_Text()
        messagebox.showinfo("微博热点发现","操作成功！")

    def K_meansdel(self):
        self.label006.destroy()

        self.entry06.destroy()

        self.label007.destroy()

        self.entry07.destroy()

        self.btnK_means.destroy()

        self.btnK_meansdel.destroy()

    def cleanmood(self):
        self.label008 = Label(self, text="请输入你情感分析的的文件名")
        self.label008.grid(row=2, column=5)

        moodwenjian = StringVar()
        self.entry08 = Entry(self, textvariable=moodwenjian)
        self.entry08.grid(row=2, column=6)

        self.btnmood = Button(self, text="确定", command=self.mood)
        self.btnmood.grid(row=3, column=5)

        self.btncidel = Button(self, text="取消", command=self.mooddel)
        self.btncidel.grid(row=3, column=6)

    def mood(self):
        mood = Mood(self.entry08.get())
        mood.action()
        path = str(self.entry08.get()).replace(".csv", '')
        self.photo1 = PhotoImage(file=f'data/pngdata/{path}情感分析.png')
        self.out_data_Text.image_create(1.0, image=self.photo1)
        self.write_log_to_Text()
        messagebox.showinfo("微博热点发现", "操作成功！")

    def mooddel(self):
        self.label008.destroy()

        self.entry08.destroy()

        self.btnmood.destroy()

        self.btncidel.destroy()

    def createkmeansjiajia(self):
        '''self.label008 = Label(self, text="请输入你情感分析的的文件名")
        self.label008.grid(row=2, column=5)

        moodwenjian = StringVar()
        self.entry08 = Entry(self, textvariable=moodwenjian)
        self.entry08.grid(row=2, column=6)'''

        self.btnyuanshi = Button(self, text="原始数据展示", command=self.yuanshikmeans)
        self.btnyuanshi.grid(row=2, column=5)

        self.btnkmeans = Button(self, text="k-means聚类展示", command=self.csdnkmeans)
        self.btnkmeans.grid(row=3, column=5)


        self.btnkmeansjiajia = Button(self, text="k-means++聚类展示", command=self.csdnkmeansjiajia)
        self.btnkmeansjiajia.grid(row=4, column=5)

        self.btnkmeansjiajiadel = Button(self, text="取消", command=self.kmeansjiajiadel)
        self.btnkmeansjiajiadel.grid(row=4, column=6)

    def yuanshikmeans(self):
        self.photo1 = PhotoImage(file=f'data/pngdata/原始数据.png')
        self.out_data_Text.image_create(1.0, image=self.photo1)
        self.write_log_to_Text()
        messagebox.showinfo("微博热点发现", "操作成功！")

    def csdnkmeans(self):
        k1 = K1()
        self.photo2 = PhotoImage(file=f'data/pngdata/kmeans.png')
        self.out_data_Text.image_create(1.0, image=self.photo2)
        self.write_log_to_Text()
        messagebox.showinfo("微博热点发现", "操作成功！")

    def csdnkmeansjiajia(self):
        k2 = K2()
        self.photo3 = PhotoImage(file=f'data/pngdata/kmeans++.png')
        self.out_data_Text.image_create(1.0, image=self.photo3)
        self.write_log_to_Text()
        messagebox.showinfo("微博热点发现", "操作成功！")

    def kmeansjiajiadel(self):
        self.btnkmeans.destroy()
        self.btnyuanshi.destroy()
        self.btnkmeansjiajia.destroy()

        self.btnkmeansjiajiadel.destroy()

    def cleantext(self):#清除结果展示文本框内容
        self.out_data_Text.delete(1.0,'end')

    def get_current_time(self):#获取系统时间
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time

    def write_log_to_Text(self):#写入日志区
        global LOG_LINE_NUM
        LOG_LINE_NUM = 0
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + "操作完成!" + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)

def gui_start():
    root = Tk()
    root.geometry("1180x681+250+40")
    root.title("微博热点发现")
    app = Application(master=root)

    root.mainloop()

gui_start()