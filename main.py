from board import *
from PrioQueue import *
import random

initial = [ [ 1, 2, 3 ],  
            [ 5, 6, 0 ],  
            [ 7, 8, 4 ] ]  

final = [ [ 1, 2, 3 ],  
        [ 4, 5, 6 ],  
        [ 7, 8, 0 ] ]  

firstBoard = board(initial, final)
boardqueue = PQueue()

print("original board: ")
print(firstBoard)

curMove = firstBoard
diff = firstBoard.getManhTotal()
counts = 0

while(diff != 0):
    moves = curMove.calcNextMove()
    for i in moves:
        boardqueue.push(i)
    curMove = boardqueue.pop()
    diff = curMove.getManhTotal()
    print("Current move: ")
    print(curMove)
    counts += 1
    
print(curMove)
print("Goal found with " + str(counts) + " Moves")
    