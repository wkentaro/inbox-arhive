#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def feed_events(url):
    """Get events in Google Calendar via the feed"""
    import requests
    from bs4 import BeautifulSoup

    res=requests.get(url)
    soup=BeautifulSoup(res.text)

    data=[]
    for entry in soup.findAll('entry'):
        data.append(
                {
                "id"              : entry.find('id').string,
                "published"       : entry.find('published').string,
                "updated"         : entry.find('updated').string,
                "title"           : entry.find('title').string,
                "summary"         : entry.find('summary').string,
                "content"         : entry.find('content').string,
                "author"          : {"name" : entry.find('name').string,
                                     "email": entry.find('email').string},
                },
        )

    return data

#demo
import pprint
url="https://www.google.com/calendar/feeds/2qeq3jv7ph6o3mg023i31s5te4%40group.calendar.google.com/public/basic"
pprint.pprint(feed_events(url))
