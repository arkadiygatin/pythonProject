while True:
    days = 1
    start = float(input("Первый день"))
    last = float(input("Желаемый результат"))
    if start <= 0 or last < 0:
        print("Не могут быть 0")
    else:
        while start < last:
            start+= start * 0.1
            days += 1

        print(f"Он потратит {days} дней")
        break