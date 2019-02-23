import hug
import Search.googleSearch as googleSearch
import json

@hug.post('/googleSearch')
def googleSearchFunction(body):
    return {
        'message': googleSearch.googleSearch(body['keyword'])
    }

if __name__ == '__main__':
    print('test')