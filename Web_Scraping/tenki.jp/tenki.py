#!/usr/bin/env python
#-*- coding:utf-8 -*-

def get_tokyo_tenki():
    import requests
    from bs4 import BeautifulSoup
    
    url="http://tenki.jp/component/static_api/rss/forecast/city_63.xml"
    response=requests.get(url)
    #print(response.text)
    soup=BeautifulSoup(response.text)
    #print(soup.prettify())
    data = []
    for item in soup.find_all('item'):
        d, w, t = item.title.string.split(" ")
        data.append({
            "date": d,
            "weather": w,
            "temperature": t,
            })
    return data

print(get_tokyo_tenki())
