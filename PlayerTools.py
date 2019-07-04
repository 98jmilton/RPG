from Main import player
from Tools import *

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
        error()
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
        myPrint('You chose:')
        printClass(player.classType)
    # Input has no matches
    else:
        error()
        chosingClass()

def editPlayer():
    if(myPrint('Edit player details:')):pass
    chosingRace()
    pass

def playerDetails():
    if(myPrint(player)):pass

def printRace(input):
    race=raceStats[input]
    output='Race name: '+race['Name']
    output+='\nDescription: '+race['Description']
    for stat in stats:
        output+='\n\t'+stat+': '+str(race[stat])
    myPrint(output)
    myPrint('-')

def printClass(input):
    className=classStats[input]
    output='Race name: '+className['Name']
    output+='\nDescription: '+className['Description']
    for stat in stats:
        output+='\n\t'+stat+': '+str(race[stat])
    myPrint(output)
    myPrint('-')