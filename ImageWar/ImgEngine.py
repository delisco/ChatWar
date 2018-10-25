import _google
import _baidu
import _bing
from enum import Enum

# this is interface
class ImgEngine():
    def getImage(self,keyWord,limit):
        pass

# this is factory's
class Google():
    def getImage(self,keyWord,limit):
        # 說明文件 https://github.com/hardikvasa/google-images-download
        response = _google.googleimagesdownload()   #class instantiation
        arguments = {"keywords":keyWord,"limit":1,"print_urls":True}   #creating list of arguments
        paths = response.download(arguments)   #passing the arguments to the function
        print(paths)   #printing absolute paths of the downloaded images
        pass

class Baidu():
    def getImage(self,keyWord,limit):
        print('call Baidu api')
        BaiduCrawler = _baidu.BaiduCrawler(0.05)  # 抓取延迟为 0.05
        # crawler.start('美女', 10, 2)  # 抓取关键词为 “美女”，总数为 10 页（即总共 10*60=60 张），开始页码为 2
        BaiduCrawler.start(keyWord, 1, 1)  # 抓取关键词为 keyword，总数为 1 页（即总共 1*60=60 张），起始抓取的页码为 1
        pass

class Bing():
    def getImage(self,keyWord,limit):
        print('call Bing api')
        # 限制十張圖
        limit = 10
        keyword = 'cat'
        BingCrawler = _bing.fetch_images_from_keyword(keyword, limit)
        pass


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