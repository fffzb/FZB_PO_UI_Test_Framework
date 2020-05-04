from selenium import webdriver
from common import config_utils
from common.base_page import BasePage


def set_driver():
    driver = webdriver.Chrome(executable_path=config_utils.Config.chrome_path)
    base_page = BasePage(driver)
    driver.implicitly_wait(10)
    base_page.set_max_window()
    url = config_utils.Config.zantao_url
    base_page.open_url(url)
    return driver


if __name__ == '__main__':
    set_driver()