"""
Ikkita sonni qo'shadigan funksiyaga dekorator qo'shing,
bunda funksiya qiymati 2 ga ko'payirilgan holda qaytarilsin.

"""



def main_funct():
    def extra_func(n, m):
        return (n + m) * 2

    return extra_func


marge = main_funct()

print(marge(10, 3))
