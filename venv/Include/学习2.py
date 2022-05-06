mport pandas as pd
import numpy as np

# 读取文本数据

path='冬奥.csv'
data = pd.read_csv(path)
data = data.drop('发布者名称',axis=1)
data = data.drop('发布时间以及设备',axis=1)
data = data.drop('发布者主页',axis=1)

from snownlp import SnowNLP
import matplotlib.pyplot as plt
sentimentslist=[]
for i in data['微博内容']:
    s=SnowNLP(i)
    sentimentslist.append(s.sentiments)
plt.figure(dpi=70)
plt.hist(sentimentslist,bins=np.arange(0,1,0.01),facecolor='g')
plt.rcParams['font.sans-serif']=['Simhei']
plt.xlabel('情绪概率')
plt.ylabel('数量')
plt.title('情感分析')
#plt.figure(figsize=(8, 8))

#path01 = str(self.path).replace(".csv",'')
#plt.savefig(f'{path01}情感分析.png')
plt.savefig('微博内容.png')
plt.show()
