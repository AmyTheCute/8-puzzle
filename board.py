import copy

class puzzle:
    def __init__(self, initial, final) -> None:
        self.initial = initial
        self.final = final
        
    def getDistance(self, a,b):
        coorA = self.getLocation(a)
        coorB = self. getLocation(b)
        return abs((coorB[0] - coorA[0])) + abs((coorB[1] - coorA[1]))
    
    def getManhDiff(self, a):
        coorInt = self.getLocation(a, board= 0)
        coorFin = self.getLocation(a, board= 1)
        return abs((coorFin[0] - coorInt[0])) + abs((coorFin[1] - coorInt[1]))

    def getLocation(self, num, board=0):
        for i in range(3):
            for j in range(3):
                if self.initial[i][j] == num and board == 0:
                    return i,j
                elif self.final[i][j] == num and board == 1:
                    return i,j
    
    def __repr__(self):
        print("Current Board: ")
        for i in self.initial:
            print(i)
        print("Goal Board: ")
        for i in self.final:
            print(i)
                
                
    def getManhTotal(self):
        totalman = 0
        for i in range(3):
            for j in range(3):
                totalman += self.getManhDiff(self.initial[i][j])
        return totalman
                
class board:
    def __init__(self, board, goal, parent = 0) -> None:
        self.board = board
        if(parent != 0): 
            self.parent = parent
        else: 
            self.parent = [ [ 1, 1, 1 ],  
                                [ 1, 1, 1 ],  
                                [ 1, 1, 1 ] ] 
        self.goal = goal
        self.distance = self.getManhTotal()
        
    def __eq__(self, other):
        return self.distance == other.distance
    
    def __lt__(self, other):
        return self.distance > other.distance
    
    def __le__(self, other):
        return self.distance >= other.distance
    
    def __repr__(self):
        returnstring = ""
        for i in self.board:
            for j in i:
                returnstring += str(j) + " "
            returnstring += "\n"
        returnstring += "Manh diff: " + str(self.distance)
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
    
    # Checks if the move it was generator from matches this to avoid going back and forth
    def isParentMove(self, move):
        for i in range(3):
            for j in range(3):
                if(self.parent[i][j] != move[i][j]):
                    return False
                
        return True
                
    def getManhDiff(self, item):
        coorInt = self.findNum(item)
        coorFin = self.findNum(item, 1)
        return abs((coorFin[0] - coorInt[0])) + abs((coorFin[1] - coorInt[1]))
    
    def getManhTotal(self):
        totalman = 0
        for i in range(3):
            for j in range(3):
                #totalman += self.getManhDiff(self.board[i][j])
                if(self.goal[i][j] == self.board[i][j]):
                    totalman += 1
        return totalman
    
    def calcNextMove(self):
        zero = self.findNum()
        
        #hack way to create an array of 2d lists
        moves = [self.board[:], self.board[:]]
        del moves[-1]
        del moves[-1]
        newCoor = [0,0]
        
        #Calculate Y axis moves
        if(zero[0] < 2):
            newCoor[0] = zero[0] + 1
            newCoor[1] = zero[1]
            moves.append(self.genSwapedMove(zero, newCoor))
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
        returnList = []
        for i in moves:
               returnList.append(board(i, self.goal, self.board))
               
        return returnList
    