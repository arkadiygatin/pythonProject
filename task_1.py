def my_f(s_1="", s_2=""):
    div = s_1 / s_2
    return int(div)
try:
    print(my_f(int(input("Введите первое число")), int(input("Введитие второе число"))))
except (ValueError, ZeroDivisionError) as err:
   print(err)
