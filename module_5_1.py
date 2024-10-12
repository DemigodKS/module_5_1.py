class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)


h1 = House('ЖК Бобры,', 15)
h2 = House('Домик в горах,',5)

print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)

h1.go_to(0)
h1.go_to(2)
print()
h2.go_to(7)
h2.go_to(3)