import os
# import Player
import Utils
# import Enemy
from Enemy import RandomEnemy
import time
from StoryBoard import Story
from Player import PlayerChoice
Story.intro()


print('Would you like to start the adventure?')

user_input = ''
incorrect_answer = True
while incorrect_answer:
    user_input = input('Please type Yes or No -> ')
    if user_input.upper() == 'Y':
        incorrect_answer = False
        Utils.Ambiance.intro_music()
        time.sleep(0.5)
        os.system('cls')
        PlayerChoice.class_choice()
        Utils.Ambiance.expl_music()
        Story.first_path()
        Story.road1()
        Utils.Ambiance.battle_music()
        RandomEnemy()
        Utils.combat()
        time.sleep(0.5)


        print("onward")

    elif user_input.upper() == 'N':
        print('Thank you, good bye')
        break
    else:
        incorrect_answer = True
        print("Invalid option, please choose again")
