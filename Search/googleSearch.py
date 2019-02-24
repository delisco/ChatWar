import sys
import requests
import hug
from urllib.parse import unquote
from bs4 import BeautifulSoup

SEARCH_AMOUNT = 3

def parseUrl(url):
    tempString = ' ' + url[7:]
    unneededParam = '&sa'
    unneededParamIndex = tempString.index(unneededParam)
    urlResult = tempString[:unneededParamIndex]
    result = unquote(urlResult)
    return result

def generateResultText(textType, content):
    if textType == 'idx':
        return '#' + str(content + 1) + '\n'
    elif textType == 'title':
        return '標題：' + content + '\n'
    elif textType == 'url':
        return '網址：' + content + '\n'

def generateResponse(selectionResult):
    response = ''
    for idx, item in enumerate(selectionResult):
        response += generateResultText('idx', idx)
        # title
        response += generateResultText('title', item.text)
        # url
        url = item.get('href')
        urlResult = parseUrl(url)
        response += generateResultText('url', urlResult)
        if idx == SEARCH_AMOUNT:
            break
    return response

def googleSearch(keyword):
    google_url = 'https://www.google.com.tw/search'
    # search param
    my_params = {'q': keyword}
    req = requests.get(google_url, params=my_params)
    # Check status code
    if req.status_code == requests.codes.ok:
        bsParsingResult = BeautifulSoup(req.text, 'html.parser')
        # CSS selector
        selectionResult = bsParsingResult.select('div.g > h3.r > a[href^="/url"]')
        return generateResponse(selectionResult)
    else:
        print(req.status_code)


if __name__ == '__main__':
    googleSearch('test')

# 目前可用的查詢參數
# num = 設定一頁內顯示的搜索結果
# lr = 限制語言
# cr = 限制Server地點
# hl = 限制Google搜索介面的語言
# as_qdr = 限制時間
