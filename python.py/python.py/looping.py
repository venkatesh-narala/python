
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("fizz buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
 
print(f"using a enumerate method")

list=[2,5,6,4,9,8]
for key ,value   in enumerate(list) :
    if key%2 !=0:
        print(key)
    

print(f"using a range method")
list=[2,5,6,4,9,8]
for i   in range(len(list)) :
    if i%2 !=0:
        print(list[i])

i=0
while i<=10 :
    i+=1
    print(i)

while True:

    s=11

    if s==10:
        print("s==10")
        break

    elif s!=10:
        print("s!=10")
        break



