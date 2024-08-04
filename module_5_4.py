class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return cls.houses_history


    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        self.number_of_floor = self.number_of_floor + value
        return self

    def __iadd__(self, value):
        self.number_of_floor += value
        return self

    def __radd__(self, value):
        self.number_of_floor = value + self.number_of_floor
        return self

    def go_to(self, new_floor):
        for i in range(new_floor):
            if new_floor > self.number_of_floor:
                print(f'{new_floor} этажа в "{self.name}" не существует')
                break
            else:
                print(i+1)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)
