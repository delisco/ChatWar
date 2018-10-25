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
        print(result)

class Baidu():
    def getImage(self,keyWord,limit):
        print('call Baidu api')
        BaiduCrawler = _baidu.BaiduCrawler(0.05)  # 抓取延迟为 0.05
        # crawler.start('美女', 10, 2)  # 抓取关键词为 “美女”，总数为 10 页（即总共 10*60=60 张），开始页码为 2
        BaiduCrawler.start(keyWord, 1, 1)  # 抓取关键词为 keyword，总数为 1 页（即总共 1*60=60 张），起始抓取的页码为 1

class Bing():
    def getImage(self,keyWord,limit):
        print('call Bing api')
        # 限制十張圖
        limit = 10
        keyword = 'cat'
        BingCrawler = _bing.fetch_images_from_keyword(keyword, limit)


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
    s = ImgHandler.getImageEngine(Engine.google)  
    keyWord = 'cat'
    limit = 5
    s.getImage(keyWord,limit)  