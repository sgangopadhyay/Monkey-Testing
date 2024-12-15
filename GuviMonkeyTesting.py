from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import random


class Locators:

    SCROLLING_POINT = "//a[text()='Privacy Policy']"
    FOOTER_URL = "//li[@class='Linklist__Item']/a[@class='Link Link--primary']"

class MonkeyTesting(Locators):

    def __init__(self, url):

        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.EXCEPTIONS = (NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException)


    def monkey_testing(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            self.driver.implicitly_wait(10)
            action = ActionChains(self.driver)
            scrolling_point = self.driver.find_element(by=By.XPATH, value=self.SCROLLING_POINT)
            action.move_to_element(scrolling_point).perform()
            footer_list = self.driver.find_elements(by=By.XPATH, value=self.FOOTER_URL)

            """Fetch the URL from the List"""
            footer_url = []
            for data in footer_list:
                footer_url.append(data.get_attribute('href'))
            print(footer_url)

            """Monkey Testing"""
            random_data = random
            for data in range(len(footer_url)):
                if data in random_data:
                    self.driver.find_element(by=By.XPATH, value=self.FOOTER_URL).click()
                    print(self.driver.current_url)
                    self.driver.back()
                    return self.monkey_testing()


        except self.EXCEPTIONS as error:
            print(error)
        finally:
            self.driver.quit()

if __name__ == "__main__":

    url = "https://sevengramscaffe.com/"

    testing = MonkeyTesting(url)

    testing.monkey_testing()
