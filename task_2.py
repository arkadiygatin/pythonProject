time = int(input("введите время в секундах: "))
hours = time // 3600
minutes = time // 60 - hours * 60
sec = time % 60
print(f" {hours}:{minutes}:{sec} ")