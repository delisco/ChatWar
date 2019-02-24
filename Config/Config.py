import ConfigParser
import os

class Config:
    def __init__(self):
        pass

    def get(self, section, key):
        config = ConfigParser.ConfigParser()
        file_root = os.path.dirname(__file__)
        path = os.path.join(file_root, 'Config.conf')
        config.read(path)
        return config.get(section, key)