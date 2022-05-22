with open("text_2.txt", encoding="utf-8") as f:
    my_l = f.readlines()
    for index, value in enumerate(my_l, 1):
        num = len(value.split())
        print(f'строка{index} содержит {num} слов')