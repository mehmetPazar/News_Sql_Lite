# -*- coding: utf-8 -*-

import feedparser
from dha import Dha_news
from news_sqllite import News_sqllite
from file_operations import File_operations
from json_news import Json_news



news = feedparser.parse('https://ajanda.dha.com.tr/feed/rss/')

sqllite = News_sqllite()
dha_news_s = Dha_news()
file_news = File_operations()


for i in range(0,20):
    dha_news_s.setTitle(news["entries"][i]["title"])
    dha_news_s.setSummary(news["entries"][i]["summary"])
    dha_news_s.setAuthor(news["entries"][i]["author"])
    dha_news_s.setLink(news["entries"][i]["link"])
    dha_news_s.setPublished(news["entries"][i]["published"])
    
    if sqllite.controltNews(dha_news_s) != dha_news_s.getSummary():
        sqllite.insertNews(dha_news_s)
    else:
        print("Bu haber kayitlidir!")

#sqllite.printNews()
file_news.writetxt(sqllite.listNews())
#print(file_news.readtext())
     
json_news_dha = Json_news(sqllite.listNews())
x = json_news_dha.newsJson()
json_news_dha.writeJson(x)

#print(datas)

#y = json.loads(datas)
#print(y["news"])

del file_news
del dha_news_s
del sqllite

    
 
