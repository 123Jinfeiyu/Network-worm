from snownlp import SnowNLP
import pandas as pd
import re

# 使用NLP情感分析

df = pd.read_csv('jiuzhaigou.csv',names=["username", "usertype", "score", "zan", "sc", "times", "comment"])
content = df['comment']

# 去除一些无用的字符   只提取出中文出来
# 确保content列表中每个元素都是字符串
content = [str(item) for item in content]  # 将所有元素转换为字符串
# 使用正则表达式提取中文字符并连接
content = [' '.join(re.findall(u"[\u4e00-\u9fa5]+", item, re.S)) for item in content]
print(content)

# 对每条评论进行情感打分
scores = [SnowNLP(i).sentiments for i in content]
print(scores)
emotions = []
# 根据分数来划定好评 中评 差评
for i in scores:
    if i >= 0.75:
        emotions.append('好评')
    elif 0.45 <= i < 0.75:
        emotions.append('中评')
    else:
        emotions.append('差评')

df['sent_score'] = scores
df['sent'] = emotions
df.to_csv('NLP测试后数据.csv', encoding='utf-8',
          index=False)
