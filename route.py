import hug
import Search.googleSearch as googleSearch

@hug.get()
def googleSearchFunction(keyword: hug.types.text):
    print(keyword)
    return {
        'message': googleSearch.googleSearch(keyword)
    }

if __name__ == '__main__':
    print('test')