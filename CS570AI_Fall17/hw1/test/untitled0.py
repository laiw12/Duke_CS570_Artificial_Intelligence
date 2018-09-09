# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 22:58:27 2017

@author: laiw1
"""





def printboard(board):
    for i in range(4):
        for j in range(4):
            print(str(board[i][j])+" ",end="")
            
        print("")








### input the intial board based on the question

### create empty board
Board = [[0 for x in range(4)] for y in range(4)]

Board[0][0]=1
Board[0][1]=2
Board[0][2]=12
Board[0][3]=13
Board[1][0]=5
Board[1][1]=6
Board[1][2]=7
Board[1][3]=8
Board[2][0]=9
Board[2][1]=3
Board[2][2]=4
Board[2][3]=0
Board[3][0]=11
Board[3][1]=14
Board[3][2]=15
Board[3][3]=10

Board


###
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




## find the location of zero
def locatezero(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return [i,j]
    else:
        print("Error, no empty space on board is found")
        
    

## copy the list to aviod memory issues
def copy2(board):
    result = [[0 for x in range(4)] for y in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = board[i][j]
    
    return result
            
    



## find all valid move locations that can move to 0
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
            
## find the number of misplaced tiles.        (h score)
def misplaced(board):
    count = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != GoalBoard[i][j]:
                if board[i][j]==0:
                    continue
                count+=1
    return count
                           

# return the a new board after placed the move
def placemove(board,location):
    copy=copy2(board)
    a = locatezero(copy)
    copy[a[0]][a[1]] = copy[location[0]][location[1]]
    copy[location[0]][location[1]]=0
    return copy
    
 # given the board, return the possible nodes in the next layer      
def generatesuccessors(board):
    result =[]
    possiblemoves = findmoves(board)
    for i in range(len(possiblemoves)):
        result = result + [placemove(board,possiblemoves[i])]
     
    return result

   
def scorelist(boardlist):
    score = [-5 for x in range(len(boardlist))]
    for i in range(len(boardlist)):
        score[i] = misplaced(boardlist[i])
    return score


def lowhscoreindex(boardlist):
    score = scorelist(boardlist)
    a = min(score)
    for i in range(len(score)):
        if a ==score[i]:
            return i 
    


        
        

    
    

        
    









print()
print("====================================================================")
print("test cases inspection:")

print("initial board:")
printboard(Board)
print()
print("GoalBoard:")
printboard(GoalBoard)
print()
a = generatesuccessors(Board)
print("successors of initial board:")
printboard(a[0])
print()
printboard(a[1])
print()
printboard(a[2])
print()
print("fscores for successors:")
print(scorelist(a))
print()
print("low score index:")
print(lowscoreindex(a))


print("======================================================================")











def astar():
    visited =[]
    unvisited =[Board]
    
    
    while len(unvisited)!=0:
        q = lowscoreindex(unvisited)
        unvisited.remove(q)
        successors = generatesuccessors(q)
        for i in range(len(successors)):
            if successors == GoalBoard:
                return
        
            
            







    
    
    
    
    
    


    
    
    
    
    
    
    
    
    







              
            

            
    

##a =locatezero(Board)
##print(findmoves(a[0],a[1]))

    
    
        
        
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
