import csv
from collect_exception import get_exceptiona


class WorkWithCSVFiles:
    def __init__(self, file_path_):
        self.file_path = file_path_

    def read_files(self):
        try:
            open(self.file_path)
        except Exception as e:
            ex_object = get_exceptiona.GetException(Exception, e)
            ex_object.write_exception()
        else:
            with open(self.file_path) as file:
                csv_reader = csv.DictReader(file)
                return [data for data in csv_reader]

    @staticmethod
    def write_csv_file(csv_file_path, data):
        # print(type(data))
        csv_file_path = f'/home/davlat/p10_lessons/module_3/lesson_1/on_lesson/' \
                        f'csv_files/country_csv_files/{csv_file_path}'

        with open(csv_file_path, 'a', encoding='utf8') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(data)

    def work_with_dict_data_files(self):
        # print(self.read_files())
        data = self.read_files()

        for i in data:
            res = [['username', 'owner']]
            country = i.get('Country/Continent')
            country = country + '.csv'
            user_name = i.get('Username')

            owner = i.get('Owner')
            res.append([user_name, owner])
            # print(res)
            print(res)
            self.write_csv_file(country, res)
            res = []


file_path = '/home/davlat/p10_lessons/module_3/lesson_1/on_lesson/csv_files/List_of_most_followed_Instagram_accounts.csv'
csv_file_obj = WorkWithCSVFiles(file_path)
print(csv_file_obj.work_with_dict_data_files())
