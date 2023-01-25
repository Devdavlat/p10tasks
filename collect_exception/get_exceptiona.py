import csv
from datetime import datetime


class GetException:
    def __init__(self, exception, e):
        self.exception = exception
        self.e = e

    def write_exception(self):
        header = ['Exception Name', 'about exceptions', 'time']
        current_time = datetime.now()
        rows = [self.exception, self.e, current_time]

        with open("exceptions.csv", 'a', encoding='utf8') as f:
            csv_writer = csv.DictWriter(f, header)
            csv_writer.writeheader()
            csv_writer.writerows(rows)
