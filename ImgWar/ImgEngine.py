# this is interface
class ImgEngine():
    def getImage(self):
        pass

# this is factory's
class Google():
    def getImage(self):
        print('call Google api')
        pass

class Baidu():
    def getImage(self):
        print('call Baidu api')
        pass


class ImgHandler():
    def getImageEngine(self,name):
        if name== "google" :  
            return Google()  
        elif name== "baidu" :  
            return Baidu()
        else:
            raise Exception('Not Support this image engine')

if  __name__ == "__main__" :  
    print (" please input \"ImageEngine\" : ")  
    engineName= input()  
    ImgHandler = ImgHandler()  
    s = ImgHandler.getImageEngine(engineName)  
    s.getImage()  