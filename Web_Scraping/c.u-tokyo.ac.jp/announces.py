#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def admin_annouces():
    """Get annouces from the administration office of University of Tokyo"""
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime, time

    url="http://www.c.u-tokyo.ac.jp/zenki/news/kyoumu/index.html"
    host=url.split("/zenki", 2)[0]

    res=requests.get(url)
    soup=BeautifulSoup(res.text)
    newslist=soup.find("div", id="newslist2")

    data=[]
    for line in list(newslist.find("dd").next_siblings):
        if line == "\n":
            continue
        if str(line).startswith("<dt>"):
            data.append(
                    {"date"       : line.contents[0].strip(),
                     "kind_image" : host + line.contents[1].attrs["src"],
                     "grade_image": host + line.contents[2].attrs["src"],
                    },
            )
        elif str(line).startswith("<dd>"):
            data[len(data)-1]["href"]     = host + line.contents[0].attrs["href"]
            data[len(data)-1]["announce"] = line.contents[0].string

    return data

#demo
import pprint
pprint.pprint(admin_annouces())
