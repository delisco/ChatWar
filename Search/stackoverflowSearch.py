import requests
from bs4 import BeautifulSoup


def stackoverflowSearch(keyword):
    stackoverflow_url = 'https://stackoverflow.com/search'
    # search param
    my_params = {'q': keyword}
    req = requests.get(stackoverflow_url, params=my_params)
    # Check status code
    if req.status_code == requests.codes.ok:
        bsParsingResult = BeautifulSoup(req.text, "html.parser")
        # print(bsParsingResult)
        # CSS selector
        selectionResult = bsParsingResult.select('div.result-link > h3 > a[href^="/questions"]')
        for idx, item in enumerate(selectionResult):
            print(idx)
            # title
            print("標題：" + item.get('title'))
            # url
            url = 'https://stackoverflow.com' + item.get('href')
            print("網址：" + url)
            if idx == 3:
                break
    else:
        print(req.status_code)


keyword = input('請輸入關鍵字 :')
stackoverflowSearch(keyword)