"""
sum_index nomli funksiya yarating va bu funksiya faqat list qabul qilsin.
Funksiya berilgan list indexlari yig'indisini qaytarsin.
Funksiyaga beriladigan argumentni tekshirish uchun dekorator yozing.

"""


def my_funct(funct):
    def inner_funct(variable):
        if type(variable) is not list:
            return 'Please send only list'
        else:
            funct(variable)

    return inner_funct


@my_funct
def sum_index(variable_):
    sum_up = [i for i in variable_]
    res = sum(sum_up)
    print(res)
    return res


print(sum_index([1, 2, 3]))
print(sum_index([1, 2]))
print(sum_index((1, 2)))
