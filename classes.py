class animals():

    def __init__(self, name, voice, weight):
        self.name = name
        self.voice = voice
        self.weight = weight


    def feeding(self):
        self.state = 'Накормлен(а)'
        print(f'{self.name} {self.state}')

    def get_voice(self):
        print(f'{self.name} говорит {self.voice}')

    def __add__(self, other):
        return self.weight + other.weight


class birds(animals):
    def collect_eggs(self):
        print(f'у {self.name} собраны яйца')


class horned(animals):
    def milk(self):
        self.state = 'подоена'
        print(f'{self.name} {self.state}')


class sheep(animals):
    def shave(self):
        self.state = 'подстрижен'
        print(f'{self.name} {self.state}')


name_by_weight = {}
weight_list = []
goose_grey = birds("Серый", 'Кря-кря', 6)
goose_grey.feeding()
goose_grey.get_voice()
goose_grey.collect_eggs()
name_by_weight[goose_grey.weight] = goose_grey.name

goose_white = birds('Белый', "Кря-кря", 5)
goose_white.feeding()
goose_white.collect_eggs()
goose_white.get_voice()
name_by_weight[goose_white.weight] = goose_white.name

chicken_coco = birds("Ко-ко", "Ко-ко", 4)
chicken_coco.feeding()
chicken_coco.collect_eggs()
chicken_coco.get_voice()
name_by_weight[chicken_coco.weight] = chicken_coco.name

chicken_Kukareku = birds("Кукареку", "Ко-ко", 3)
chicken_Kukareku.feeding()
chicken_Kukareku.collect_eggs()
chicken_Kukareku.get_voice()
name_by_weight[chicken_Kukareku.weight] = chicken_Kukareku.name

duck_quack = birds("Кряква", 'Кря-кря', 4)
duck_quack.feeding()
duck_quack.collect_eggs()
duck_quack.get_voice()
name_by_weight[duck_quack.weight] = duck_quack.name

goat_horns = horned("Рога", 'Мее', 53)
goat_horns.feeding()
goat_horns.milk()
goat_horns.get_voice()
name_by_weight[goat_horns.weight] = goat_horns.name

goat_hoofs = horned("Копыта", 'Мее', 42)
goat_hoofs.feeding()
goat_hoofs.milk()
goat_hoofs.get_voice()
name_by_weight[goat_hoofs.weight] = goat_hoofs.name

cow_manka = horned("Манька", 'Муу', 240)
cow_manka.feeding()
cow_manka.milk()
cow_manka.get_voice()
name_by_weight[cow_manka.weight] = cow_manka.name

sheep_lumb = sheep("Барашек", 'Бее', 53)
sheep_lumb.feeding()
sheep_lumb.shave()
sheep_lumb.get_voice()
name_by_weight[sheep_lumb.weight] = sheep_lumb.name

sheep_curly = sheep("Кудрявый", 'Бее', 50)
sheep_curly.get_voice()
sheep_curly.shave()
sheep_curly.get_voice()
name_by_weight[sheep_curly.weight] = sheep_curly.name

sum_weight = goose_grey.weight + goose_white.weight + \
             duck_quack.weight + goat_hoofs.weight + goat_horns.weight + \
             chicken_coco.weight + sheep_curly.weight + sheep_lumb.weight + \
             cow_manka.weight

print(f'Суммарный вес всех животных: {sum_weight}')

for weight in name_by_weight:
    weight_list.append(weight)

print(f'Наибольший вес среди животных у {name_by_weight[max(weight_list)]}')
