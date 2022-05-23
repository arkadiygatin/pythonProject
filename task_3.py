class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_total_income(self):
        return sum(self._income.values())


check = Position(input("Имя"), input("Фамилия"), input("Должность"), int(input("ЗП")), int(input("Премия")))
print(check.get_full_name())
print(check.position)
print(check.get_total_income())