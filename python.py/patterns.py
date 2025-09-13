n = 5
for rows in range(1 , n +1 ):
    for cols in range( 1, rows+1):
        print("*" , end=" ")
    print()

for i in range (5 , 0, -1):
    print("* "*i)


n = 5
for rows in range(1 , n +1 ):
    for cols in range( 1, n+1):
        print("*" , end=" ")
    print()

m=5 

for i in range(1 , m+1):
    for j in range(1 , i+1):
        print(j,end=" ")
    print()

# m=5 

# for rows in range(1, 5):
#     if rows -1 :
#         print(rows , end=" ")


for i in range (5 , 0,-1 ):
    for j in range (1 , i+1):
        print(j , end=" ")
    print()


n=5
for rows in range(1 , n+1):
    for space in range(1 , n -rows+1):#
        print(" " , end="")
    for cols in range (1,2*rows):
        print("*", end="")
    print()

n=5
for rows in range(1 , n+1):
    for space in range(1 , n -rows+1):
        print(" " , end="")
    for cols in range (1,2*rows):
        print(cols, end="")
    print()

n=5 
for rows in range (1, n+1):
    for space in range(1 , rows+1):
        print(" ", end="")
    for cols in range(1 ,2*(n-rows)+2 ):#2*(5-1)+1=9->2*(5-2)+1=7
        print("*", end="")
    print()

n=5
for rows in range(1,n+1):
    for space in range (1,rows+1):
        print(" ", end="")
    for cols in range (1, 2*(n-rows)+2):
        print(cols,end="")
    print()

# for i in range(0, 51, 2):
#     print(i)