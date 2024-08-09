//...................................PATTERN PROBLEMS.............................................

Q:1 Pattern problem

for i in range(1, 6):
    print(" "*(5-i),end="")
    for j in range(i, i+i):
        print(j%2, end=" ")
    print()
    
OUTPUT:

    1 
   0 1 
  1 0 1 
 0 1 0 1 
1 0 1 0 1     
    
    
Q:2 Pattern problem    

for i in range(5, 0, -1):
    print(' ' * (5 - i), end='')
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
    
OUTPUT:

5 4 3 2 1 
 4 3 2 1 
  3 2 1 
   2 1 
    1 
    
    
Q:3 Pattern problem     

for i in range(1,6):
    print(" "*(5-i),end="")
    for j in range(i,0,-1):
        print(j,end='')
    print()
    
OUTPUT:

    1
   21
  321
 4321
54321       


Q:4 Pattern problem     

for i in range(1,6):
    print(" "*(5-i),end="")
    for j in range(i, i+i):
        print(j%2, end=" ")    
    print()    
for i in range(5,0,-1):
    print(' ' * (5 - i), end='')
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()  
    
OUTPUT:

    1 
   0 1 
  1 0 1 
 0 1 0 1 
1 0 1 0 1 
5 4 3 2 1 
 4 3 2 1 
  3 2 1 
   2 1 
    1 
    
 
