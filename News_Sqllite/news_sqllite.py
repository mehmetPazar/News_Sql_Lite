# -*- coding: utf-8 -*-

import sqlite3
import sys
from dha import Dha_news

class News_sqllite(object):
             
    def __init__(self):
        self.news = Dha_news()
        self.connection = sqlite3.connect("DHA_news.db")
        self.cursor = self.connection.cursor()
        if(self.connection):
            print('Baglanti Başarili!')
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS news(Id integer NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE ,
                                        Title text NOT NULL,
                                        Summary text NOT NULL,
                                        Author text,
                                        Link text NOT NULL,
                                        Published text NOT NULL
                                    );""")
        else:
            print("Baglanti Basarisiz!!")
        
    def __del__(self):
        print("Baglanti kapatildi!")
        self.connection.close()
        
    def insertNews(self,News):                       
        try: 
            news = News
            self.cursor.execute("insert into news(Title,Summary,Author,Link,Published) values(?,?,?,?,?)" , (news.getTitle(),news.getSummary(),news.getAuthor(),news.getLink(),news.getPublished()))
            self.connection.commit()
        except:
            print("Bir hata olustu!" + str(sys.exc_info()[0]))
        finally:
            if self.connection is None:           
                self.connection.close()
    
    def controltNews(self,News):                      
        try: 
            news = News
            self.cursor.execute("select Summary from news where Title = ?  and  Link = ? " , (news.getTitle(),news.getLink()) )
            for row in self.cursor:
                return row[0]
        except:
            print("Bir hata olustu!" + str(sys.exc_info()[0]))
        finally:    
            if self.connection is None:           
                self.connection.close()
                
                
    def printNews(self):
        try:
            self.cursor.execute("select * from news")
            for row in self.cursor:
                print(str(row[0]) + "\n" + str(row[1]) + "\n" + str(row[2][:10]) + "\n" + str(row[3]) + "\n" + str(row[4]) + "\n")
                print("-----------------------------------------------------------------------")
        except:
            print("Bir hata olustu!" + str(sys.exc_info()[0]))
        finally:
            if self.connection is None:
                self.connection.close()
                
    def listNews(self):
        try:
            self.cursor.execute("select * from news")
            listnews = []
            for row in self.cursor:
                listnews.append(str(row[0]) + "#" + str(row[1]) + "#" + str(row[2]) + "#" + str(row[3]) + "#" + str(row[4]) + "#" + str(row[5]) )
            
            return listnews
        except:
            print("Bir hata olustu!" + str(sys.exc_info()[0]))
        finally:
            if self.connection is None:
                self.connection.close()
        