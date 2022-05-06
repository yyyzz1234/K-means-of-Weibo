# coding:utf-8
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import pandas as pd
# 清洗文本
class TDIDF:
    def __init__(self,path):
        self.path = path
        #self.path02 = str(self.path).replace(".csv", '')
    def tdidf(self):
        #   texts = f.readlines()
        with open(f'data/txtdata/{self.path}','r',encoding='utf-8') as f:
            texts = f.readlines()
        vectorizer = CountVectorizer(max_features=10)  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
        transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
        tfidf = transformer.fit_transform(
            vectorizer.fit_transform(texts))  # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
        word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
        weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
        print(weight)
        # np.savetxt("./result.txt", weight)
        for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
            print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
            for j in range(len(word)):
                print(word[j], weight[i][j])
        return weight,word

        # 将文本中的词转换成词频矩阵
        '''vectorizer = CountVectorizer()
        # print(vectorizer)
        # 计算某个词出现的次数
        X = vectorizer.fit_transform(texts)
        print(type(X), X)
        # 获取词袋中所有文本关键词
        word = vectorizer.get_feature_names()
        print(vectorizer.vocabulary_)
        print(word)
        # 查看词频结果
        print(X.toarray())

        transformer = TfidfTransformer()
        # print(transformer)
        # 将词频矩阵统计成TF-IDF值
        tfidf = transformer.fit_transform(X)
        # 查看数据结构tfidf[i][j]表示i类文本中tf-idf权重
        # print(type(tfidf.toarray()))
        print(tfidf.toarray())
        '''