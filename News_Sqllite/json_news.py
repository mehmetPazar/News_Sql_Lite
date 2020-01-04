# -*- coding: utf-8 -*-

import json

class Json_news(object):
    
    def __init__(self,news):
        self.json_news = news
        self.datas = ''
        
    def newsJson(self):
        
        data = '{"news": ['  
        for line in self.json_news:
            part = line.split('#')
            data += '{ "id":"' + part[0] + '", "title":"' + part[1].strip().replace('"', "") + '", "author":"' + part[3] + '", "link":"' + part[4] + '", "published":"' + part[5] + '" }, '                
        self.datas =   data[:-2]                  
        self.datas += ']}'
    
        return self.datas
    
    
    def writeJson(self,json_news_data):
        
        json_news_data = self.datas
        with open("json_news.json", "w") as write_file:
            json.dump(json_news_data, write_file)