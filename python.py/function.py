# # x=2
# # y=7
# # print(x&y)

# def fact (num):
#     if num==1:
#         return 1
#     return num*fact(num-1)#recursion method 
# n=int(input("enter the number:"))
# result=fact(n)
# print(f"{n} factorial is {result}")

# def decimal_to_binary(n):
#     if n==0:
#         return ""
#     else:
#         return decimal_to_binary(n//2)+str(n%2)#recursion method 
    
# num=int(input("enter the number:"))

# if num==0:
#     print("binary:",0)
# else :
#     print("binary:",decimal_to_binary(num))


# def fib(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     else:
#         for i in range(n):
#             print(a,end=" ")
#             c=a+b
#             a=b
#             b=c
#             # a, b = b, a + b
# n=int(input("enter the number:"))
# fib(n)



# n=int(input("Enter the number"))
# def prime_number(num):
    
#     if num<=1:
#         print(f"{num} is not a prime number")
        
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is pirme number")
# prime_number(n)


def func(**a):
    for key ,value in a.items():
        print(f'{key}:{value}')
    # print(a)
func(a='nani',b='sai')

def fib(num):

    if num==1 or num==2:
        return 1
    else:
        return (fib(num-1)+fib(num-2))
print(fib(3))
# n=7
# for i in range(1,n+1):
#     print(fib(i),end=" ")

print(pow(2,3))



def fun():
    x=19
    y=1.7
    z='nani'
print(fun.__code__.co_nlocals)

x=19
y=1.7
z='nani'

def fun():
    return x+y

print(len(fun.__code__.co_names))



def get_permutation(string,i=0):
    if i==len(string):
        print("".join(string))
    for j in range(i , len(string)):
        words=[c for c in string]
        words[i],words[j]=words[j],words[i]
        get_permutation(words ,i+1 )
get_permutation('run')

s='nani'
wordss=list(s)
print(wordss)


import numpy as np

# data=[10,29,37,48,789]
# data=np.array('i',[29,37,48,789])

# mean_value=np.mean(data)

# print(mean_value)

print(np.__version__)
array=np.array([18,38,49,5 ], dtype=int)
print(array)
print(type(array))
print(np.mean(array))
median_value=np.median(array)
print(median_value)


# li=[10,40,30,20]
s='nani'

median=list(sorted(s))
print(median)


# median using without libraries

data=[10,30,20,40]

data.sort()

n=len(data)

if n%2==1:
    mid=data[ n//2]
else :
    mid1=data[n//2 -1]
    mid2=data[n//2]
    mid=(mid1+mid2)/2

print('Data:',data)
print('Median:',mid)



l2=[10,20,30,10,10]

count={}

for i in l2:

    if i in count:
        count[i]+=1
    else:
        count[i]=1

mode_value=max(count , key=count.get)


print(mode_value)   