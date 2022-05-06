# coding:utf-8


import jieba
import pandas as pd
import codecs
import string
import re

# 清洗文本
def clearTxt(line:str):

    '''stopwordlist = []
    with open('user_stop_dict.txt', 'r', encoding='utf-8') as f:
        for i in f:
            stopwordlist.append(i)'''

    if(line != ''):
        '''line = line.strip()
        # 去除文本中的英文和数字
        line = re.sub("[a-zA-Z0-9]", "", line)
        # 去除文本中的中文符号和英文符号
        line = re.sub("[\s+\.\!\/_,$%^*(+\"\'；：“”．]+|[+—·！{}『』｜：:（）《》【】，。？?、~@#￥%……&*]+", "", line)
        '''
        with open('user_stop_dict.txt', 'r', encoding='utf-8') as f:
            stop = f.readlines()
        stop = [re.sub(' |\n|\ufeff', '', r) for r in stop]
        #line = [[i for i in s if i not in stop] for s in line]
        for i in stop:
            line = line.replace(i,'')
        line = line.strip()
        return line

    return None

#文本切割
def sent2word(line):
    segList = jieba.cut(line,cut_all=False)
    segSentence = ''
    for word in segList:
        if word != '\t':
            segSentence += word + " "
    return segSentence.strip()



if __name__ == '__main__':
    df = pd.read_csv('何野5.csv')
    target = codecs.open('何野7.txt', 'w', encoding='utf-8')

    for i in df['微博内容']: #i是str类型
        line = clearTxt(i)
        seg_line = sent2word(line)
        target.writelines(seg_line + '\n')



