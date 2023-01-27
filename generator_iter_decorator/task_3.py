"""
Ikkita sonni qo'shadigan funksiyaga dekorator qo'shing,
bunda funksiya qiymati 2 ga ko'payirilgan holda qaytarilsin.

"""


def main_funct(funct):
    def extra_func(a, b):
        return funct(a * 2, b * 2)

    return extra_func


@main_funct
def marge(a, b):
    return a + b


print(marge(10, 3))
