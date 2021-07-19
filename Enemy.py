import random
import time


class Monster:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage


class Goblin(Monster):
    def __init__(self):
        super(Goblin, self).__init__(50, 5)
        print("I'll gut you and make you squeel like a little piggy")


    def attack(self):
        print('The goblin lashes at you!')


class Orc(Monster):
    def __init__(self):
        super(Orc, self).__init__(100, 10)
        print('The age of men has ended the age of the orc has begun!')

    def attack(self):
        print('The orc slashes at you')


class Rat(Monster):
    def __init__(self):
        super(Rat, self).__init__(25, 5)
        print('SQEEEEEL')

    def attack(self):
        print("The rat bites you!")


class RandomEnemy:
    def __init__(self):
        random_number = random.randint(0, 3)
        if random_number == 0:
            enemy = Goblin()
            # print(enemy.health)
            # enemy = Monster.Goblin()
            print("Prepare to battle the bloodthirsty goblin")
            # print(Goblin.__dict__)
            time.sleep(1.5)
        elif random_number == 1:
            enemy = Orc()
            # print(enemy.health)
            # enemy = Monster.Orc()
            print("Prepare to battle the brutish orc")
            # print(Orc.__dict__)
            time.sleep(1.5)
        elif random_number == 2:
            enemy = Rat()
            # print(enemy.health)
            # enemy = Monster.Rat()
            print("Prepare to battle the diseased rat")
            # print(Rat.__dict__)
            time.sleep(1.5)
        return
