# -*- coding: utf-8 -*-

class File_operations(object):
    
    
    def __init__(self):
        print("news_txt'ye yazma islemi baslatildi!")
        self.news_txt= open("news"+".txt","r+" , encoding='utf-8')
    
    def __del__(self):
        
        print("news_txt'ye yazma islemi sonlandirildi!")
        self.news_txt.close()
    
    def writetxt(self,listnews):
        
        for x in listnews :
            column = x.split("#")
            self.news_txt.write(column[0])
            self.news_txt.write("\n")
            self.news_txt.write(column[1])
            self.news_txt.write("\n")
            self.news_txt.write(column[2][:10])
            self.news_txt.write("\n")
            self.news_txt.write(column[3])
            self.news_txt.write("\n")
            self.news_txt.write(column[4])
            self.news_txt.write("\n")
            self.news_txt.write(column[5])
            self.news_txt.write("\n")

    def readtext(self):
        
        i=0
        str = ""
        text_to_news = []
        for line in self.news_txt:
            str += self.news_txt.readline()
            if i%6 != 0 :
                str += "#"
            if i%6 == 0 :
                text_to_news.append(str)
                str = ""    
            i =  i + 1
            
        return text_to_news
        
            