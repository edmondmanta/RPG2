import time


class Player:
    def __init__(self, name, health, mana, damage):
        self.name = name
        self.health = health
        self.mana = mana
        self.damage = damage

    def attack(self):
        pass


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, 150, 50, 50)


class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, 100, 150, 75)


class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, 100, 75, 100)


class PlayerChoice:
    @staticmethod
    def class_choice():
        # cls_choice = ''
        incorrect_option = True
        while incorrect_option:
            cls_choice = input('''What class would you like to be? Press a number to select a class 
1 - Warrior - strong, agile, packs a punch
2 - Mage - slick caster, turns enemies to dust 
3 - Rogue -  sneaky thief, agile back stabber

Press a number to select a class ->
    ''')
            if cls_choice == '1':
                incorrect_option = False
                player_name = input("""
    You have chosen to be a mighty warrior
                
What is the character's name ? -> """)
                print(f'''
    You shall be called {player_name} the Strong''')
                print('''
    Loading
                ''')
                player = Warrior(player_name)
                # print(player.health)
                time.sleep(2)
            elif cls_choice == '2':
                incorrect_option = False
                player_name = input("""
    You have chosen to be a clever wizard
    
What is the character's name ? -> """)
                print(f'''
    You shall be called {player_name} the Wise''')
                print('''
    Loading
                ''')
                player = Wizard(player_name)
                time.sleep(2)
            elif cls_choice == '3':
                incorrect_option = False
                player_name = input("""
    You have chosen to be a sneaky rogue
    
What is the character's name ? -> """)
                print(f'''
    You shall be called {player_name} the Shadow''')
                print('''
    Loading
                ''')
                player = Rogue(player_name)
                time.sleep(2)
            else:
                incorrect_option = True
                print('Invalid option, please choose again')
