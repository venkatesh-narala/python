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