"""
only_even_parameters nomli dekorator yarating,
bunda quyidagi funksiyallarda ishlating va tegishli natija qaytaring.

"""


def only_even_parametres(funct):
    def inner_funct(*args):

        for i in args:
            if i % 2 != 0:
                return "please enter even number"

        return funct(*args)

    return inner_funct


@only_even_parametres
def add(a, b):
    return a + b


@only_even_parametres
def multiply(a, b, c, d):
    return a * b * c * d


print(add(2, 2))
print(multiply(1, 2, 2, 2))
