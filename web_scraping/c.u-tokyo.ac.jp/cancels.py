#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def admin_room_cancels():
    import requests
    from bs4 import BeautifulSoup

    url = "http://www.c.u-tokyo.ac.jp/zenki/classes/cancel/index.html"
    root = url.split("/zenki", 2)[0]

    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    cancels = []
    for tr in soup.find_all("tr"):
        tdata = tr.find_all("td")
        cancels.append(
            {"date": tdata[0].get_text(strip=True),
             "day": tdata[1].get_text(strip=True),
             "period": tdata[2].get_text(strip=True),
             "subject": tdata[3].get_text(strip=True),
             "teacher": tdata[4].get_text(strip=True),
             "room": tdata[5].get_text(strip=True),
             "updated": tdata[6].get_text(strip=True),
            }
        )
    return cancels

# demo
import pprint
pprint.pprint(admin_room_cancels())
