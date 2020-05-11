import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from common.config_utils import Config
from common.element_data_utils import ElementdataUtils
from common.browser import Browser
from common import set_driver


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.username_inputbox = {'element_name':'用户名输入框',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//input[@id="account"]',
        #                           'timeout':5}
        # self.password_inputbox = {'element_name':'密码输入框',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//input[@name="password"]',
        #                           'timeout':4}
        # self.login_click = {'element_name':'登录按钮',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//button[@id="submit"]',
        #                           'timeout':3}
        elements = ElementdataUtils('login_page').get_element_info()
        self.username_inputbox = elements['username_input_box']
        self.password_inputbox = elements['password_input_box']
        self.login_click = elements['login_button']
    def input_username(self,username): #方法 ==》控件的操作
        self.input(self.username_inputbox,username)
    def input_password(self,password):
        self.input(self.password_inputbox,password)
    def click_login(self):
        self.click(self.login_click)
if __name__ == '__main__':
    driver = Browser().get_driver()
    login_page =  LoginPage(driver)
    login_page.open_url(Config.zantao_url)
    login_page.input_username(Config.user_name)
    login_page.input_password(Config.password)
    login_page.click_login()