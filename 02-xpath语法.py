# 导入解析模块
from lxml import etree
import requests

# html是获取的网页源码
html = """
<li>
    <div class="item">
        <div class="pic">
            <em class="">1</em>
            <a href="https://movie.douban.com/subject/1292052/">
                <img width="100" alt="肖申克的救赎" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" class="">
            </a>
        </div>
        <div class="info">
            <div class="hd">
                <a href="https://movie.douban.com/subject/1292052/" class="">
                    <span class="title ">肖申克的救赎</span>
                    <span class="title ">&nbsp;/&nbsp;The Shawshank Redemption</span>
                    <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
                </a>


                <span class="playable">[可播放]</span>
            </div>
            <div class="bd">
                <p class="">
                    导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
                    1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
                </p>

                
                <div class="star">
                        <span class="rating5-t"></span>
                        <span class="rating_num" property="v:average">9.7</span>
                        <span property="v:best" content="10.0"></span>
                        <span>2977677人评价</span>
                </div>

                    <p class="quote">
                        <span class="inq">希望让人自由。</span>
                    </p>
            </div>
        </div>
    </div>
</li>
"""

# 创建对象 html指的就是网页源码
tree = etree.HTML(html)

# 解析数据 // 不需要考虑标签位置，直接定位, 找多个span标签，
# 返回的数据类型：列表，直接定位标签，返回的标签元素
# span = tree.xpath('//span')
# print(span, len(span))
# # 获取图片标签
# img = tree.xpath('//img')
# print(img)

# 直系的上下级：/ : 选择当前元素的下一级
# span = tree.xpath('//p/span')
# print(span)

# 获取标签里面的文本信息：/text()
# span = tree.xpath('//p/span/text()')[0]
# print(span)
# # <em class="">1</em>
# # 首先要定位em标签
# em = tree.xpath('//em/text()')
# print(em)

# 获取标签里面的属性值  @属性名
'''
文本内容：<开始标签>文本内容</结束标签>
属性值：<开始标签 class="" href="" src="">
'''
# 图片链接
# img = tree.xpath('//img/@src')[0]
# res = requests.get(img)  # 向图片链接发请求
# with open('1.png', 'wb') as f:  # wb 指的是写入二进制数据
#     f.write(res.content)  # res.content获取响应的二进制数据，写入到文件当中
# # 图片名称
# img_name = tree.xpath('//img/@alt')[0]
# print(img, img_name)

#  通过属性定位到标签[@属性名="属性值"]
# span = tree.xpath('//span[@class="title "]/text()')
# ''.join()  拼接字符串
# print(''.join(span))
# rat = tree.xpath('//span[@class="rating_num"]/text()')
# print(rat)

# 位置定位 xpath位置是从1开始
title = tree.xpath('//div[@class="hd"]/a/span[1]/text()')
print(title)
