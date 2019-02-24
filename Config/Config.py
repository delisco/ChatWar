import configparser
import os

class Config:
    def __init__(self):
        pass

    def get(self, section, key):
        config = configparser.ConfigParser()
        file_root = os.path.abspath(__file__)
        path = os.path.join(file_root, 'Config.ini')
        config.read(path)
        print(config.sections())
        return config['chatWar']['CHANNEL_ACCESS_TOKEN']