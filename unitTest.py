import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

import page
from selenium.webdriver import ChromeOptions


class OrionTest(unittest.TestCase):
    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:\\Users\\mgelumb\\Desktop\\test_orion\\chromedriver.exe", options=options)
        self.driver.get('https://www.orioninc.com/')

    def test_lithuanian_jobs(self):
        main_page = page.MainPage(self.driver)
        accept_all = main_page.AcceptElement
        accept_all.click()
        main_page.click_careers()
        career_page = page.CareersPage(self.driver)
        career_page.click_europe()
        career_page.click_ltu()
        assert career_page.check_work_exist()

    def test_search(self):
        main_page = page.MainPage(self.driver)
        accept_all = main_page.AcceptElement
        accept_all.click()
        main_page.click_search()
        main_page.search_text_element = 'covid'
        main_page.click_submit_search()
        content = main_page.main
        assert main_page.check_search_results(content)

    def test_photo_exists(self):
        main_page = page.MainPage(self.driver)
        accept_all = main_page.AcceptElement
        accept_all.click()
        main_page.click_contact_us()
        contat_page = page.ContactPage(self.driver)
        assert contat_page.check_photo_exists()
        assert contat_page.check_if_all_listings_have_photos()

    def test_sign_me_up_errors(self):
        main_page = page.MainPage(self.driver)
        accept_all = main_page.AcceptElement
        accept_all.click()
        main_page.enter_validation_bad('covid')
        email_error = main_page.validation_err_email
        assert email_error.text == \
               'The email address entered is invalid, please check the formatting (e.g. email@domain.com).'
        main_page.enter_validation_bad('papa@gmail.com')
        time.sleep(2)
        with self.assertRaises(TimeoutException):
            main_page.validation_err_email

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
