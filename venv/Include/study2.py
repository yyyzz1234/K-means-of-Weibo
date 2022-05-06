import numpy as py
import pandas as pd
import jieba
import re
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

path='data/csvdata/丰县.csv'
data = pd.read_csv(path)
df = pd.DataFrame(columns=(['colone','coltwo', 'colthree']))
df = data
print(df)
# data = data.drop('发布者名称',axis=1)
# data = data.drop('发布时间以及设备',axis=1)
# data = data.drop('发布者主页',axis=1)
#
#
# data['分词后']=data['微博内容'].apply(lambda x:list(jieba.cut(x)))
# #stop是list类型 换行默认下一个元素
# with open('stopword.txt','r',encoding='utf-8') as f:
#     stop = f.readlines()
#
# stop = [re.sub(' |\n|\ufeff','',r) for r in stop]
# data['去除停用词之后'] = [[i for i in s if i not in stop] for s in data['分词后']]
#
# w=[]
# for i in data['去除停用词之后']:
#     w.extend(i)
# num_data = pd.DataFrame(pd.Series(w).value_counts())
# num_data['id'] = list(range(1,len(num_data)+1))
# a = lambda x:list(num_data['id'][x])
# data['词频tongji'] = data['去除停用词之后'].apply(a)
#
#
#
# num_words = [''.join(i) for i in data['去除停用词之后']]#class'list'
# num_words = ''.join(num_words)#类型str
# num_words=re.sub(' ','',num_words)
# num = pd.Series(jieba.lcut(num_words)).value_counts()
# wc_pic = WordCloud(background_color='white',font_path=r'SimHei.ttf').fit_words(num)
# plt.figure(figsize=(10,10))
# plt.imshow(wc_pic)
# plt.axis('off')
# plt.show()





