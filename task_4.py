my_l = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_l = [n for n in my_l if my_l.count(n) == 1]
print(my_l)
print(new_l)