

# # import array

# # num=array.array("i",[13,23,24,44])

# # print(num)



# # s='10'

# # print(str(s))

# # print(type(s))

# x = [1, 2, 3]
# y=x
# z = [1,2,3]
# print(x is y)      # True (same object)
# print(x is z)      # False (different objects but same content)
# print(x is not z)  # True
# print(id(x))
# print(id(y))
# print(id(z))


# x,y =2,4

# print((2+3)*4)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b


for i in range(0,51):
    if i%3==0 and i%5==0:
        print("fizz buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0 :
        print("buzz")
    else :
        print(i)
l=[1,2,3,4.5]
for i  in range(len(l)):
    if i%2!=0:
        print(l[i])

