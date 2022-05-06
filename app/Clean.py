import pandas as pd
import jieba
import codecs
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class Clean:
    def __init__(self,path):
        self.path = path
        self.path02 = str(self.path).replace(".csv",'')

    def clearTxt(self,line:str):
        if (line != ''):

            line = line.strip()
            line = re.sub("[a-zA-Z0-9]", "", line)
            with open('data/txtdata/user_stop_dict.txt', 'r', encoding='utf-8') as f:
                stop = f.readlines()
            stop = [re.sub(' |\n|\ufeff', '', r) for r in stop]
            for i in stop:
                line = line.replace(i, '')
            return line
        return None

    def sent2word(self,line):
        segList = jieba.cut(line, cut_all=False)
        segSentence = ''
        for word in segList:
            if word != '\t':
                segSentence += word + " "
        return segSentence.strip()

    def action(self):
        df = pd.read_csv(f'data/csvdata/{self.path}')
        #global path02
        #path02 = str(self.path).replace(".csv",'')
        target = codecs.open(f'data/txtdata/预处理后{self.path02}文本.txt', 'w', encoding='utf-8')

        for i in df['微博内容']:  # i是str类型
            line = self.clearTxt(i)
            seg_line = self.sent2word(line)
            target.writelines(seg_line + '\n')

    '''def get_word(self):
        data = pd.read_csv(self.path)
        data = data.drop('发布者名称', axis=1)
        data = data.drop('发布时间以及设备', axis=1)
        data = data.drop('发布者主页', axis=1)
        data['分词后'] = data['微博内容'].apply(lambda x: list(jieba.cut(x)))
        with open('user_stop_dict.txt', 'r', encoding='utf-8') as f:
            stop = f.readlines()
        stop = [re.sub(' |\n|\ufeff', '', r) for r in stop]
        data['去除停用词之后'] = [[i for i in s if i not in stop] for s in data['分词后']]

        w = []
        for i in data['去除停用词之后']:
            w.extend(i)
        num_data = pd.DataFrame(pd.Series(w).value_counts())
        num_data['id'] = list(range(1, len(num_data) + 1))
        a = lambda x: list(num_data['id'][x])
        data['词频tongji'] = data['去除停用词之后'].apply(a)
        print(data['去除停用词之后'])
        data.to_csv(f'预处理后{self.path}')
    '''
    def picture(self,path03):
        picpath=str(path03).replace(".txt",'')
        with open(f'data/txtdata/{path03}', 'r', encoding='utf-8') as f:
            stop = f.readlines()
        num_words = [''.join(i) for i in stop]
        num_words = ''.join(num_words)
        num_words = re.sub(' ', '', num_words)
        num = pd.Series(jieba.lcut(num_words)).value_counts()
        wc_pic = WordCloud(background_color='white', font_path=r'data/ttfdata/SimHei.ttf').fit_words(num)
        plt.figure(dpi=100)
        plt.imshow(wc_pic)
        plt.axis('off')
        plt.savefig(f'app/static/images/{picpath}.png')