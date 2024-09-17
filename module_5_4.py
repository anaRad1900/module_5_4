class House:
    houses_history = []  # Атрибут класса для хранения истории зданий

    def __new__(cls, *args, **kwargs):
        # Получаем название здания из args
        name = args[0]

        # Добавляем название здания в историю
        cls.houses_history.append(name)

        # Создаём новый объект
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        # Выводим сообщение о том, что объект был удалён
        print(f"{self.name} снесён, но он останется в истории")


# Создание объектов
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2
del h3

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
