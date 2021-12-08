import time
from classes.application import Application
from classes.filesaver import FileSaver

job_list = ['https://meraki.cisco.com/jobs?gh_jid=3457552&gh_src=f894f2621us',
            'https://boards.greenhouse.io/boxinc/jobs/3649182?utm_source=Otta',
            'https://www.waybridge.com/careers?gh_jid=4542136003&gh_src=ef46f6f63us',
            'https://jobs.lever.co/mainstreet/fc953385-a176-4b53-9061-9eecabf5eef3?lever-source=Otta',
            'https://boards.greenhouse.io/tiney/jobs/4819177003?gh_src=c4e964713us',
            'https://boards.greenhouse.io/vivian/jobs/5475454002?utm_source=Otta',
            'https://boards.greenhouse.io/signpost/jobs/3316364?utm_source=Otta',
            'https://jobs.lever.co/flatfile/fc635adf-bef8-44a9-960a-9bac968372a9?lever-source=Otta',
            'https://boards.greenhouse.io/homer/jobs/5570280002?utm_source=Otta',
            'https://boards.greenhouse.io/tifin/jobs/4148383004?utm_source=Otta']


def automation_events():
    application_automator = Application("otta")
    application_automator.set_safari_webdriver()
    application_automator.set_url("https://app.otta.com/login")
    application_automator.get_webpage(application_automator.url)
    application_automator.email_auth('', '')
    application_automator.capture_openings(3)
    time.sleep(10)


def file_writing_events():
    data_file = FileSaver()
    data_file.write_row('f')
    for job in job_list:
        print(data_file.url_checker(job))

    # driver = webdriver.Safari()
    # driver.get("https://app.otta.com/login")
    # time.sleep(10)
    # driver.close()


if __name__ == '__main__':
    file_writing_events()
