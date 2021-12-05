import time
from classes.application import Application


def events():
    application_automator = Application("otta")
    application_automator.set_safari_webdriver()
    application_automator.set_url("https://app.otta.com/login")
    application_automator.get_webpage(application_automator.url)
    application_automator.email_auth('', '')
    application_automator.capture_openings(6)
    time.sleep(10)


    # driver = webdriver.Safari()
    # driver.get("https://app.otta.com/login")
    # time.sleep(10)
    # driver.close()


if __name__ == '__main__':
    events()
