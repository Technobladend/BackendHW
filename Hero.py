
class SuperHero:
    people = 'people'

    def __init__(self, name: str, nickname: str, superpower: str, health_point: int, catch_phrase: str):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_point
        self.catch_phrase = catch_phrase


    def hero_name(self):
        return print(self.name)


    def multiply_hp(self):
        return self.health_point * 2

    def __str__(self):
        return f"Hero's name: {self.name}, his power: {self.superpower} And he has {self.health_point}HP"

    def __len__(self):
        return len(self.catch_phrase)


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_point, catch_phrase, damage, efficiency, fly=False):
        super().__init__(name, nickname, superpower, health_point, catch_phrase)
        self.damage = damage
        self.fly = fly
        self.efficiency = efficiency
        self.true_phrase = "My justice"

    def multiply_hp(self):
        self.fly = True
        return self.health_point ** 2

    def true_phrase_method(self):
        print(f"True in the {self.true_phrase}")


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_point, catch_phrase, damage, efficiency, fly=False):
        super().__init__(name, nickname, superpower, health_point, catch_phrase)
        self.damage = damage
        self.fly = fly
        self.efficiency = efficiency
        self.true_phrase = "Power of Heaven"

    def multiply_hp(self):
        self.fly = True
        return self.health_point ** 2

    def true_phrase_method(self):
        print(f"True in the {self.true_phrase}")



class Villain(SuperHero):
    def __init__(self, name, nickname, superpower, health_point, catch_phrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_point, catch_phrase)
        self.damage = damage
        self.fly = fly
        self.people = "monster"

    def __str__(self):
        return f"Villain's name: {self.name}, his power: {self.superpower} And he has {self.health_point}HP"

    def gen_x(self):
        pass

    def crit(self, other):
        return self.damage ** other.damage



earth_hero = EarthHero("John", "Sonic", "Speed", 1000, "Catch, if you can", 10, "massive")
print(earth_hero.multiply_hp())
print(earth_hero.fly)
earth_hero.true_phrase_method()

air_hero = AirHero("Mike", "WindWalker", "Flight", 80, "Breeze through!", 100, "single", True)
print(air_hero.multiply_hp())
print(air_hero.fly)
air_hero.true_phrase_method()

villain = Villain("EggMan", "EggMan", "Mind", 60, "I will rule the world!", 3)
print(villain)
print(villain.crit(earth_hero))
