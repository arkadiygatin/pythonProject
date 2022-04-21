n = input("Введите число - ")

while n < "0":
    print ("Введите число больше 0 :")
    n = input("Введите число больше 0 ")

print (f"{n} + {n + n} + {n + n + n} = {int(n) + int(n +n) + int(n +n + n)}")
