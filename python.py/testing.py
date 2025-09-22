# import dict

# print(dict.add(5, 3))  # 8
# print(dict.sub(10, 4)) # 6
# # /

# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("nani")
#     elif i%5==0:
#         print('sai')
#     else :
#         print(i)


# list=[2,5,6,4,9,8]
# for i   in range(len(list)) :
#     if i%2 ==0:
#         print(list[i])

# def add(a,b=5):
#     return a,b
# print(add(4,3))


# y=x=z = (1, 2 )   # same as (x, y) = (1, 2)
# print(x)
# # Output: 1 2
# print(type(z))

# (a,b)=(1,2)
# print(type(a))

# a=9
# b=2
# result=a//b
# print(result)

# l=[1,2,3,4]

# t1=tuple(l)
# print(t1)

# def divide(x, y):
#     return (x // y, x % y)   # quotient, remainder

# q, r = divide(10, 3)
# print(q, r)  # 3 1
t=(1,2,3,4,5)
gen=(x*x for x in t)
tup=tuple(gen)
print(tup)


def divide(x,y):
    return x//y,x%y
print(divide(3,4))
i=2
if i%2==0 or i!=2:
    print(i)

d = {1: "one", 2: "two", 1: "duplicate", 1:"another"}

d.update({1:"nani"})
print(d)   # {1: 'duplicate', 2: 'two'}

print(d.get(1))
colors = {"red", "green", "blue" , "yellow"}
for c in colors:
    print(c)
