# d={1:'nani',2:'sai',3:'chitti'}

# print(f"dict_values{d.values()}")

# print(f"dict_items{d.items()}")

# print(f"dict_keys{d.keys()}")

# # print(f"dict_clear{d.clear()}")

# d2=d.copy()

# print(f"dict_values{d}")

# print(f"dict_pop{d.pop("2")}")

# print(f"dict_pop_items{d.popitem()}")

# print(f"dict_setdefault{d.setdefault({4:'ram'})}")

# print(f"dict_update{d.update({2:'ramu'})}")

# print(f"dict_values{d.__delattr__del()}")



# nums = range(5)
# print(list(nums))

# while True:

#     num=int(input("enter the number:"))
#     if num<=1:
#         print(f"{num}is not prime number")
#         break
#     for i in range(2,int (num**0.5)+1):
#         if num%i ==0:
#             print(f"{num}is not prime number")
#             break
#     else:
#         print(f"{num}is prime number")

# l=[1,3,5,6,6,7,]
# print(l[::-1])

# # Program to reverse a list without using built-in methods

# numbers = [10, 20, 30, 40, 50]
# reversed_list = []

# # Iterate from last element to first
# for i in range(len(numbers)-1, -1,-1):
#     reversed_list.append(numbers[i])

# print("Original list:", numbers)
# print("Reversed list:", reversed_list)


# text = "Python"
# reversed_text = ""

# # for ch in text:
# #     reversed_text = ch + reversed_text   # add character in front

# # print("Original string:", text)
# # print("Reversed string:", reversed_text)

# # listed=[20,10,30,40,'nani']
# # reversed_l=list(reversed(listed))
# # print(reversed_l)
# # listed.reverse()
# # print(listed)



# #write a program in python to input a two digit number and print it in words . for example if input is 98 , the output should be "nini eight"

# dict_words={
#     '0':"zero",
#     '1':"one",
#     '2':"two",
#     '3':"three",
#     '4':"four",
#     '5':"five",
#     '6':"six",
#     '7':"seven",
#     '8':"eight",
#     '9':"nine",
# }
# num=input("enter the number:")
# output=" ".join(dict_words[d] for d in num)
# print(output)

names='nani sai'
words=names.split()
words.reverse()
j=" ".join(words)
print(names)
print(j)