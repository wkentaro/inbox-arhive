#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def admin_room_changes():
    import requests
    from bs4 import BeautifulSoup

    url = "http://www.c.u-tokyo.ac.jp/zenki/classes/classroomchange/index.html"
    root = url.split("/zenki", 2)[0]

    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    changes = []
    for row in soup.find_all("tr"):
        data = row.find_all("td")
        print(data[0].get_text(strip=True))
        changes.append(
            {"date": data[0].get_text(strip=True),
             "day": data[1].get_text(strip=True),
             "period": data[2].get_text(strip=True),
             "subject": data[3].get_text(strip=True),
             "teacher": data[4].get_text(strip=True),
             "before_change": data[5].get_text(strip=True),
             "after_change": data[6].get_text(strip=True),
             "updated": data[7].get_text(strip=True),
            }
        )
    return changes

import pprint
pprint.pprint(admin_room_changes())
