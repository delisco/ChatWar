import ImgEngine

class ImgWar():
    def __init__(self):
        return
    def printtext(self):
        print('hello world')
    
    def getImg(self, engineName,keyWord):
        if not keyWord:
            raise Exception('please input keyWords')
        engine = ImgEngine.ImgHandler().getImageEngine(engineName)
        engine.getImage(keyWord)


if __name__ == '__main__':
    imgWar = ImgWar()
    keyWord = 'cat'
    imgWar.getImg('google',keyWord)
    # imgWar.getImg('baidu',keyWord)


