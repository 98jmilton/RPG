import Player
from Tools import parseInput,myPrint,choosingOptions,printRace
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
    if(myPrint(options)):pass
    raceChoice = parseInput('Enter choice or type \"stats [racename]\" to see each races stats').lower().split(' ')
    if raceChoice[0].lower() == 'stats':
        printRace(raceChoice[1])
        if(myPrint('cont')):pass
        raw_input()
        chosingRace()
    elif raceChoice[0].lower()== key in raceStats:
        if(myPrint('You chose: ', raceChoice[0])):pass
        player.race=raceChoice[0]
        if(myPrint('cont')):pass             
        raw_input()
    else:
        if(myPrint('\nError: check input')):pass
        chosingRace()
 
def chosingClass():
    if(myPrint('Class options:\n\t'+',\n\t'.join(classStats.keys['Name']))):pass
    classChoice = parseInput('Enter choice or type \"stats [classname]\" to see each classs stats').lower().split(' ')
    if classChoice[0] == 'stats':
        if(myPrint(classStats[classChoice[1]])):pass
        if(myPrint('cont')):pass
        raw_input()
        chosingClass()
    elif classChoice[0] in classStats.keys:
        if(myPrint('You chose: ', classChoice[0])):pass
        player.className=classChoice[0]
        if(myPrint('cont')):pass             
        raw_input()
    else:
        if(myPrint('\nError: check input')):pass
        chosingClass()

def playerDetails():
    raceChoice()
    if(myPrint(player)):pass


def editPlayer():
    if(myPrint('Edit player details:')):pass
    chosingRace()
    pass

def error():
    if(myPrint("ERROR\nWell that wasnt meant to happen...")):pass
    if(myPrint('cont')):pass
    choosingOptions(currentOptionList)

if __name__ == '__main__':
    createPlayer()
    currentOptionList=mainMenu
    while true:
        choosingOptions(currentOptionList)
