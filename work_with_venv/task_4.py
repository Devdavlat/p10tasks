import csv


def read_csv_file():
    with open('country_of_the_world.csv', 'r', encoding='utf8') as f:
        cvs_reader = csv.DictReader(f)
        return [i for i in cvs_reader]


def make_data(func):
    def replace_(data_):
        for row in data_:
            for key, value in row.items():
                value = value.replace(',', '.')
                row[key] = value
        return func(data_)

    return replace_


@make_data
def main_func(data_):
    header = list(data_[0].keys())
    new_file_path = 'new_info_about_countries.csv'
    with open(new_file_path, 'w', encoding='utf8') as f:
        csv_writer = csv.DictWriter(f, header)
        csv_writer.writeheader()
        csv_writer.writerows(data)



file_path = 'country_of_the_world.csv'
data = read_csv_file()

print(main_func(data))
