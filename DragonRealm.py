# @author: Ama Freeman
# @date: Dec. 28, 2016
# @purpose: Create a random choice game where the player
#                  picks a cave and hops a dragon isn't in it.
# Created and source code from: "Invent Your Own Games with Python, 2nd Edition" by Al Sweigert
#

#Win Jingle from LittleRobotSoundFactory
# https://www.freesound.org/people/LittleRobotSoundFactory/

import random
import time
import sys, pygame

#pygame.init()
pygame.mixer.init()

HEARTBEAT = pygame.mixer.Sound('heartbeat.wav')
#WINJINGLE = pygame.mixer.Sound('spaceywin.wav')

def displayIntro():
    print('You are in a land full of dragons. In front of you, ')
    print('you see two caves. In one cave, the dragon is friendly ')
    print('and will share his treasure with you. The other dragon ')
    print('is greedy and hungry, and will eat you on sight.')

def chooseCave():
    cave = ' '
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave, winCounter):

    #start heartbeat sound
    HEARTBEAT.play()
    
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    HEARTBEAT.stop()
    
    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        #WINJINGLE = pygame.mixer.Sound('spaceywin.wav')
        #Play win Jingle
        #WINJINGLE.play()
        print('Gives you his treasure!')
        winCounter = winCounter + 1
        #WINJINGLE.stop()
        
    else:
        print('Gobbles you down in one bite! Game over!')

    return winCounter

playAgain = 'yes'
winCounter = 0
# Continuous Game Loop
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()

    caveNumber = chooseCave()

    winCounter = checkCave(caveNumber, winCounter)

    print('You have met ' ,winCounter, ' friendly dragons.')
    print('Do you want to play again? (yes or no)')
    playAgain = input()

print('Thanks for playing!')
