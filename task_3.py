with open("text_3.txt", encoding="utf-8") as f:
    people = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Оклад = {round(sum(people.values()) / len(people), 3)}\n'
          f'Оклад меньше 20 тысяч {[n[0] for n in people.items() if n[1] < 20000]}')