def a_iter():
    for i in range(1, 21):
        if i % 2 == 0:
            yield i * -1
        else:
            yield i


iter = a_iter()
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))


