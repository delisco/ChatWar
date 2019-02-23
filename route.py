import hug
import Search.googleSearch as googleSearch
import json
import linebot

class googleSearchResponse:
    replyToken = ''
    type = ''
    timestamp = ''
    source = None # type userId
    message = None # id type text

@hug.post('/googleSearch')
def googleSearchFunction(body):
    return {
        # 'message': googleSearch.googleSearch(body['keyword'])
        'message': 'test'
    }

if __name__ == '__main__':
    print('test')