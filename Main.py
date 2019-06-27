import Player
from Tools import *
from Lists import * 
from PlayerTools import *

# Global Variables
player=Player.Player()
currentOptionList=''

if __name__ == '__main__':
    createPlayer()
    currentOptionList=mainMenu
    while 0==0:
        choosingOptions(currentOptionList)