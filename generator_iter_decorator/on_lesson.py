# my_list = [1, 2, 3, 4]
# iterator = iter(my_list)
# print(next(iterator))
# print(next(iterator))


def gen():
    yield 1,2
    yield 2
    yield 3
    yield 4


print(gen())

i = iter(gen())
print(type(next(i)))
print(next(i))
print(next(gen()))
print(next(gen()))
print(next(gen()))
print(next(gen()))
print(next(gen()))

# class PowTwo:
#     def __init__(self, limit=0):
#         self.limit = limit
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n < self.limit:
#             pow_number = 1 + self.n
#             self.n += 1
#             return pow_number
#         else:
#             raise StopIteration
#
#
# numbers = PowTwo(20)
# iterator = iter(numbers)
# print(next(iterator))
# print(next(iterator))

# for i in iterator:
#     print(i)

# def square():
#     return
#
#
# def generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
#
# generator = generator()
#
# [print(next(generator)) for i in range(generator)]

# def hello(name):
#     def get_name():
#         return f'hello {name}'
#
#     return get_name
#
#
# name = hello("aa")
# print(name())
