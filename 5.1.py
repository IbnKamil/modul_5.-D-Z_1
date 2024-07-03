# Модуль №5, Д/З №1
# ПРАКТИЧЕСКОЕ ЗАДАНИЕ
# 2023/10/25 00:00|Домашняя работа по уроку "Атрибуты и методы объекта."
# Цель: применить на практике знания о классах, объектах и их атрибутах.
#
# Задача "Developer - не только разработчик"


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor < 1:
            print("Такого этажа не существует")
        elif self.new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        elif self.new_floor < self.number_of_floors:
            i = 1
            while i <= self.new_floor:
                print(int(i))
                i += 1


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

h3 = House('Lagranda', 20)

h3.go_to(19)