class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
        self.house_info()

    def house_info(self):
        print(f'В жилищном комплексе {self.name}, {self.number_of_floor} этажей ')


    def go_to(self, new_floor):
        if new_floor > self.number_of_floor or new_floor < 1:
            print(f'{new_floor} этажа в "{self.name}" не существует')
        else:
            for i in range(new_floor):
                print(i+1)


h1 = House('ЖК Горский', 18)
h1.go_to(5)
h2 = House('Домик в деревне', 2)
h2.go_to(10)
