month = int(input("Введите месяц от 1 до 12:"))
month_dict = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь",
              7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
month_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
              "Июль", "Август" "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
if month in month_dict:
    print (f"{month} - {month_dict[month]}")
    print (f"{month} - {month_list[month - 1]}")
else:
    print("Wrong number.")