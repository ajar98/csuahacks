from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import json
import time

CHROMEDRIVER_PATH = 'chromedriver' 
SLADER_ENDPOINT = 'https://www.slader.com/'
SLADER_SEARCH_ENDPOINT = 'search/?search_query='
TEXTBOOK_SEARCH_RESULTS_XPATH = '//section[@class="type-results textbook_index"]/article[1]/section' 
PAGE_NUMBER_INPUT_XPATH = '/html/body/div[3]/section[3]/section[1]/nav[2]/form/input' 
PAGE_NUMBER_GO_BUTTON_XPATH = '/html/body/div[3]/section[3]/section[1]/nav[2]/form/a'
CHAPTER_DROPDOWN_XPATH = '//article[@class="toc"]/section[{0}]'
EXERCISES_PAGE_NUMBER_XPATH = '//article[@class="toc"]/section[{0}]//tr[{0}]/td[4]'

class SladerClient():

    def __init__(self, textbook_name):
        self.driver = webdriver.Chrome(CHROMEDRIVER_PATH)
        self.driver.get('{0}{1}{2}'.format(SLADER_ENDPOINT, SLADER_SEARCH_ENDPOINT, textbook_name))
        time.sleep(5)
        self.textbook_url = '{0}{1}'.format(
            SLADER_ENDPOINT,
            self.driver.find_element_by_xpath(TEXTBOOK_SEARCH_RESULTS_XPATH).get_attribute('data-url'))
        self.driver.get(self.textbook_url)

    def get_answers_by_page(self, page_number):
        self.driver.find_element_by_xpath(PAGE_NUMBER_INPUT_XPATH).send_keys(str(page_number))
        self.driver.find_element_by_xpath(PAGE_NUMBER_GO_BUTTON_XPATH).click()

    def get_page_number_by_section(self, chapter, section):
        self.driver.find_element_by_xpath(CHAPTER_DROPDOWN_XPATH.format(chapter)).click()
        return self.driver.find_element_by_xpath(EXERCISES_PAGE_NUMBER_XPATH.format(chapter, section)).get_attribute('innerHTML')

sc = SladerClient('Linear Algebra and Its Applications, 4th Edition')
print(sc.get_answers_by_page(97))
