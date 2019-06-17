import Player
from Tools import parseInput,myPrint,choosingOptions
from Lists import raceStats,mainMenu
# Global Variables
player=Player.Player()
currentOptionList=''


def createPlayer():
    player.name=parseInput('Please enter characters name: ')
    chosingRace()
        
def chosingRace():
    options='Race options:'
    for key in raceStats:
        options+='\n\t'+key+','
    myPrint(options)
    raceChoice = parseInput('Enter choice or type \"stats [racename]\" to see each races stats').lower().split(' ')
    if raceChoice[0].lower() == 'stats':
        myPrint(raceStats[raceChoice[1]])
        myPrint('cont')
        raw_input()
        chosingRace()
    elif raceChoice[0].lower() in raceStats.keys:
        myPrint('You chose: ', raceChoice[0])
        player.race=raceChoice[0]
        myPrint('cont')             
        raw_input()
    else:
        myPrint('\nError: check input')
        chosingRace()

def chosingClass():
    myPrint('Class options:\n\t'+',\n\t'.join(classStats.keys))
    classChoice = parseInput('Enter choice or type \"stats [classname]\" to see each classs stats').lower().split(' ')
    if classChoice[0] == 'stats':
        myPrint(classStats[classChoice[1]])
        myPrint('cont')
        raw_input()
        chosingClass()
    elif classChoice[0] in classStats.keys:
        myPrint('You chose: ', classChoice[0])
        player.className=classChoice[0]
        myPrint('cont')             
        raw_input()
    else:
        myPrint('\nError: check input')
        chosingClass()

def playerDetails():
    raceChoice()
    print(player)


def editPlayer():
    myPrint('Edit player details:')
    chosingRace()
    pass

def error():
    myPrint("ERROR\nWell that wasnt meant to happen...")
    myPrint('cont')
    choosingOptions(currentOptionList)

if __name__ == '__main__':
    createPlayer()
    currentOptionList=mainMenu
    while true:
        choosingOptions(currentOptionList)
