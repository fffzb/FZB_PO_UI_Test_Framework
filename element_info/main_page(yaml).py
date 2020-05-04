from common import login
from common.config_utils import Config
from common import set_driver
from common.base_page import BasePage
from common.element_yaml_utills import ElementYamlData



class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        elements = ElementYamlData('main_page').read_yaml()
        self.company_show_box = elements['company_show_box']
        self.my_zone_menu = elements['my_zone_menu']
        self.product_menu = elements['product_menu']
        self.username_show_span = elements['username_show_span']
        self.logout_menu = elements['logout_menu']
        self.zentao_vaesion = elements['zentao_vaesion']
        self.forget_password_menu = elements['forget_password_menu']
        self.forget_password_original_password = elements['forget_password_original_password']
        self.forget_password_password1 = elements['forget_password_password1']
        self.forget_password_password2 = elements['forget_password_password2']
        self.forget_password_save_button = elements['forget_password_save_button']

    def get_company_name(self):
        value = self.get_attribute(self.company_show_box)
        return value

    def goto_myzone(self):
        self.click(self.my_zone_menu)

    def goto_product(self):
        self.click(self.product_menu)

    def get_user_name(self):
        text = self.get_text(self.username_show_span)
        return text

    def get_zentao_version(self):
        zantao_version = self.get_text(self.zentao_vaesion)
        return zantao_version

    def goto_forget_password(self):
        self.click(self.username_show_span)
        self.click(self.forget_password_menu)

    def change_password(self, original_password, password1, password2):
        self.switch_to_frame('iframe-triggerModal')
        self.input(self.forget_password_original_password, original_password)
        self.input(self.forget_password_password1, password1)
        self.input(self.forget_password_password2, password2)
        self.click(self.forget_password_save_button)
        self.switch_to_default_content()

    def logout(self):
        self.click(self.username_show_span)
        self.click(self.logout_menu)


if __name__ == '__main__':
    driver = set_driver.set_driver()
    login.test_login(Config.zantao_url, Config.user_name, Config.password, driver)
    main_page = MainPage(driver)
    company_name = main_page.get_company_name()
    main_page.goto_myzone()
    main_page.goto_product()
    username_text = main_page.get_user_name()
    zantao_version = main_page.get_zentao_version()
    main_page.goto_forget_password()
    main_page.change_password(Config.password, Config.password, Config.password)
    main_page.logout()
    driver.close()