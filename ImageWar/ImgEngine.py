import _google
import _baidu
import _bing

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
    def getImageEngine(self,name):
        if name== "google" :  
            return Google()  
        elif name== "baidu" :  
            return Baidu()
        elif name =="bing" :
            return Bing()
        else:
            raise Exception('Not Support this image engine')

if  __name__ == "__main__" :  
     
    engineName= 'google'  
    ImgHandler = ImgHandler()  
    s = ImgHandler.getImageEngine(engineName)  
    keyWord = 'cat'
    limit = 5
    s.getImage(keyWord,limit)  