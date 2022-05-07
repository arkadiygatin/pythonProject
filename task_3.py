my_f = lambda s_1, s_2, s_3: (s_1 + s_2 + s_3) - min(s_1, s_2, s_3)
print(my_f(s_1=int(input("Первое число - ")),s_2=int(input("Второе число - ")),s_3=int(input("Третье число - "))))