class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points: int, catchprhase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchprhase = catchprhase

    def prent(self):
        print(self.name)

    def mul(self):
        self.health_points = self.health_points * 2

    def __str__(self):
        return f'nickname: {self.nickname} \n' \
               f'superpower: {self.superpower} \n' \
               f'health_points: {self.health_points} \n'

    def __len__(self):
        return len(self.catchprhase)


Hero = SuperHero('Andrey', 'Aratus', 'Boroda', 20, (len('internet is a mistake')))

Hero.mul()
Hero.prent()
print(Hero)
print(Hero.catchprhase)


class FlyHero(SuperHero):
    fly = False
    damage = 8

    def __init__(self, name, nickname, superpower, health_points, catchprhase, damage=int, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchprhase)
        self.damage = damage
        self.fly = fly

    def mul(self):
        self.health_points = self.health_points ** 2
        if FlyH.fly == False:
            FlyH.fly = True

    def prhase(self):
        print('fly in the True_phrase')


FlyH = FlyHero('Fly', 'FlyHero', 'Flying', 15, 'Air is my territory', 8, )

FlyH.mul()
FlyH.prhase()
print(FlyH)
print(FlyH.fly)


class SoilHero(SuperHero):
    fly = False
    damage = 6

    def __init__(self, name, nickname, superpower, health_points, catchprhase, damage=int, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchprhase)
        self.damage = damage
        self.fly = fly

    def mul(self):
        self.health_points = self.health_points ** 2
        if SoilH.fly == False:
            SoilH.fly = True

    def prhase(self):
        print('fly in the True_phrase')


SoilH = SoilHero('Soil', 'SoilHero', 'Soiling', 20, 'Soil is my ground', 6, )
SoilH.mul()
SoilH.prhase()
print(SoilH)
print(SoilH.fly)


class Villain(FlyHero):
    people = 'monster'

    def gen_x(self): ...

    def crit(self):
        self.damage = self.damage ** 2


villain = Villain('npc', "gopar'", 'drobovik', 100, 'maslinu poimal', 10, )

Villain.crit(FlyH)

print(FlyH.damage)