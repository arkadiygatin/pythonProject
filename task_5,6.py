revenue = float(input("Введите значение выручки"))
costs = float(input("Введите значение издержек"))
result = revenue - costs
if result > 0:
    print(f"Ваша прибыль {result} рублей")
    print(f"Ваш убыток {100 * result / revenue:.1f}%")
    pesonal = int(input("Количество людей в компании?"))
    print(f"Всю прибыль людям компании, каджый получает по {result / personal:.3f} рублей. ")
elif result < 0:
    print(f"Ваш убыток {result} рублей")
else:
    print(f"Ваша прибыль {result} рублей")