from functools import reduce
def my_f(n_1, n_2):
    return n_1 * n_2
my_l = [n for n in range (100, 1001, 2)]
print(reduce(my_f, my_l))

