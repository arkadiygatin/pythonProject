def my_f(**kwargs):
    return ' '.join(kwargs.values())
print(my_f(name=input("Имя - "), surname=input("Фамилия - "),birthday=input("Год рождения - "),
           city=input("Город - "), email=input("Email"), phone=input("Телефон - ")))


