# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:19:29 2017

@author: laiw1
"""

from  itertools import combinations 



#############################
# Here is the only thing you can modify in this program
# change the value of n to get different optimal results
n= 7
# change the output file name here
outputfile = open("queen_output.txt",'w')



#############################






# write results to files

def writeboard(board,file):
    for i in range(len(board[0])):
        for j in range(len(board[0])):
         
                file.write(str(board[0][i][j])+" ")
         
        
        
        file.write("\n")
    file.write("\n")
        




# construct the board
def construct_queen(n):
    Board = [[0 for x in range(n)] for y in range(n)]
    return [Board] + [0,0,0]

# print the board
def printboard(board):
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            print(str(board[0][i][j])+" ",end="")
            
        print("")
        
# copy the board itself       
def copy2(board):
    result = [[0 for x in range(len(board[0]))] for y in range(len(board[0]))]
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            result[i][j] = board[0][i][j]
    
    return [result] +[ board[1],board[2],board[3]]
            
  
# find rows and columns that does not contain queens ( hard  constraint)
def findrc(board):
    rows = []
    columns=[]
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[0][i][j] == 1:
                rows = rows + [i]
                columns = columns + [j]
    return[rows] +   [columns]


# find columns that does not contain queens

def findmoves(board):
    hardc = findrc(board)
    rows = hardc[0]
    columns = hardc[1]
  
    playablecolumns = -100
    playablemoves = []
    
    if (len(rows)== len(board[0])) or ( len(columns))==len(board[0]):
        return "done"
    
    
    for i in range(len(board[0])):
        if i not in columns:
            playablecolumns = i
          
            break
    for i in range(len(board[0])):
        if i not in rows:
          
            playablemoves = playablemoves + [ [i,playablecolumns]]
    
    
    return playablemoves
    
    
    
# place the move on the board based on selected loaction
def placemove(board,location):
    copy=copy2(board)
    
    copy[0][location[0]][location[1]] = 1
    
    
   



    return copy
    
    
# generate the possible children
def generatesuccessors(board):
    result =[]
    possiblemoves = findmoves(board)
    for i in range(len(possiblemoves)):
        result = result + [placemove(board,possiblemoves[i])]
        
    return result

 
 # returns a list of index that queens are located   
def locate_queens(board):
    index = []
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[0][i][j] ==1: 
                index = index + [[i,j]]
    return index



                
# calculate the number of pairs that can attack each other
def h_cost(board):
    dcost =0
    kcost =0
    index =locate_queens(board)
   
    c= list(combinations(index,2))
  
    for i in range(len(c)):
        
        ## (x,y) and (a,b) are on the same diagonal if  |x-a| = |y-b|
        ## (x,y) and (a,b) are on the knight attack move if  their abolute difference is equal to [1,2] or [2,1]
        
        x = abs(c[i][0][0]- c[i][1][0])
        y = abs(c[i][0][1] -c[i][1][1])
        
        # diagonal_ attack 
        if x==y:
            dcost = dcost + 1
        # knight attack 
        if ([x,y] ==[1,2] )or ([x,y] == [2,1]):
            kcost = kcost + 1
    
    return kcost + dcost

        

            
        


## return the lowest node fscore in openset

def lowfscore(openset):
    scorelist = [-5 for x in range(len(openset))]
    for i  in range(len(openset)):
       
        ## if it already has the lowest score, stop and return. this will improve the performance of the searching
        if openset[len(openset)-i-1][1] ==0:
        
            return openset[len(openset)-i-1]
        scorelist[i] = openset[i][1]
    
    a = scorelist.index(min(scorelist))
    return openset[a]



## counstruct the path from recorded list (for this question, we dont need to trach back the path)
## if we every needed to track the path, just update this method
def constructpath(recordlist,current):
    
    path = [current]
   
      
    return path


# doing A star search
def astar(n):
    # construct the first fscore
    Board = construct_queen(n)
    Board[1] = 0
    openset = [Board]
    closeset = []
    recordlist= []

    while len(openset)!=0:
  
      
      
        
        ## return the lowest fscore in the openset
        current = lowfscore(openset)
        if findmoves(current)=="done":
            ## find the solution, rebuild the path （backing tracking)
            ## in this question, only the optimal solution is stored in the path
            path =constructpath(recordlist,current)
            # print result to console and write it to the txt file
            for i in range(len(path)):
                printboard(path[len(path)-i-1])
                writeboard(path[len(path)-i-1],outputfile)
                print()
            
            outputfile.write("the number of pairs attack each other is: "+str(h_cost(current)))
            outputfile.close()
            print("the number of pairs attack each other is: "+str(h_cost(current)))
         
            print("mission accomplished")
            return current

        openset.remove(current)
        closeset.append(current[0])
    
        ## generate children
        children = generatesuccessors(current)
        
        for i in range(len(children)):
            #if children[i][0] in closeset:
              #  continue
         #   if children[i] not in openset:
            openset.append(children[i])
              
              
                
            cost = h_cost(children[i])
        
            ## in this question, g(n) = 0
            children[i][2] = 0
            ## update the h(n)  (number of pairs that can attack each other)
            children[i][1] = children[i][2] + cost
            children[i][3] = current[0]
            recordlist = recordlist + [children[i]]
            
     
    
    return "No solutions Found"
                
    
    
astar(n)
    
    
    
    
    
    
    
    
    
        
            
   
        
        
    
            















    
    
            
            
    
















    
