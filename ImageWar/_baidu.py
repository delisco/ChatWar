#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import urllib
import json
import socket
import urllib.request
import urllib.parse
import urllib.error
# 设置超时
import time

timeout = 5
socket.setdefaulttimeout(timeout)


class BaiduCrawler:
    # 睡眠时长
    __time_sleep = 0.1
    __counter = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    # 获取图片url内容等
    # t 下载图片时间间隔
    def __init__(self, t=0.05):
        self.time_sleep = t

    # 获取后缀名
    def get_suffix(self, name):
        m = re.search(r'\.[^\.]*$', name)
        if m.group(0) and len(m.group(0)) <= 5:
            return m.group(0)
        else:
            return '.jpeg'

    # 获取referrer，用于生成referrer
    def get_referrer(self, url):
        par = urllib.parse.urlparse(url)
        if par.scheme:
            return par.scheme + '://' + par.netloc
        else:
            return par.netloc

    # 开始获取
    def get_images(self, word,limit):
        search = urllib.parse.quote(word)
        # pn 開始搜尋起點
        pn = 0
        result = []
        while len(result) < limit:

            url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + search + '&cg=girl&pn=' + str(
                pn) + '&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
            # 设置header防ban
            try:
                time.sleep(self.time_sleep)
                req = urllib.request.Request(url=url, headers=self.headers)
                page = urllib.request.urlopen(req)
                rsp = page.read().decode('unicode_escape')
            except UnicodeDecodeError as e:
                print(e)
                print('-----UnicodeDecodeErrorurl:', url)
                return result
            except urllib.error.URLError as e:
                print(e)
                print("-----urlErrorurl:", url)
                return result
            except socket.timeout as e:
                print(e)
                print("-----socket timout:", url)
                return result
            else:
                # 解析json
                try:
                    rsp_data = json.loads(rsp)
                except:
                    return result
                for image in rsp_data['imgs']:
                    if len(result) >= limit:
                        return result
                    result.append(image['objURL'])
                # 读取下一页
                print("下载下一页")
                pn += 60
            finally:
                page.close()
        print("爬取任务结束")
        return result

if __name__ == '__main__':
    BaiduCrawler = BaiduCrawler()
    result = BaiduCrawler.get_images('aasgasgasgjsljgsalkgjaslgjasl;gjas;lgjal;sjglasjglsajgla;gj;sdfasgasgasgasgasgasgasg', 3) 
    print(result)
    print(len(result))

