from selenium import webdriver
import time

class CommonDriver(object):
    """docstring for CommonDriver"""
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def open_url(self,url):
        self.driver.get(url)

    def locat_element(self,locat_type,expr):
        el = None
        if locat_type == 'id':
            el = self.driver.find_element_by_id(expr)
        elif locat_type == 'name':
            el = self.driver.find_element_by_name(expr)
        elif locat_type == 'class_name':
            el = self.driver.find_element_by_class_name(expr)
        elif locat_type == 'tag_name':
            el = self.driver.find_element_by_tag_name(expr)
        elif locat_type == 'link_text':
            el = self.driver.find_element_by_link_text(expr)
        elif locat_type == 'partial_text':
            el = self.driver.find_element_by_partial_link_text(expr)
        elif locat_type == 'xpath':
            el = self.driver.find_element_by_xpath(expr)
        elif locat_type == 'css_selector':
            el = self.driver.find_element_by_css_selector(expr)
        return el


    def click(self,locat_type,expr):
        el = self.locat_element(locat_type,expr)
        el.click()

    def input_data(self,locat_type,expr,data):
        el = self.locat_element(locat_type,expr)
        time.sleep(0.5)
        el.send_keys()

    def get_text(self,locat_type,expr):
        el = self.locat_element(locat_type,expr)
        return el.text()
    
    def get_attr(self,locat_type,expr,attr):
        el = self.locat_element(locat_type,expr)
        value = el.get_attribute(attr)
        return value
    def quit(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    driver = CommonDriver()
    driver.open_url('http://www.baidu.com')
    driver.input_data('id','kw','selenium')
    driver.click('id','su')
    driver.quit()

