class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
    def mass(self, weight=25, fatness=5):
        return f'{self._lenght} m * {self._width} m * {weight} kg * {fatness} sm ='\
               f'{(self._lenght * self._width * weight * fatness) / 1000} t'


road_1 = Road(int(input("Введите длину")), int(input("Введите ширину")))
print(road_1.mass())