import csv


class FileSaver(object):
    options = {
        'workable': 0,
        'greenhouse': 1,
        'lever': 2,
        'meraki': 3
    }

    def __init__(self):
        self.file = False

    def write_row(self, file):
        with open('csv/protagonist.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for i in range(4):
                writer.writerow([f'{i}'])

    def url_checker(self, url):
        for key, value in self.options.items():
            if key in url:
                return value
        return 4

    def sort(self):
        return
