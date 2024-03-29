import os
import jieba
import wordcloud

# 获取当前文件所在路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 读取文件内容
with open(os.path.join(current_dir, 'jiuzhaigou.csv'), 'r', encoding='utf-8') as f:
    word_list = ''
    for line in f:
        word_list += line.split(',')[6]

# 使用 jieba 分词
word_list = jieba.lcut(word_list)
string = ' '.join(word_list)

# 加载停用词
stopwords = set()
with open(os.path.join(current_dir, 'stopwords.txt'), 'r', encoding='utf-8') as f:
    for line in f:
        stopwords.add(line.strip())

# 创建词云对象
wc = wordcloud.WordCloud(
    width=1920,
    height=1080,
    background_color='#1d2130',
    font_path=os.path.join(current_dir, 'msyh.ttc'),
    stopwords=stopwords,
    collocations=False
)

# 生成词云图像并保存
wc.generate(string)
wc.to_file(os.path.join(current_dir, 'static/word.png'))
