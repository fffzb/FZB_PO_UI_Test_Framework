import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    #浏览器操作 --> 二次封装
    def open_url(self,url):
        self.driver.get(url)
        logger.info('打开url地址 %s' % url)
    def set_max_window(self):
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')
    def set_min_window(self):
        self.driver.minimize_window()
        logger.info('设置浏览器最小化')
    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新')
    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题，标题是：%s' % value)
        return value
    def close(self):
        self.driver.close()
    #元素相关的封装
    #element_info = {'element_name':'用户名输入框','locator_type':'xpath','locator_value':'//input[@id="account"]','timeout':5}
    def find_element(self,element_info):
        locator_element_name = element_info['element_name']
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'CLASS_NAME':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'XPATH':
            locator_type = By.XPATH
        element = WebDriverWait(self.driver, int(locator_timeout)) \
            .until(lambda x: x.find_element(locator_type, locator_value_info))
        logger.info('%s：  元素识别成功' % locator_element_name)

        return element

    def click(self,element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s]元素进行点击操作成功' % element_info['element_name'])
    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容：%s' % (element_info['element_name'],content))
    # 获取属性值
    def get_attribute(self,element_info):
        element = self.find_element(element_info)
        value = element.get_attribute('title')
        logger.info('[%s]属性值为:%s' % (element_info['element_name'],value))
    # 获取文本信息
    def get_text(self,element_info):
        text = self.find_element(element_info).text
        logger.info('[%s]对象的文本信息为:%s' % (element_info['element_name'], text))
    #frame处理
    #切换到frame
    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)
        time.sleep(2)
    #切换至最外层frame
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        time.sleep(2)
    # alert处理
    def switch_to_alert(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        logger.info('弹窗提示值为：  %s' % text)
    # 鼠标右击
    def mouse_right_click(self, element_info):
        mouse = ActionChains(self.driver)
        element = self.find_element(element_info)
        mouse.context_click(element).perform()
    # 键盘常用操作
    def key_board_operate(self, element, operate):
        if operate == 'enter':
            element.send_keys(Keys.ENTER)
        elif operate == 'up':
            element.send_keys(Keys.UP)
        elif operate == 'dowm':
            element.send_keys(Keys.DOWN)
        elif operate == 'left':
            element.send_keys(Keys.LEFT)
        elif operate == 'right':
            element.send_keys(Keys.RIGHT)