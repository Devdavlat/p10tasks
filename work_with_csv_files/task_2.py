"""
List of most-followed Instagram accounts.csv faylda berilgan ma'lumotlardan foydalangan holda bir davlatga
tegishli account larni alohida csv faylga yozing, bunda fayl nomi
<country_name> accounts.csv, masalan: United States accounts.csv

"""
from task_1 import WorkWith2Files


class WorkWithFile(WorkWith2Files):
    def __init__(self, file_1, file_2, instagram_csv_file):
        super().__init__(file_1, file_2)
        self.file = instagram_csv_file

    def display(self):
        data = self.read_file(self.file)
        [print(row) for row in data]

    def make_data_by_country_name(self):
        country_names_and_data = {}

        data = self.read_file(self.file)
        header = list(data[0].keys())
        for row in data:
            country_name = row.get('Country/Continent')

            if country_name not in list(country_names_and_data.keys()):
                country_names_and_data[country_name] = [row]
            else:
                country_names_and_data.get(country_name).append(row)

        for name, data_ in country_names_and_data.items():
            file_path = f'work_with_csv_files/csv_files/country_accounts_file/{name} account.csv'

            self.make_csv_file(file_path, header, data_)


file_1_path = 'csv_files/Department_information.csv'
file_2_path = 'csv_files/Employee_information.csv'
instagram_csv_file_path = 'csv_files/list_of_most_followed_instagram_account.csv'

file_obj = WorkWithFile(file_1_path, file_2_path, instagram_csv_file_path)
# print(file_obj.make_data_by_country_name())
