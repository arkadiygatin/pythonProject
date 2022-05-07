def my_f(x,y):
    try:
        res = x ** y
    except TypeError:
        return "Положительное и отрицательное число"
    return res
print(my_f(int(input("Положительное число - ")),int(input("Отрицательное число - "))))