import winsound
# import Player
# import Enemy
from Player import PlayerChoice
import os


class Ambiance:
    @staticmethod
    def intro_music():
        intro = 'Main_Menu.wav'
        winsound.PlaySound(intro, winsound.SND_ASYNC)

    @staticmethod
    def expl_music():
        expl = "Exploring.wav"
        winsound.PlaySound(expl, winsound.SND_ASYNC)

    @staticmethod
    def battle_music():
        battle = 'BattleFinal.wav'
        winsound.PlaySound(battle, winsound.SND_ASYNC)

class combat:
    pass
