with open("text.txt", "w", encoding="utf-8") as f:
    while True:
        line = input("Введите данные построчно:")
        if not line:
            break
        print(line,file=f)
