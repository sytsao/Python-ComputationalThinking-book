#e5-4-1自然語言處理
#載入jieba與jieba.analyse。
import jieba
import jieba.analyse

# 把檔案的內容讀出來，請將文章存在目錄的article.txt中
f = open('article.txt','r',encoding = 'utf8')
article = f.read()

# 透過jieba內建的idf頻率庫, 我們可以計算文章中最重要的字詞
tags = jieba.analyse.extract_tags(article, 10)
print("最重要字詞", tags)
