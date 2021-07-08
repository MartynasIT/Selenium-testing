from selenium.webdriver.common.by import By


class MainPageLocators(object):
    COMPANY_BUTTON = (By.XPATH, '//span[contains(text(),\'Company\')]')
    CAREERS_BUTTON = (By.LINK_TEXT, 'Careers')
    SEARCH_BTN = (By.CLASS_NAME, 'search-icon')
    SEARCH_FIELD = (By.CLASS_NAME, 's')
    SUBMIT_BTN = (By.XPATH, '//header/div[1]/div[1]/div[1]/div[2]/form[1]/input[2]')
    CONTACT_US_BTN = (By.XPATH, '//header/div[1]/nav[1]/div[2]/ul[1]/li[6]')
    SIGN_ME_UP_BTN = (By.ID, 'gform_submit_button_1')
    EMAIL_FIELD = (By.XPATH, '//input[@id=\'input_1_2\']')


class CareerPageLocators(object):
    EUROPE_BUTTON = (By.LINK_TEXT, 'Europe')
    LITHUANIA_BUTTON = (By.XPATH, '/html[1]/body[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[4]')


class ContactPageLocators(object):
    LOCATION_BLOCK_US = (By.ID, 'locations-block-block_5df152bacb094')
    MAIN = (By.CLASS_NAME, 'site-main')

