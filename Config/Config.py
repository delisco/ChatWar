import configparser
import os

CONFIG_PATH = 'Config/Config.conf'

class Config:
    def __init__(self):
        pass

    def get(self, section, key):
        config = configparser.ConfigParser(CONFIG_PATH)
        file_root = os.path.dirname(__file__)
        path = os.path.join(file_root, 'Config.conf')
        config.read(path)
        return config.get(section, key)