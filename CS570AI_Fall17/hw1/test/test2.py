# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:37:12 2017

@author: laiw1
"""



'''

## returns the minimum number of knight moves
def knight_distance(a1,b1,a2,b2):
    file = open("knight_distance.txt")
    for line in file:
        line = line.split("  ")
    knight_distance = line
    i = a1*4 +b1
    j = a2*4 +b2
    return int(knight_distance[16*i+j])
    




def locateposition(goal,n):
    for i in range(4):
        for j in range(4):
            if goal[0][i][j] == n:
                return [i,j]
            
            

def hcost(start,goal):
    dist = 0
    for i in range(4):
        for j in range(4):
            for k in range(15):
                if start[0][i][j] == k+1:
                    location = locateposition(goal,k+1)
                    dist = dist+ knight_distance(i,j,location[0],location[1])
    return dist
                    
                    
          
'''  







## print the board in the console
def printboard(board):
    for i in range(4):
        for j in range(4):
            print(str(board[0][i][j])+" ",end="")
            
        print("")








### input the intial board based on the question

### create empty board
Board = [[0 for x in range(4)] for y in range(4)]

Board[0][0]=10
Board[0][1]=11
Board[0][2]=3
Board[0][3]=13
Board[1][0]=5
Board[1][1]=4
Board[1][2]=1
Board[1][3]=2
Board[2][0]=9
Board[2][1]=8
Board[2][2]=6
Board[2][3]=12
Board[3][0]=0
Board[3][1]=14
Board[3][2]=15
Board[3][3]= 17

Board = [Board] + [0,0,0]




## input the Goal Board
GoalBoard = [[0 for x in range(4)] for y in range(4)]


GoalBoard[0][0]=1
GoalBoard[0][1]=2
GoalBoard[0][2]=3
GoalBoard[0][3]=4
GoalBoard[1][0]=5
GoalBoard[1][1]=6
GoalBoard[1][2]=7
GoalBoard[1][3]=8
GoalBoard[2][0]=9
GoalBoard[2][1]=10
GoalBoard[2][2]=11
GoalBoard[2][3]=12
GoalBoard[3][0]=13
GoalBoard[3][1]=14
GoalBoard[3][2]=15
GoalBoard[3][3]=0

print()
GoalBoard = [GoalBoard] +[0,0,0]



# loate the empty square on the board
def locatezero(board):
    for i in range(4):
        for j in range(4):
            if board[0][i][j] == 0:
                return [i,j]
    else:
        print("Error, no empty space on board is found")
        


## copy the list to aviod memory issues
def copy2(board):
    result = [[0 for x in range(4)] for y in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = board[0][i][j]
    
    return [result] +[ board[1],board[2],board[3]]
            


## find possible moves of the current board
def findmoves(board):
    empty = locatezero(board)
    i = empty[0]
    j = empty[1]
    a = i-2
    b = i+2
    c = j+1
    d = j-1
    e = i-1
    f = i+1
    g = j+2
    h = j-2
    check =[a,b,c,d,e,f,g,h]
   
    for i in range(len(check)):
        if check[i]>=4 or check[i]<0:
            check[i] = "null"
    
    output1 = [[check[0],check[2]],[check[0],check[3]],[check[1],check[2]],[check[1],check[3]]]
    output2 = [[check[4],check[6]],[check[4],check[7]],[check[5],check[6]],[check[5],check[7]]]
    output = output1 + output2
    
   
    result=[]
    for m in range(len(output)):
        if( output[m][0] !="null") and (output[m][1] != "null"):
                result += [[output[m][0],output[m][1]]]
    return result
            
# my H function
def misplaced(board):
    count = 0
    for i in range(4):
        for j in range(4):
            if board[0][i][j] != GoalBoard[0][i][j]:
                if board[0][i][j]==0:
                    continue
                count+=1
    return count



# return the a new board after placed the move
def placemove(board,location):
    copy=copy2(board)
    a = locatezero(copy)
    copy[0][a[0]][a[1]] = copy[0][location[0]][location[1]]
    copy[0][location[0]][location[1]]=0
    return copy
    
 # given the board, return the possible nodes in the next layer      
def generatesuccessors(board):
    result =[]
    possiblemoves = findmoves(board)
    for i in range(len(possiblemoves)):
        result = result + [placemove(board,possiblemoves[i])]
        
    return result




## return the lowest node fscore in openset

def lowfscore(openset):
    scorelist = [-5 for x in range(len(openset))]
    for i  in range(len(openset)):
        scorelist[i] = openset[i][1]
    
    a = min(scorelist)
    for i in range(len(scorelist)):
        if a == scorelist[i]:
            return openset[i]




## counstruct the path from recorded list
def constructpath(recordlist,current):
    path = [current]

    while path[-1][0] != Board[0]:
        for i in range(len(recordlist)):
            if recordlist[i][0] == current[3]:
                path = path + [recordlist[i]]
                current = recordlist[i]
              
                break
      
    return path
    
    
def astar():
    # construct the first fscore
    Board[1] = misplaced(Board)
    openset = [Board]
    closeset = []
    
    recordlist= []
  
    while len(openset)!=0:
        
        ## return the lowest fscore in the openset
        current = lowfscore(openset)
        
        
        if current[0] == GoalBoard[0]:
            
            ## find the solution, rebuild the path
            path =constructpath(recordlist,current)
            
            
            for i in range(len(path)):
                printboard(path[len(path)-i-1])
                print()
            
            print("the length of the states is (including initial and goal states): " + str(len(path)))
            print("mission accomplished")
            break
        
        openset.remove(current)
        closeset.append(current)
        
        ## generate children
        children = generatesuccessors(current)
        
        for i in range(len(children)):
            if children[i] in closeset:
                continue
            if children[i] not in openset:
                openset.append(children[i])
                
         
            
            ## update the value
            children[i][2] = current[2]+ 1
            children[i][1] = children[i][2] + misplaced(children[i])
            children[i][3] = current[0]
            recordlist = recordlist + [children[i]]
    
    return "Failure"
                
                
            
        
astar()
            

    
    




















