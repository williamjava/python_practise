#分别导入了画图的库matplotlib，词云生成库wordcloud 和 jieba的分词库
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

#读取本地的文件
text_from_file_with_apath = open('/Users/wuhoujian/Documents/myself/projects/python_practise/python/txtDir/workCloud.txt').read()

#使用jieba进行分词，并对分词的结果以空格隔开
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

#对分词后的文本生成词云
my_wordcloud = WordCloud().generate(wl_space_split)

#用pyplot展示词云图
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
