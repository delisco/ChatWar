#!/usr/bin/env python3
import os, urllib.request, re, threading, posixpath, urllib.parse, argparse, socket, time, hashlib, pickle, signal, imghdr

#config
output_dir = './bing' #default output dir
adult_filter = True #Do not disable adult filter by default
socket.setdefaulttimeout(2)

in_progress = tried_urls = []
image_md5s = {}
urlopenheader={ 'User-Agent' : 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}

def fetch_images_from_keyword(keyword: str, limit: int):
    current = 0
    last = ''
    adlt = '' # 成人內容
    while True:
        request_url='https://www.bing.com/images/async?q=' + urllib.parse.quote_plus(keyword) + '&first=' + str(current) + '&count=35&adlt=' + adlt
        request=urllib.request.Request(request_url,None,headers=urlopenheader)
        response=urllib.request.urlopen(request)
        html = response.read().decode('utf8')
        links = re.findall('murl&quot;:&quot;(.*?)&quot;',html)
        try:
            if links[-1] == last:
                return
            for index, link in enumerate(links):
                if limit is not None and current + index >= limit:
                    return
                print(link)
                current += 1
            last = links[-1]
        except IndexError:
            print('No search results for "{0}"'.format(keyword))
            return
        time.sleep(0.1)

if __name__ == "__main__":
    # 限制十張圖
    limit = 10
    keyword = 'cat'
    fetch_images_from_keyword(keyword, limit)
