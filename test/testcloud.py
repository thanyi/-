# -*— coding = utf-8 -*-
# @Time : 2021/1/19 21:44
# @Author : ethanyi
# @File : testcloud.py
# @Software : PyCharm
import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3


conn = sqlite3.connect("../豆瓣电影.db")
c = conn.cursor()
sql ="select introduction from movies"
data = c.execute(sql)
text = ""
for item in data:
    text = text +item[0]

c.close()
conn.close()


cut = jieba.cut(text)
str = " ".join(cut)


img = Image.open(r"../static/assets/img/tree.jpg")
img_array = np.array(img)
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="STXINGKA.TTF"
)

wc.generate_from_text(str)


fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')

plt.show()
# plt.savefig(r"./static/assets/img/word.jpg")