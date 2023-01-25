"""
imployee id, dob, doj, department name
"""

import csv
from collect_exception import get_exceptiona


class WorkWith2CSVFiles:
    def __init__(self, first_csv_file_path, second_csv_file_path):
        self.file_1_csv_path = first_csv_file_path
        self.file_2_csv_path = second_csv_file_path

    @staticmethod
    def read_files(file_path):
        try:
            open(file_path)
        except Exception as e:
            ex_object = get_exceptiona.GetException(Exception, e)
            ex_object.write_exception()
        else:
            with open(file_path) as file:
                csv_reader = csv.DictReader(file)
                return [data for data in csv_reader]

    @staticmethod
    def write_csv_file_with_dict(file_path, data):
        try:
            open(file_path, 'w')
        except Exception as e:
            ex_object = get_exceptiona.GetException(Exception, e)
            ex_object.write_exception()

        else:
            with open(file_path, 'w', encoding='utf8') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerows(data)

    def make_data_form_files(self, file_path):
        rows = [['Employee ID', 'DOB', 'DOJ', 'Department_Name']]

        data_of_row = []
        first_file_data = self.read_files(self.file_1_csv_path)
        second_file_data = self.read_files(self.file_2_csv_path)
        counter = 1
        for i in second_file_data:

            data_of_row.append(i.get('Employee ID'))

            data_of_row.append(i.get('DOB'))

            data_of_row.append(i.get('DOJ'))
            rows.append(data_of_row)
            data_of_row = []
            counter += 1
            if counter == 42:
                break

        for index in range(len(first_file_data)):
            data_of_row.append(first_file_data[index].get('Department_Name'))
            rows[index].append(data_of_row[0])
            data_of_row = []
        return self.write_csv_file_with_dict(file_path, rows)


department_csv_file_path = '/home/davlat/p10_lessons/module_3/lesson_1/on_lesson/csv_files/department_info.csv'
employee_csv_file_path = '/home/davlat/p10_lessons/module_3/lesson_1/on_lesson/csv_files/Imployee_info.csv'
new_file_path = "/home/davlat/p10_lessons/module_3/lesson_1/on_lesson/csv_files/employee_department.csv"

work_with_file_obj = WorkWith2CSVFiles(department_csv_file_path, employee_csv_file_path)
print(work_with_file_obj.make_data_form_files(new_file_path))
