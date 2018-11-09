import requests
from urllib.parse import unquote
from bs4 import BeautifulSoup


def parseUrl(url):
    tempString = " " + url[7:]
    unneededParam = '&sa'
    unneededParamIndex = tempString.index(unneededParam)
    urlResult = tempString[:unneededParamIndex]
    Result = unquote(urlResult)
    return Result


def googleSearch(keyword):
    google_url = 'https://www.google.com.tw/search'
    # search param
    my_params = {'q': keyword}
    req = requests.get(google_url, params=my_params)
    # Check status code
    if req.status_code == requests.codes.ok:
        bsParsingResult = BeautifulSoup(req.text, "html.parser")
        # print(bsParsingResult)
        # CSS selector
        selectionResult = bsParsingResult.select('div.g > h3.r > a[href^="/url"]')
        for idx, item in enumerate(selectionResult):
            print(idx)
            # title
            print("標題：" + item.text)
            # url
            url = item.get('href')
            urlResult = parseUrl(url)
            print("網址：" + urlResult)
            if idx == 3:
                break
    else:
        print(req.status_code)


keyword = input('請輸入關鍵字 :')
googleSearch(keyword)

# 目前可用的查詢參數
# num = 設定一頁內顯示的搜索結果
# lr = 限制語言
# cr = 限制Server地點
# hl = 限制Google搜索介面的語言
# as_qdr = 限制時間