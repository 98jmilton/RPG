def myPrint(t):
    typing_speed = 150 #wpm
    if t == 'cont': t='Press enter to continue...'

    pygame.mixer.init()
    pygame.mixer.music.load('key.mp3')                        
    pygame.mixer.music.play()

    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    pygame.mixer.music.stop()
    print ''

def parseInput(input):
    myPrint(('-'*14)+'\n'+input)
    inputString = raw_input('=>')
    outString = inputString[:-1]
    if 'quit' in outString.lower(): sys.exit()
    myPrint('-'*14)
    return outString