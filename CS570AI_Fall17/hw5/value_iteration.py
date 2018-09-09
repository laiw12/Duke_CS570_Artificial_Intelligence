# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:37:45 2017

@author: Lai Wei
"""

##



'''
 reward matrix
 formart is as below:
                       drive      not drive
      top                2           3
     rolling             0           1
     bottom              0           1

'''

reward_matrix = [[0 for x in range(2)] for y in range(3)]
reward_matrix[0][0] = 2
reward_matrix[0][1] = 3
reward_matrix[1][0] = 0
reward_matrix[1][1] = 1
reward_matrix[2][0] = 0
reward_matrix[2][1] = 1

##print(reward_matrix)


## transition matrix (Drive)

''' 
            top       rolling    bottom 
top         0.9         0.1        0
rolling     0.3         0.6        0.1
bottom      0.6          0         0.4   



'''
drive_matrix = [[0 for x in range(3)] for y in range(3)]

drive_matrix[0][0] =  0.9
drive_matrix[0][1] =  0.1
drive_matrix[0][2] =  0


drive_matrix[1][0] =  0.3
drive_matrix[1][1] =  0.6
drive_matrix[1][2] =  0.1 

drive_matrix[2][0] =  0.6
drive_matrix[2][1] =  0
drive_matrix[2][2] =  0.4

##print(drive_matrix)

#3 not drive matrix
'''
            top     rolling      bottom
top        0.7       0.3           0
rolling      0        0            1
bottom       0        0            1


'''

not_drive_matrix = [[0 for x in range(3)] for y in range(3)]

not_drive_matrix[0][0] =  0.7
not_drive_matrix[0][1] =  0.3
not_drive_matrix[0][2] =  0

not_drive_matrix[1][0] =  0 
not_drive_matrix[1][1] =  0
not_drive_matrix[1][2] =  1

not_drive_matrix[2][0] =  0
not_drive_matrix[2][1] =  0
not_drive_matrix[2][2] =  1


## Start value literation process
discount_factor = 0.8

#literations
n = 40
## top rolling bottom (initial value)
v = [0,0,0]
v2 =[0,0,0]
ideal_policy =[0,0,0]
## state 
for k in range(n):
    for i in range(3):
        ## apply the value literation equation
        
        action_drive = reward_matrix[i][0] + discount_factor*( v[0]*drive_matrix[i][0]  +v[1] *  drive_matrix[i][1] +v[2]* drive_matrix[i][2] ) 
        action_not_drive = reward_matrix[i][1] + discount_factor*( v[0]*not_drive_matrix[i][0]  +  v[1] * not_drive_matrix[i][1] +v[2]* not_drive_matrix[i][2] )
        v2[i] = max(action_drive,action_not_drive)
      
        #record the policy
        if action_drive  == max(action_drive,action_not_drive):
            ideal_policy[i] = "drive"
        else:
            ideal_policy[i] = "not drive"
            
        
    v=v2.copy()
   
    print(ideal_policy)
    print(v2)
print("number of literation ",k) 






















