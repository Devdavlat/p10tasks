def read_file(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        data = f.read()
        return data


def generator(file):
    data = read_file(file)
    for i in data:
        yield i


file_path = 'text.txt'
gen = generator(file_path)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
