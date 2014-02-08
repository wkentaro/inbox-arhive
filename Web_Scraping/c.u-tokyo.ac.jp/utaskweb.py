#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
root = "https://zkyomu.c.u-tokyo.ac.jp"

def login_utaskweb(session, username, password, code_number):
    print("Logging in UTask-Web...")
    action = root + "/utask/campus"
    data = {'view': 'view.initial',
            'func': 'function.login',
            'usernm': username,
            'passwd': password,
            'code_num': code_number,}
    headers = {'User-Agent': 'Mozilla/5.0(Windows;U;Windows NT 5.1;rv:1.7.3) Gecko/20041001Firefox/0.10.1'}
    request = session.post(action, data=data, 
                           allow_redirects=True, headers=headers)
    return request

def meta_refresh(html, session):
    soup  = BeautifulSoup(html)
    result = None
    for meta in soup.find_all("meta"):
        if meta.attrs['http-equiv'].lower() == "refresh":
            result = meta
    if result:
        url=result["content"].split(";")[1].strip()
        request = session.get(root + url[4:])
        return request
    return None

def syllabus_link(html, session):
    """ Get syllabus refering link"""
    print("Crawling syllabus in Utask-Web...")

    # find frame tag which contains syllabus link
    menu = None
    for frame in BeautifulSoup(html).find_all('frame'):
        if frame.attrs['name'] == "menu":
            request=session.get(root+frame.attrs['src'])
            menu=request.text
    soup = BeautifulSoup(menu)
    menu_open = None
    for k, v in enumerate(soup.find_all('a')):
        if k is 9:
            menu_open = v.attrs['href']
    url = root + menu_open
    request = session.get(url)
    soup = BeautifulSoup(request.text)
    syllabus_link = None
    for k, v in enumerate(soup.find_all('a')):
        if k is 10:
            syllabus_link = v.attrs['href']
    url = root + syllabus_link
    request = session.get(url)
    return request

def search_syllabus(html, session, nendo=2013, semester=""):
    print("Starting search in syllabus...")
    soup = BeautifulSoup(html)
    ott4cs = soup.find('input', attrs={'name':'ott4cs'}).attrs['value']
    action = root + soup.find('form', attrs={'name': 'SearchForm'}).attrs['action']
    gakki = None
    if semester is "summer":
        gakki = 1
    elif semester is "winter":
        gakki = 2
    data = {'view': 'view.syllabus.refer.search.input.gakusei',
            'ott4cs': ott4cs,
            'func': 'function.syllabus.refer.search',
            's_type': '1',
            'nendo': nendo,
            'j_s_cd': '0A',
            'gakki': gakki,
            'kamoku_kbn': '',
            'keyword': '',
            'kamokunm': '',
            'kyokannm_kanji': '',
            'kyokannm_kana': '',
            'k_s_cd': '',
            'nenji': '',
            'yobi': '',
            'jigen': '',
            'disp_cnt': '200',}
    headers = {'User-Agent': 'Mozilla/5.0(Windows;U;Windows NT 5.1;rv:1.7.3) Gecko/20041001Firefox/0.10.1'}
    request = session.post(action, data=data, allow_redirects=True, headers=headers)
    return request

## Crawl the result of search
def search_results(html, session):
    print("Crawling the results of search...")
    soup = BeautifulSoup(html)
    crawled = []
    results = []
    while(True):
        pages = []
        for a in soup.find_all('a'):
            if a.attrs['href'].find('s_no') != -1:
                pages.append(root + a.attrs['href'])
            elif a.attrs['href'].startswith('/utask/campus?view=view.syllabus.refer.search'):
                results.append(root + a.attrs['href'])
        url = pages[-1]
        request = s.get(url)
        soup = BeautifulSoup(request.text)
        if url.split('s_no=')[1] in crawled:
            break
        else:
            crawled.append(url.split('s_no=')[1])
    return results

def scrape_syllabus(link, session):
    request = session.get(link)
    soup = BeautifulSoup(request.text)
    titles = []
    contents = []
    for th in soup.find_all('th', attrs={'class': 'syllabus-normal'}):
        if th:
            titles.append(th.get_text(strip=True))

        idx = th.parent.find_all('th').index(th) # scraping table index
        if th.next_sibling.next_sibling == None:
            continue
        elif th.next_sibling.next_sibling.name == 'th':
            contents.append(th.parent.next_sibling.next_sibling.find_all('td')[idx].get_text(strip=True))
        else:
            contents.append(th.next_sibling.next_sibling.get_text(strip=True))
    return dict(zip(titles, contents))



# start Crawling
import requests
import getpass
import sys
if __name__ == "__main__":
    print("Starting Crawling https://zkyomu.c.u-tokyo.ac.jp...")
    username = input("ID:")
    password = getpass.getpass("パスワード:")
    code_number = getpass.getpass("暗証番号:")
    s = requests.session()
    r = login_utaskweb(session=s,
                       username=username,
                       password=password,
                       code_number=code_number)
    r = meta_refresh(html=r.text, session=s)
    if r is None:
        print("Login Failed. Please check your input")
        sys.exit()

    r = syllabus_link(html=r.text, session=s)
    r = search_syllabus(html=r.text, session=s)
    results = search_results(html=r.text, session=s)

    data = []
    print("Scraping the syllabus...")
    for result in results:
        data.append(scrape_syllabus(link=result, session=s))

    import csv
    filename = "out.csv"
    with open(filename, 'w', encoding="utf-16") as f:
        w = csv.DictWriter(f, data[0].keys())
        w.writeheader()
        for d in data:
            w = csv.DictWriter(f, d.keys())
            w.writerow(d)
    f.close()
