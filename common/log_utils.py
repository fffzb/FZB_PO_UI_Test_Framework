import logging
import os
from common.config_utils import Config
class LogUtils:
    def __init__(self,logfile_path=Config.get_log_path):
        self.logfile_path = logfile_path
        self.logger = logging.getLogger()
        self.logger.setLevel(level=logging.INFO)
        file_log = logging.FileHandler(self.logfile_path)
        formatter = logging.Formatter('file:%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)
    def info(self,message):
        self.logger.info(message)
    def error(self,message):
        self.logger.error(message)
logger = LogUtils()
if __name__ == '__main__':
    log_utils = LogUtils()
    log_utils.info('hhh')