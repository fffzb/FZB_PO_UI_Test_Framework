import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_info.login_page import LoginPage
from common.log_utils import logger

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')

class MainPage:
    def __init__(self):
        login_page = LoginPage()
        login_page.input_username('admin')
        login_page.input_password('fzb123456')
        login_page.click_login()
        self.driver = login_page.driver
        self.companyname_showbox = self.driver.find_element(By.XPATH,'//h1[@id="companyname"]')
        self.myzone_menu = self.driver.find_element(By.XPATH,'//li[@data-id="my"]')
        self.product_menu = self.driver.find_element(By.XPATH,'//li[@data-id="product"]')
        self.username_showspan = self.driver.find_element(By.XPATH,'//span[@class="user-name"]')

    def get_companyname(self,username): #获取公司名称
        value = self.companyname_showbox.get_attribute('title')
        return value
    def goto_myzone(self,password): #进入我的地盘菜单
        value = self.myzone_menu.click()
        return value
    def goto_product(self): #进入产品菜单
        value = self.product_menu.click()
        return value
    def get_username(self): #获取用户名称
        value = self.username_showspan.text
        logger.info('获取用户名成功，用户名是：'+ str(value))
        return value

if __name__ == '__main__':
    main_page = MainPage()
    username = main_page.get_username()
    print(username)