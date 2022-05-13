my_l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res = [my_l[n] for n in range(1, len(my_l)) if my_l[n] > my_l[n -1]]
print(res)