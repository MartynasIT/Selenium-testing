import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from locator import *
from element import BasePageElement
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class AcceptElement(BasePageElement):
    locator = (By.ID, 'hs-eu-confirmation-button')


class ContentElement(BasePageElement):
    locator = (By.ID, 'content')


class SearchFieldElement(BasePageElement):
    locator = (By.CLASS_NAME, 's')


class ValidationERRElement(BasePageElement):
    locator = (By.ID, 'validation_message_1_9')


class ValidationErrorEmail(BasePageElement):
    locator = (By.ID, 'validation_message_1_2')


def check_exists_by_id(part, id):
    try:
        part.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True


class MainPage(BasePage):
    AcceptElement = AcceptElement()
    main = ContentElement()
    search_text_element = SearchFieldElement()
    validation_err = ValidationERRElement()
    validation_err_email = ValidationErrorEmail()

    def click_careers(self):
        element_company = self.driver.find_element(*MainPageLocators.COMPANY_BUTTON)
        element_career = self.driver.find_element(*MainPageLocators.CAREERS_BUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_company)
        actions.click(element_career)
        actions.perform()

    def click_search(self):
        element_search = self.driver.find_element(*MainPageLocators.SEARCH_BTN)
        element_search_field = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        actions = ActionChains(self.driver)
        actions.click(element_search)
        actions.click(element_search_field)
        actions.perform()

    def click_submit_search(self):
        self.driver.find_element(*MainPageLocators.SUBMIT_BTN).click()

    def check_search_results(self, main):
        while check_exists_by_id(main, 'load-more'):
            self.driver.find_element_by_id('load-more').click()
            time.sleep(2)
        articles = main.find_elements_by_tag_name('article')
        return len(articles) > 0

    def click_contact_us(self):
        self.driver.find_element(*MainPageLocators.CONTACT_US_BTN).click()

    def click_sign_me(self):
        self.driver.find_element(*MainPageLocators.SIGN_ME_UP_BTN).click()

    def enter_validation_bad(self, text):
        email_element = self.driver.find_element(*MainPageLocators.EMAIL_FIELD)
        email_element.click()
        email_element.clear()
        email_element.send_keys(text)
        self.click_sign_me()


class ContactPage(BasePage):
    def check_photo_exists(self):
        main = self.driver.find_element(*ContactPageLocators.MAIN)
        contact_block = main.find_elements(*ContactPageLocators.LOCATION_BLOCK_US)
        for contact in contact_block:
            adress = contact.find_element_by_class_name('address')
            photo_title = contact.find_element_by_class_name('img-fluid').get_attribute('alt')
            if 'Edison' in adress.text and 'Edison' in photo_title:
                return True
        return False

    def check_if_all_listings_have_photos(self):
        main = self.driver.find_element(*ContactPageLocators.MAIN)
        contact_blocks = main.find_elements_by_class_name('locations-block')
        for contact in contact_blocks:
            row = contact.find_elements_by_class_name('row')
            for item in row:
                cols = item.find_elements_by_class_name('col-md-4')
                for col in cols:
                    wrapper = col.find_element_by_class_name('image-wrapper')
                    image = wrapper.find_element_by_tag_name('img')
                    if image is False or None:
                        return False
        return True


class CareersPage(BasePage):
    def click_europe(self):
        element_eu = self.driver.find_element(*CareerPageLocators.EUROPE_BUTTON)
        element_eu.click()

    def click_ltu(self):
        element_lt = self.driver.find_element(*CareerPageLocators.LITHUANIA_BUTTON)
        element_lt.click()

    def check_work_exist(self):
        return 'Lithuania – Vilnius' in self.driver.page_source
