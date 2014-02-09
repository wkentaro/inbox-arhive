#!/usr/bin/python3
#-*- coding:utf-8 -*-

def get_example_sentences(word):
    """
    Weblio(http://ejje.weblio.jp)から指定単語の例文を取得する
    引数:
        word: string
        任意の英単語
    """
    import requests
    from bs4 import BeautifulSoup
    url="http://ejje.weblio.jp/sentence/content/" + word;
    s=requests.session()
    r=s.get(url)
    soup=BeautifulSoup(r.text)
    en_exs=[]
    ja_exs=[]
    for k,v in enumerate(soup.find_all("div", attrs={"class": "qotC"})):
        en=v.find("p", attrs={"class", "qotCE"})
        ja=v.find("p", attrs={"class", "qotCJ"})
        if ja.span is not None:
            ja.span.replace_with("")
        if en.script is not None:
            en.script.replace_with("")
        en_exs.append(en.get_text().strip())
        ja_exs.append(ja.get_text(strip=True))
    return dict(zip(en_exs, ja_exs))



import pprint
word=input("Word:")
pprint.pprint(get_example_sentences(word))
