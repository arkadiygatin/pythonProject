my_list = [4, 1, 3, 8, 3, 2, 3, 1]
new_number = int(input("введите новое число:"))
i=0
for n in my_list:
    if new_number <= n:
        i += 1
    else:
        break
my_list.insert(i, new_number)
print(my_list)