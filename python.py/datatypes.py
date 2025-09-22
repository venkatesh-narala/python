x=23
binary=bin(x)[-2:]
print(binary)

y=10
x=str(y)
print((y%2))
print(type(x))
print(id(y))
num=77
string_num=str(num)
print(type(string_num))
print(string_num)
string="nani"
print(string)


m=int(input("ente the number:")) 

for i in range(1 , m+1):
    for j in range(1 , i+1):
        print(j,end=" ")
    print()

l=[1,2,3,]
s={'nani','sai','babby'}

result=zip(l,s)
print(dict(result))


sr='rur'

if sr==sr[::-1]:
    print("paradalin")
    