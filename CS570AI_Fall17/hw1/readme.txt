For this question, I constructed two seperated files:
15puzzle.py ----------------Question 1
queen.py   -----------------Question 2

You have to run two files seperately to get each results.

Both file are excutable on Spyder(Python 3.6). ( You can find Spyder in anoconda 3)
Both files contain sample inputs from course website and if you just hit the run button,
the sample results will be displayed in the console and an output file will also be generated in
the same folder.





Instructions for 15puzzle.py:

For this file, the only thing you can modify is at the most upper part of the file.
You can change the input file name with test cases and output file name with the name you want.
After that, you just need to hit the run button and results will be displayed in the console and an output 
file will also be generated inthe same folder.

In my personal experiment, all test cases from course website retun the correct results.



Logics for the this program (15puzzle.py):

The data structure of my program is python list : [node,f(n),g(n),parent]
where f(n) is the fcost and g(n) is the g(cost). Parent is the node's previous node which is
used to backtrack and construct the path.


For this question, I use the sum of knight moves of each square of the board as my heuristic function.
To implement this function, I make use of the knight_distance.txt file from course website and the modified
version is saved as knight_distance.txt in the same folder. This file must be in the same folder so that the program
is executable.


I think my code is well commented so if you want to know the detail of a particualr function, please the the comment.
In my Astar function, if the firnge the not empty, the lowest f(n) score node is chosen and it's successors are
expanded and put in the fringe. The f(n) and g(n) are updated each loop and the parent is also stored.







Instructions for queen.py

For this file, the only thing you can modify is also at the most upper part of the file.
You can change the value of n and hit the run button. n is set to 7 by default in my program and
feel free to modify it. After that results will be displayed in the console and an output file will also be generated in
the same folder.

For this question, I am using Python list as my fringe. As a result, the performance of my searching algorithm is exteremely 
slow when n gets larger. The reason is that the lowfscore function will go through a large number of elements in my openset(fringe) each time
to return the lowest f(n) node. I've wrote some code to improve the efficency:

Below is a short picture for the time it takes run the program for n:

n = 7  about 5 seconds
n = 11 about 5 seconds
n = 18 about 10 seconds 
n = 19 about 4 minutes
n >=20 more than 20 minutes


PS. I tried the piority version suggested on Piazza and it is still not fast enough.


Logics for this program(queen.py):

I use the same data structure as the 15puzzle problem, that is [node,f(n),g(n),partent].
The logic is bassically the same as the 15puzzle except the heurisitc function:
my heurisitic function for this problem is to calculate the number of pairs that can attack each other ( either diagonally or based on knight moves)
The details of the functions can be found in the comment in my code. 
I modified the search algorithm to improve the efficiency: my search algorithm tend to expand nodes with 0 cost that are newly added to fringe.

















