import pygame,sys,time,random
from Lists import raceStats

def myPrint(t):
    typing_speed = 150 #wpm
    if t == 'cont': t='Press enter to continue...'
    if t == '-':t=('-'*14)
    pygame.mixer.init()
    pygame.mixer.music.load('key.mp3')                        
    pygame.mixer.music.play()

    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    pygame.mixer.music.stop()
    print ''
    return True #Continues on finish

def parseInput(input):
    if(myPrint('-')):pass
    if(myPrint(input)):pass
    inputString = raw_input('=>')
    outString = inputString[:-1]
    if 'quit' in outString.lower(): sys.exit()
    if(myPrint('-')):pass
    return outString

def choosingOptions(input):
    if(myPrint('Current Options:')):pass
    myPrint('\n\t'+',\n\t'.join(input.keys))     

def printRace(input):
    pass

def printClass(input):
    pass
