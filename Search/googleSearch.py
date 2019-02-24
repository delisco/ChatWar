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

def generateResponse(selectionResult):
    response = ''
    for idx, item in enumerate(selectionResult):
        response += '#' + str(idx + 1) + '\n'
        response += '標題：' + item.text + '\n'
        url = item.get('href')
        urlResult = parseUrl(url)
        response += '網址：' + urlResult + '\n'
        if idx == SEARCH_AMOUNT:
            break
    return response

def googleSearch(keyword):
    google_url = 'https://www.google.com.tw/search'
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
