"""
Program Description : Python program to perform Monkey Testing
Programmer : Suman Gangopadhyay
Email ID : linuxgurusuman@gmail.com
Date : 1-Jan-2025
Version : 1.0
Code Library : Selenium
Prerequisites : Python, Selenium, ChromeDriver
Caveats : None
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import random

# Locators Class
class Locators:

    SCROLLING_POINT = "//a[text()='Privacy Policy']"
    FOOTER_URL = "//li[@class='Linklist__Item']/a[@class='Link Link--primary']"

# Monkey Testing Class
class MonkeyTesting(Locators):
    
    """
    DESCRIPTION : Class to perform Monkey Testing
    """

    def __init__(self, url):

        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.EXCEPTIONS = (TimeoutException, NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency = 5, ignored_exceptions = self.EXCEPTIONS)


    def monkey_testing(self):
        """
        DESCRIPTION : Method to perform Monkey Testing
        """

        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            action = ActionChains(self.driver)
            scrolling_point = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.SCROLLING_POINT)))
            action.move_to_element(scrolling_point).perform()
            footer_list = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.FOOTER_URL)))
            footer_count = len(footer_list)
            
            """Fetch URLs from Footer"""
            footer_url = []
            for data in footer_list:
                footer_url.append(data.get_attribute('href'))
            
            
            """Monkey Testing"""
            run_count = 0
            for random_url in range(footer_count):
                self.driver.get(footer_url[random_url])
                run_count = run_count + 1
                sleep(random())
                self.driver.back()
                print(f"Running the Test: {run_count} & URL: {footer_url[random_url]}")
                sleep(random())
           

        except self.EXCEPTIONS as error:
            print(error)
        finally:
            self.driver.quit()

# Main Function

if __name__ == "__main__":

    url = "https://sevengramscaffe.com/"

    testing = MonkeyTesting(url)

    testing.monkey_testing()
