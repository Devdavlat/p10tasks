"""
get_next_multiple nomli generator yarating, bunda generator f
unksiya bitta son qabul qiladi. Yaratilgan generator obyekt next()
orqali olganda berilgan son keyingi bo'luvchilarini qaytarsin.
"""


def get_next_multiple(number):
    value = number
    while True:
        yield value
        value += number


it = get_next_multiple(2)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
