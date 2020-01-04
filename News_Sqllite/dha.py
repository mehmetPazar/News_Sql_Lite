# -*- coding: utf-8 -*-

class Dha_news(object):
    
    def __init__(self):
        self.__author = ""
        self.__link = ""
        self.__published = ""
        self.__summary = ""
        self.__title = ""
        print("Nesne baslatildi!")
    
    def __del__(self):
        print("Nesne silindi!")
   
    def getId(self):
        return self.__n_id
    
    def setAuthor(self,author):
        self.__author = author.lower()
    def getAuthor(self):
        return self.__author
    
    def setLink(self,link):
        self.__link = link.lower()
    def getLink(self):
        return self.__link
    
    def setPublished(self,published):
        self.__published = published.lower()
    def getPublished(self):
        return self.__published
    
    def setSummary(self,summary):
        self.__summary = summary.lower()
    def getSummary(self):
        return self.__summary
    
    def setTitle(self,title):
        self.__title = title.lower()
    def getTitle(self):
        return self.__title
    
    