import csv


class CSVFiles:
    def __init__(self, file_path):
        self.file = file_path

    def red_csv_file(self):
        try:
            open(self.file)
        except Exception as e:
            pass
        else:
            with open(self.file) as csv_reader:
                csv_reader = csv.DictReader(csv_reader)
                return [row for row in csv_reader]

    def display(self):
        return self.red_csv_file()

    # def csv_file_writer(self, new_file_path):
    #     with open(new_file_path, 'a', encoding='utf8') as file:
    #         csv_writer = csv.writer()

    def get_values_from_key(self, key):

        """
        key = str
        return =  data of key (nested list)

        EX:
        key -> 'PHP'
        -> avgust 2004 : 10
        -> avgust 2005 : 11
        -> avgust 2006 : 12
        """
        csv_data = self.red_csv_file()
        result = list()
        for row in csv_data:
            # print(row.get('Abap'))
            temp_data = [row.get('Date'), row.get(key)]
            result.append(temp_data)

        return result

    def get_average_year_values(self, key):
        data = self.get_values_from_key(key)
        term_year = list()
        # print(data)
        res = {}
        for data_list in data:
            # print(data_list)
            year_with_data = data_list[0]
            term_year.append(year_with_data)
            res[year_with_data] = data_list[1]
        for i, v in res.items():
            data = i.split()[1]



        # years = set(term_year)

        # for year in years:
    # print(term_year.count(year))


csv_file_path = '/home/davlat/p10_lessons/module_3/lesson_1/on_lesson/csv_files/most_common_programming_language.csv'

csv_file_object = CSVFiles(csv_file_path)

# print(csv_file_object.get_values_from_key('PHP'))
# print(csv_file_object.display())
print(csv_file_object.get_average_year_values("PHP"))
