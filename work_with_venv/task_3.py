def read_file(file):
    with open(file, 'r', encoding='utf8') as f:
        data = f.readlines()
        res = []
        for i in data:
            if i.split('=')[0][:-1] == 'name':
                res.append(i.split('=')[1][1:-2])
        return res


def gen_(file):
    data = read_file(file)
    for i in data:
        yield i


file_path = 'planets.txt'
generator = gen_(file_path)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

