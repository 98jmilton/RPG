import Player,sys,time,random,Tools,Dicts
import pygame

# Global Variables
player=''
chnl=0
currentOptions=''


def createPlayer():
    player = Player.Player()
    player.name=parseInput('Please enter characters name: ')
    chosingRace()
        
def chosingRace():
    myPrint('Race options:\n\t'+',\n\t'.join(raceStats.keys))
    raceChoice = parseInput('Enter choice or type \"stats [racename]\" to see each races stats').lower().split(' ')
    if raceChoice[0] == 'stats':
        myPrint(raceStats[raceChoice[1]])
        myPrint('cont')
        raw_input()
        chosingRace()
    elif raceChoice[0] in raceStats.keys:
        myPrint('You chose: ', raceChoice[0])
        player.setRace(raceChoice[0])
        myPrint('cont')             
        raw_input()
    else:
        myPrint('\nError: check input')
        chosingRace()

def editPlayer():
    myPrint('Edit player details:')

    pass

if __name__ == '__main__':
    createPlayer()
