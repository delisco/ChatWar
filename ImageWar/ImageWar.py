import ImgEngine

class ImgWar():
    def __init__(self):
        return
    def printtext(self):
        print('hello world')
    
    def getImg(self, engineName,keyWord,limit = 5):
        if not keyWord:
            raise Exception('please input keyWords')
        engine = ImgEngine.ImgHandler().getImageEngine(engineName)
        engine.getImage(keyWord,limit)




if __name__ == '__main__':
    imgWar = ImgWar()
    keyWord = 'cat'
    limit = 5
    result = imgWar.getImg(ImgEngine.Engine.google,keyWord,limit)
    print(result)
    # imgWar.getImg('baidu',keyWord,limit)


