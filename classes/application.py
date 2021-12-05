from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        Check if Modal has data
        '''
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@data-test="apply-modal-external-link"]'))
        )

        if self.driver.find_element(By.XPATH, '//*[@data-test="apply-modal-external-link"]'):
            return True

    def applications_left(self):

        amount_left = len(self.driver.find_elements(By.XPATH, '//div[@class="sc-bYEvvW bEenI"]//*[@class="sc-kLgnNl jJkxZW"]'))

        return amount_left

    def capture_openings(self, amount):

        captures = []

        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="sc-bYEvvW bEenI"]//*[@class="sc-kLgnNl jJkxZW"]')),
        )

        applications_left = self.applications_left()

        for i in range(applications_left):
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@data-test="apply-button"]'))
            )
            # open modal

            self.driver.find_element(By.XPATH, '//*[@data-test="apply-button"]').click()

            if self.modal_checker():

                href = self.driver.find_element(By.XPATH, '//*[@data-test="apply-modal-external-link"]').get_attribute(
                    'href')

                captures.append(href)
                # exit
                self.driver.find_element(By.XPATH, '//div[@class="sc-clsFYl gDsWBR"]').click()

            # next
            self.driver.find_element(By.XPATH, '//*[@data-testid="next-button"]').click()

        print(captures)
