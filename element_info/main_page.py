import os
from common.login import test_login
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils
from common.config_utils import Config
from common import set_driver

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # self.companyname_showbox =  {'element_name':'公司名称',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//h1[@id="companyname"]',
        #                           'timeout':5}
        # self.myzone_menu =  {'element_name':'我的地盘菜单',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//li[@data-id="my"]',
        #                           'timeout':5}
        # self.product_menu = {'element_name': '产品菜单',
        #                     'locator_type': 'xpath',
        #                     'locator_value': '//li[@data-id="product"]',
        #                     'timeout': 5}
        # self.username_showbox = {'element_name': '用户按钮',
        #                     'locator_type': 'xpath',
        #                     'locator_value': '//span[@class="user-name"]',
        #                     'timeout': 5}
        elements = ElementdataUtils('main_page').get_element_info()
        self.companyname_showbox = elements['companyname_showbox']
        self.myzone_menu = elements['myzone_menu']
        self.product_menu = elements['product_menu']
        self.username_showbox = elements['username_showbox']
        self.story_button = elements['story_button']
        self.plan_button = elements['plan_button']
        self.release_button = elements['release_button']
        self.roadmap_button = elements['roadmap_button']
        self.project_button = elements['project_button']
        self.dynamic_button = elements['dynamic_button']
        self.doc_button = elements['doc_button']
    def get_companyname(self): #获取公司名称
        self.get_attribute(self.companyname_showbox)
    def goto_myzone(self): #进入我的地盘菜单
        self.click(self.myzone_menu)
    def goto_product(self): #进入产品菜单
        self.click(self.product_menu)
    def get_username(self): #获取用户名称
        text = self.get_text(self.username_showbox)
        return text
    def goto_story(self):
        self.click(self.story_button)
    def goto_plan(self):
        self.click(self.plan_button)
    def goto_release(self):
        self.click(self.release_button)
    def goto_roadmap(self):
        self.click(self.roadmap_button)
    def goto_project(self):
        self.click(self.project_button)
    def goto_dynamic(self):
        self.click(self.dynamic_button)
    def goto_doc(self):
        self.click(self.doc_button)
if __name__ == '__main__':
    driver = set_driver.set_driver()
    test_login(Config.zantao_url, Config.user_name, Config.password,driver)
    main_page = MainPage(driver)
    main_page.goto_myzone()
    main_page.goto_product()
    main_page.goto_story()
    main_page.goto_plan()
    main_page.goto_release()
    main_page.goto_roadmap()
    main_page.goto_project()
    main_page.goto_dynamic()
    main_page.goto_doc()