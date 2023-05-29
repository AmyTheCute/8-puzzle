import copy
from PrioQueue import *

class puzzle:
    def __init__(self, initial, final) -> None:
        self.initial = initial
        self.final = final 
        
    def solve(self):
        boardqueue = PQueue()
        curMove = board(self.initial, self.final)
        diff = curMove.getTotalInPlace()
        boards = [curMove]
        counts = 0
        
        while(diff != 0):
            moves = curMove.calcNextMove()
            for i in moves:
                boardqueue.push(i)
            curMove = boardqueue.pop()
            diff = curMove.getTotalInPlace()
            print(curMove)
            counts += 1

        return curMove
             
             
    def getDistance(self, a,b) -> int:
        """
        Get move distance between of number a and b. (Does not take location)
        """
        coorA = self.getLocation(a)
        coorB = self. getLocation(b)
        return abs((coorB[0] - coorA[0])) + abs((coorB[1] - coorA[1]))
    
    # Not used, for testing purposes.
    def getManhDiff(self, a):
        coorInt = self.getLocation(a, board= 0)
        coorFin = self.getLocation(a, board= 1)
        return abs((coorFin[0] - coorInt[0])) + abs((coorFin[1] - coorInt[1]))

    
    def getLocation(self, num, board=0):
        """
        Get coordinates of number

        :param int num: number
        :param int board: board=0: current board, board=1 Goal board.
        """
        for i in range(3):
            for j in range(3):
                if self.initial[i][j] == num and board == 0:
                    return i,j
                elif self.final[i][j] == num and board == 1:
                    return i,j
    
                
class board:
    def __init__(self, board, goal, parent = 0) -> None:
        self.board = board
        self.goal = goal
        self.distance = self.getTotalInPlace()
        
        if(type(parent) is not int): 
            self.parent = parent
        else: 
            self.parent = 0 
        
    def __eq__(self, other):
        return self.distance == other.distance
    
    def __lt__(self, other):
        return self.distance < other.distance
    
    def __le__(self, other):
        return self.distance <= other.distance
    
    def __repr__(self):
        returnstring = ""
        for i in self.board:
            for j in i:
                returnstring += str(j) + " "
            returnstring += "\n"
        returnstring += "diff: " + str(self.distance) + "\n"
        return returnstring
    
    def findNum(self, num = 0, isgoal = 0):
        for i in range(3):
            for j in range(3):
                if(self.board[i][j] == num and isgoal == 0):
                    return i,j
                elif((self.goal[i][j] == num) and isgoal == 1):
                    return i,j
    def genSwapedMove(self, a, b):
        newMove = copy.deepcopy(self.board)
        newMove[a[0]][a[1]], newMove[b[0]][b[1]] = newMove[b[0]][b[1]], newMove[a[0]][a[1]]
        return newMove
    
    # Checks if the move it was generated from matches this to avoid going back and forth
    def isParentMove(self, move):
        if(type(self.parent) != int):
            return self.parent.board == move
        else:
            return False
                
 #   def getManhDiff(self, item):
 #       coorInt = self.findNum(item)
 #       coorFin = self.findNum(item, 1)
 #       return abs((coorFin[0] - coorInt[0])) + abs((coorFin[1] - coorInt[1]))
    
    def getTotalInPlace(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if(self.goal[i][j] != self.board[i][j]):
                    distance += 1
        return distance
    
    def calcNextMove(self):

        zero = self.findNum()
        
        moves = [] # List of 2d arrays, not boards
        newCoor = [0,0]
        
        #Calculate Y axis moves
        if(zero[0] < 2):
            #Generate new Coordinate to move to
            newCoor[0] = zero[0] + 1
            newCoor[1] = zero[1]
            #Generate 2d array rep of new move
            moves.append(self.genSwapedMove(zero, newCoor))    
            # Check if it matches previous move
            if(self.isParentMove(moves[-1])): 
                del moves[-1]
                
        if(zero[0] >= 1):
            newCoor[0] = zero[0] -1
            newCoor[1] = zero[1]
            moves.append(self.genSwapedMove(zero, newCoor))
            if(self.isParentMove(moves[-1])): 
                del moves[-1]
        
        #Calculate X axis moves
        if(zero[1] < 2):
            newCoor[0] = zero[0] 
            newCoor[1] = zero[1] + 1
            moves.append(self.genSwapedMove(zero, newCoor))
            if(self.isParentMove(moves[-1])): 
                del moves[-1]
                
        if(zero[1] >= 1):
            newCoor[0] = zero[0]
            newCoor[1] = zero[1] - 1
            moves.append(self.genSwapedMove(zero, newCoor))
            if(self.isParentMove(moves[-1])): 
                del moves[-1]
        
        # Generate return list
        returnList = []
        for i in moves:
               returnList.append(board(i, self.goal, self))
               
        return returnList
    
    def getParentList(self):
        parents = [self.board]
        currBoard = self
        
        while(currBoard.parent != [ [ 1, 1, 1 ],  
                                [ 1, 1, 1 ],  
                                [ 1, 1, 1 ] ]):
            parents.append(currBoard.parent)
            currBoard = currBoard.parent