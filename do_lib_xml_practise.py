# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request

class WeatherSaxHandler(object):
    def __init__(self):
        self.forecast = list()

    def start_element(self,name,attrs):
        if name == "yweather:location":
            self.country = attrs["country"]
            self.city = attrs["city"]
        elif name == "yweather:forecast":
            self.forecast.append({"date":attrs["date"],"high":attrs["high"],"low":attrs["low"]})

    def end_element(self,name):
        pass

    def char_data(self,text):
        pass

def parseXml(xml_str):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return {"city":handler.city,"forecast":handler.forecast}

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
print(result)
assert result['city'] == 'Beijing'