import random


class Story:
    @staticmethod
    def intro():
        print('''
*****************************************************************************************
* Welcome,stranger.                                                                      *
* Here in Hinterlands, you'll get to fight dragons and conquer the deadliest dungeons.   *
* In a country where magic rules, anything is possible if you wish so.                   *
* It all depends on you, brave hero.                                                     *
*****************************************************************************************

''')

    @staticmethod
    def first_path():
        print('''
    ***************************
    **** You arrive at a crossroad.                   |    0   |
    **** You have 3 paths in front of you:            |   /#\  | <----- You are here
    **** 1. One leads to The Forest of Mirrors        |  + # + |
    **** 2. One leads to Gludin Village               |   | |  |
    **** 3. One leads to the Wastelands               |   = =  |
                                                      |        |
                                                      |        |                                    ^  ^   ^  ^  ^   ^  ^
     ___I_                                            |        |                                   /|\/|\ /|\/|\/|\ /|\/|\  
    /\-_--\                                           |        |                                   /|\/|\ /|\/|\/|\ /|\/|\ 
   /  \_-__\        ---------------------------------           --------------------------------       
   |[]| [] |             < - - - Gludin Village                   Forest of Mirrors - - - >         ^  ^   ^  ^  ^   ^  ^
                    ----------------------------------          --------------------------------   /|\/|\ /|\/|\/|\ /|\/|\    
     ___I_                                            |        |                                   /|\/|\ /|\/|\/|\ /|\/||
    /\-_--\                                           |        |
   /  \_-__\                                          |        |                                    ^  ^   ^  ^  ^   ^  ^
   |[]| [] |                                          |        |                                   /|\/|\ /|\/|\/|\ /|\/|
                                                      |        |                                   /|\/|\ /|\/|\/|\ /|\/|
                                                      |   W    |
                                                      |   A    |
                                                      |   S    |
                                                      |   T    |
                                                      |   E    |
                                                      |   L    |
                                                      |   A    |
                                                      |   N    |
                                                      |   D    | 
                                                      |        |
                                                      |   ||   |
                                                      |  \  /  |
                                                      |   \/   |
                                                      |        |
                                                ,,                               .-.
                                              || |                               ) )
                                              || |   ,                          '-'
                                              || |  | |
                                              || '--' |
                                        ,,    || .----'
                                       || |   || |
                                       |  '---'| |
                                       '------.| |                                  _____
                                       ((_))  || |      (  _                       / /|\ 
                                       (o o)  || |      ))("),                    | | | | |
                                    ____\_/___||_|_____((__^_))____________________\_\|/_/__
''')

    @staticmethod
    def road1():
        # way1 = ''
        incorrect_way1 = True
        while incorrect_way1:
            way1 = input('Choose a path: ')
            if way1 == '1':
                incorrect_way1 = False
                print('You are in the Village of Gludin. From a demolished house exists and enemy')
            elif way1 == '2':
                incorrect_way1 = False
                print('You arrive in the Wastelands')
            elif way1 == '3':
                incorrect_way1 = False
                print('You arrive in the Forest of Mirrors')
            else:
                incorrect_way1 = True
                print('Path not available')
        return
