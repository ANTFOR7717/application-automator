# TODO: Convert find by class to find by xpaths
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Application(object):
    def __init__(self, job_board_name):
        self.url = str()
        self.driver = object
        self.job_board_name = job_board_name

    def set_safari_webdriver(self):
        self.driver = webdriver.Safari()

    def set_url(self, url):
        self.url = url

    def get_webpage(self, url):
        self.driver.get(url)

    def element_available(self, xpath, time=4):
        try:
            WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            self.driver.find_element(By.XPATH, xpath)
        # TODO: Fix Exception Issue
        except:
            return False
        return True

    def select_element_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def email_auth(self, email, password):
        if self.job_board_name in "otta":
            find_email = self.driver.find_element(By.ID, 'email')
            find_password = self.driver.find_element(By.ID, 'password')
            find_email.send_keys("testingitout@gmail.com")
            find_password.send_keys("Qazws123!")
            self.driver.find_element(By.XPATH, '//button').click()
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="view-matches-button"]')),
            )
            self.driver.find_element(By.XPATH, '//*[@data-testid="view-matches-button"]').click()
        else:
            print("Incorrect Option")
            self.driver.close()

    def modal_checker(self):
        '''
        Check if Modal has href data
        :return: Boolean
        '''
        return self.element_available('//*[@data-test="apply-modal-external-link"]')

    def applications_left(self):

        amount_left = len(
            self.driver.find_elements(By.XPATH, '//div[@class="sc-bYEvvW bEenI"]//*[@class="sc-kLgnNl jJkxZW"]'))

        return amount_left

    # TODO: Implement Next Batch auto
    def next_batch(self):
        """
        Change batch
        :return:
        """
        if self.element_available('//button[@class="sc-kstqJO jkAPd"]'):
            self.driver.find_element(By.XPATH, '//button[@class="sc-kstqJO jkAPd"]').click()

    def application_loop(self, applications_left, amount):
        applications = []

        for i in range(applications_left):
            if len(applications) <= amount:
                WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@data-test="apply-button"]'))
                )
                # open modal

                self.driver.find_element(By.XPATH, '//*[@data-test="apply-button"]').click()

                if self.modal_checker():
                    href = self.driver.find_element(By.XPATH,
                                                    '//*[@data-test="apply-modal-external-link"]').get_attribute(
                        'href')
                    applications.append(href)
                    print(href)

                # exit
                self.driver.find_element(By.XPATH, '//div[@data-testid="modal-content"]//div').click()

                # next
                if applications_left == 0:
                    self.next_batch()
                    applications_left = self.applications_left()
                else:
                    self.driver.find_element(By.XPATH, '//*[@data-testid="next-button"]').click()

        return applications

    def capture_openings(self, amount):

        # captures = []

        if self.element_available('//button[@class="sc-kstqJO jkAPd"]', 2):
            self.driver.find_element(By.XPATH, '//button[@class="sc-kstqJO jkAPd"]').click()

        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="sc-bYEvvW bEenI"]//*[@class="sc-kLgnNl jJkxZW"]')),
        )

        applications_left = self.applications_left()

        openings = self.application_loop(applications_left, amount)

        print(openings, len(openings))

        # print(captures)
