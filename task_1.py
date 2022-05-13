from sys import argv
name, n_1, n_2, n_3, = argv
try:
    n_1 = int(n_1)
    n_2 = int(n_2)
    n_3 = int(n_3)
    n_4 = n_1 * n_2 + n_3
    print(f'Заработная плата сотрудника {n_4}')
except ValueError:
    print("Введите три числа")



