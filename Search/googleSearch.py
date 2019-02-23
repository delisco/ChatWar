import sys
import requests
import hug
from urllib.parse import unquote
from bs4 import BeautifulSoup


def parseUrl(url):
    tempString = " " + url[7:]
    unneededParam = '&sa'
    unneededParamIndex = tempString.index(unneededParam)
    urlResult = tempString[:unneededParamIndex]
    result = unquote(urlResult)
    return result

def googleSearch(keyword):
    # keyword = sys.argv
    google_url = 'https://www.google.com.tw/search'
    # search param
    my_params = {'q': keyword[1]}
    req = requests.get(google_url, params=my_params)
    response = ''
    # Check status code
    if req.status_code == requests.codes.ok:
        bsParsingResult = BeautifulSoup(req.text, "html.parser")
        # print(bsParsingResult)
        # CSS selector
        selectionResult = bsParsingResult.select('div.g > h3.r > a[href^="/url"]')
        for idx, item in enumerate(selectionResult):
            print(idx)
            response += str(idx) + '\n'
            # title
            print("標題：" + item.text)
            response += "標題：" + item.text + '\n'
            # url
            url = item.get('href')
            urlResult = parseUrl(url)
            print("網址：" + urlResult)
            response += "網址：" + urlResult + '\n'
            if idx == 3:
                break
        return response
    else:
        print(req.status_code)


if __name__ == '__main__':
    googleSearch()

# 目前可用的查詢參數
# num = 設定一頁內顯示的搜索結果
# lr = 限制語言
# cr = 限制Server地點
# hl = 限制Google搜索介面的語言
# as_qdr = 限制時間
