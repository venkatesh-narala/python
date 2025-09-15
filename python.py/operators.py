# num=int(input("enter the number:"))
# temp=num

# length=len(str(num))
# sum1=0
# while num!=0:
#     r=num%10
#     sum1=sum1+(r**length)
#     num=num//10
# if sum1==temp:
#     print("armstrong number")
# else :
#     print("not armstrong number")

# using for loop check armstrongnumbers
# class Armstorngchecker:
#     def __init__(self,number):
#         self.number=number
#     def is_armstrong(self):
#         num_str=str(self.number)
#         power=len(num_str)
#         number=self.number
#         total=0
#         for digits in num_str:
#             total+=int(digits)**power
#         return total==number
# if __name__=="__main__":
#     num=int(input("enter the number:"))
#     checker=Armstorngchecker(num)

#     if checker.is_armstrong():
#         print(f"{num} is a arm strong number")
#     else :
#         print(f"{num} is  not a arm strong number")

# #using while loop
# class Armstorngchecker:
#     def __init__(self,number):
#         self.number=number
        
#     def is_armstrong(self):
#         temp=self.number
#         num_str=len(str(self.number))
#         temp_num=self.number
#         total=0
#         while temp_num!=0:
#             r=temp_num%10
#             total+=(r**num_str)
#             temp_num=temp_num//10

#         return total==temp

# if __name__=="__main__":
#     num=int(input("enter the number:"))
#     checker=Armstorngchecker(num)

#     if checker.is_armstrong():
#         print(f"{num} is a arm strong number")
#     else :
#         print(f"{num} is  not a arm strong number")

# import random

# secert_number=random.randint(1,10)
# print("welcome gessing number")
# print(" i have picked a number between  1 to 100 , try to guess it")

# while True:
#     guess=int(input("Enter the number:"))
#     if guess<secert_number:
#         print("Too low , try again ")
#     elif guess>secert_number:
#         print("Too high , try again ")
#     else:
#         print("🎉 correct ! the number was ",secert_number)
#         break



# def word_count(str):
#     count=dict()
#     words=str.lower().split()
#     for word in words:
#         if word in count:
#             count[word]+=1
#         else:
#             count[word]=1
#     return count
# print(word_count('the the quick drown for jumps over the lazy '))



l1=[1,2,3,4]
l2=[5,6,7,8]
l3=zip(l1,l2)
print(list(l3))