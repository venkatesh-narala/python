# num=input("enter the number:")
# total=sum(int(digit)  for digit in num)
# print("sum of the digits =",total)

# #largest of three numbers
# a=int(input("enter first number :"))
# b=int(input("enter second number :"))
# c=int(input("enter thrid number :"))

# if a>=b and a>=c:
#     print("largest number is :",a)
# elif b>=a and b>=c:
#     print("largest number is :",b)
# else:
#     print("largest number is :",c)

# l=["nani","sai",12]
# # vowels=[ch for ch in l  if ch.lower() in "aeiou"]
# # print(vowels)
# l.reverse()
# print(l)
# l=[8,5,6,9,1]
# n=sorted(l,reverse=True)
# l.sort(reverse=True)
# print(l,"\n",n)


# a=int(input("enter first number:"))
# b=int(input("enter second number"))
# a=b
# b=a
# print(f"swap a ={a} \nswap b={b}")

# year=int(input("enter the year :"))

# if year%400==0:
#     print(f"{year} : leap year")
# elif year%100==0:
#     print(f"{year}: Not a leap year ")
# elif year%4==0:
#     print(f"{year} : leap year")
# else :
#     print(f"{year} not a leap year")



# numbers=list(map(int, input('enter the number separated by space:').split()))

# total=sum(numbers)

# average=total/len(numbers)

# print(f'sum = {total}')
# print("Average = {}".format(average))



# l1=[10,20,30]
# l2=[10,20,30]

# print("orignal list:")
# print(l1,'\n',l2)

# result=map(lambda x,y:x+y ,l1,l2)

# print(f"result : {list(result)}")



X=[[10,2,3],
   [12,3,4],
   [2,3,5]]

y=[[10,3,6],
   [4,8,9],
   [35,6,7]]

result=[[0,0,0],
   [0,0,0],
   [0,0,0]]
# print(len(X[0]))

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]=X[i][j]+y[i][j]

for r in result:
    print(r)