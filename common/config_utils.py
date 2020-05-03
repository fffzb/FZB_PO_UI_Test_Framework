import os
import configparser

current_path = os.path.dirname(__file__)
cfpath = os.path.join(current_path, '../conf/config.ini')
class ConfigUtils:
    def __init__(self,config_path=cfpath):
        self.__config_path = config_path
        self.__conf = configparser.ConfigParser()
        self.__conf.read(self.__config_path,encoding='utf-8')
    def read_ini(self,sec,option):
        value = self.__conf.get(sec,option)
        return value
    @property
    def get_excel_path(self):
        value = self.read_ini('default','excel_path')
        return value
    @property
    def get_log_path(self):
        value = self.read_ini('default', 'log_path')
        return value
Config = ConfigUtils()

if __name__ == '__main__':
    config_u = ConfigUtils()
    print(config_u.get_excel_path)
