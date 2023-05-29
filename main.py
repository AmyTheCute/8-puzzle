from board import *
from PrioQueue import *
import random

initial = [ [ 1, 2, 3 ],  
            [ 5, 6, 0 ],  
            [ 7, 8, 4 ] ]  

final = [ [ 1, 2, 3 ],  
        [ 5, 8, 6 ],  
        [ 0, 7, 4 ] ]  

firstBoard = puzzle(initial, final)


print("original board: ")
print(initial)

moves = firstBoard.solve()

print("Solved puzzle: ")
print(moves)
