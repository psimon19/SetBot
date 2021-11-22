# Python program to find all subsets of a set
# A set is defined by Color + Shading + Symbol + Number
#   Example: Solid double green diamond  = "gsd2"
#            Lined single green squiggle = "gld1"
#            Open triple green oval      = "god3"
#
#   Color: Red ("r"), Green ("g"), Purble ("p")
#   Shading: Open ("o"), Lined ("l"), Solid ("s")
#   Symbol: Oval ("o"), Diamond ("d"), Squiggle ("s")
#   Number: "1", "2", "3"

import itertools
import random
import time

# finds all subsets of length n
def findSubsets(s, n):
    return list(itertools.combinations(s,n))

# returns True if valid set, else returns False
def checkSet(setList):
    checkSetCount = 0
    for i in range(4):
        if ((setList[0][i] == setList[1][i] and setList[0][i] == setList[2][i] and setList[1][i] == setList[2][i]) or (setList[0][i] != setList[1][i] and setList[0][i] != setList[2][i] and setList[1][i] != setList[2][i])):
            checkSetCount += 1
    
    if (checkSetCount == 4):
        return True
    else:
        return False

# n is the number of cards to generate on the board
# returns a list of cards
def randomBoardGenerator(n):
    color  = ['r', 'g', 'p']
    shade  = ['o', 'l', 's']
    symbol = ['o', 'd', 's']
    number = ['1', '2', '3']
    
    cardList = []
    for i in range(n):
        card = color[random.randint(0, 2)] + shade[random.randint(0, 2)] + symbol[random.randint(0, 2)] + number[random.randint(0, 2)]
        while (card in cardList):
            card = color[random.randint(0, 2)] + shade[random.randint(0, 2)] + symbol[random.randint(0, 2)] + number[random.randint(0, 2)]
            
        cardList.append(card)
    return cardList
    
def fullBoardGenerator():
    color  = ['r', 'g', 'p']
    shade  = ['o', 'l', 's']
    symbol = ['o', 'd', 's']
    number = ['1', '2', '3']
    
    cardList = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    card = color[i] + shade[j] + symbol[k] + number[l]
                    cardList.append(card)
    return cardList
    

if __name__ == '__main__':
    print("Set Recognition Script")
    start_time = time.time()
    
    setBoard = randomBoardGenerator(81)
    subsetList = findSubsets(setBoard, 3)
    print(len(subsetList))
    
    validSetList = []
    for subset in subsetList:
        if (checkSet(subset)):
            validSetList.append(subset)
    
    print ("Game board:\n==================")
    for i in range(0, len(setBoard) - 2, 3):
        print (setBoard[i] + "   " + setBoard[i + 1] + "   " + setBoard[i + 2])
        print ("\n")
    print ("==================")
    print (str(len(validSetList)) + " valid sets on the board")
    print (validSetList)
    print("Execution time: %s seconds" % (time.time() - start_time))
    print ("\n\n")
    
    fullBoard = fullBoardGenerator()
    for i in range(len(fullBoard)):
        print(fullBoard[i])
    
    