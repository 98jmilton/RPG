import Player
from Tools import parseInput,myPrint,choosingOptions,printRace
from Lists import raceStats,stats,classStats,mainMenu
# Global Variables
player=Player.Player()
currentOptionList=''

def createPlayer():
    player.name=parseInput('Please enter characters name: ')
    chosingRace()
    chosingClass()
        
def chosingRace():
    options='Race options:'
    for key in raceStats:
        options+='\n\t'+raceStats[key]['Name']+','
    if(myPrint(options)):pass
    raceChoice = parseInput('Enter choice or type \"stats [racename]\" to see each races stats').lower().split(' ')
    #Stats requested
    if raceChoice[0].lower() == 'stats':
        printRace(raceChoice[1])
        chosingRace()
    #Only choice entered
    elif raceChoice[0] in raceStats:
        player.race=raceChoice[0]
        myPrint('You chose:')
        printRace(player.race)
    # Input has no matches
    else:
        if(myPrint('\nError: check input')):pass
        chosingRace()
 
def chosingClass():
    options='Race options:'
    for key in classStats:
        options+='\n\t'+classStats[key]['Name']+','
    if(myPrint(options)):pass
    classChoice = parseInput('Enter choice or type \"stats [classname]\" to see each classes stats').lower().split(' ')
    #Stats requested
    if classChoice[0].lower() == 'stats':
        printClass(classChoice[1])
        chosingClass()
    #Only choice entered
    elif classChoice[0] in classStats:
        player.classType=classChoice[0]
    # Input has no matches
    else:
        if(myPrint('\nError: check input')):pass
        chosingClass()

def playerDetails():
    if(myPrint(player)):pass


def editPlayer():
    if(myPrint('Edit player details:')):pass
    chosingRace()
    pass

def error():
    if(myPrint('*'*4+'ERROR'+'*'*4+'\nWell that wasnt meant to happen...')):pass
    if(myPrint('cont')):pass
    choosingOptions(currentOptionList)

if __name__ == '__main__':
    createPlayer()
    currentOptionList=mainMenu
    while 0==0:
        choosingOptions(currentOptionList)