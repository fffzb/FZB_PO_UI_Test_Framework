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
        return self.__conf.get(sec,option)

    @property
    def get_log_path(self):
        return self.read_ini('log', 'log_path')

    @property
    def zantao_url(self):
        return self.read_ini("zentao", "zentao_url")

    @property
    def user_name(self):
        return self.read_ini("user", "user_name")

    @property
    def password(self):
        return self.read_ini("user", "password")

    @property
    def chrome_path(self):
        return self.read_ini("driver", "chrome_path")
    @property
    def url(self):
        url_value = self.read_ini("default", "url")
        return url_value
    @property
    def driver_path(self):
        driver_path_value = self.read_ini("default", "driver_path")
        return driver_path_value
    @property
    def driver_name(self):
        driver_name_value = self.read_ini('default','driver_name')
        return driver_name_value
Config = ConfigUtils()

if __name__ == '__main__':
    config = ConfigUtils()
    print(config.driver_name)
