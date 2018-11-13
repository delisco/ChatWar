import sys
import requests
from bs4 import BeautifulSoup


def stackoverflowSearch():
    keyword = sys.argv
    stackoverflow_url = 'https://stackoverflow.com/search'
    # search param
    my_params = {'q': keyword[1]}
    req = requests.get(stackoverflow_url, params=my_params)
    # Check status code
    if req.status_code == requests.codes.ok:
        bsParsingResult = BeautifulSoup(req.text, "html.parser")
        # print(bsParsingResult)
        # CSS selector
        # selectionResult = bsParsingResult.select('div.result-link > h3 > a[href^="/questions"]')
        selectionResult = bsParsingResult.select('a.question-hyperlink')
        for idx, item in enumerate(selectionResult):
            print(idx)
            # title
            print("標題：" + item.text)
            # url
            url = 'https://stackoverflow.com' + item.get('href')
            print("網址：" + url)
            if idx == 3:
                break
    else:
        print(req.status_code)

stackoverflowSearch()