number = int(input("Введите целое положительное число:"))
max_var = 0
num = number

while num > 0:
    digit = num % 10
    if digit > max_var:
        max_var = digit
        if max_var == 9:
         break
    num = num // 10
print(f"Наибольшая цифра в числе {number} равна {max_var}  ")