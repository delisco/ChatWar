import _baidu
import _bing
from enum import Enum
from imagesoup import ImageSoup as _google

# this is interface
class ImgEngine():
    def getImage(self,keyWord,limit):
        pass

# this is factory's
class Google():
    def getImage(self,keyWord,limit):
        GoogleCrawler = _google()
        images = GoogleCrawler.search(keyWord, n_images=limit)
        result = []
        for image in images:
            result.append(image.URL)
        return result

class Baidu():
    def getImage(self,keyWord,limit):
        BaiduCrawler = _baidu.BaiduCrawler()
        return BaiduCrawler.get_images(keyWord, limit) 


class Bing():
    def getImage(self,keyWord,limit):
        return _bing.fetch_images_from_keyword(keyWord, limit)


class ImgHandler():
    def getImageEngine(self,Engine):
        if not isinstance(Engine, Enum):
            raise Exception('Please input Engine enum')
        if not Engine.has_value(Engine.value):
            raise Exception('Not Support this image engine')
        if Engine== Engine.google :  
            return Google()  
        elif Engine== Engine.baidu :  
            return Baidu()
        elif Engine == Engine.bing :
            return Bing()

class Engine(Enum):
    google = 1
    baidu = 2
    bing = 3
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)

if  __name__ == "__main__" :  
 
    ImgHandler = ImgHandler()  
    s = ImgHandler.getImageEngine(Engine.bing)  
    keyWord = 'cat'
    limit = 5
    print(s.getImage(keyWord,limit))