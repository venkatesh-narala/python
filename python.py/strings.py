
import string

print(string.ascii_letters)   # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_lowercase) # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase) # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(string.digits)          # '0123456789'
print(string.hexdigits)       # '0123456789abcdefABCDEF'
print(string.octdigits)       # '01234567'

print(string.punctuation)     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.whitespace)      # ' \t\n\r\x0b\x0c'  (space, tab, newline, etc.)





try:
    x=10/0
except ZeroDivisionError as err:
    print("Caught an error:", err)



n=10
print(type(n).__name__)



str="VFOnvdi"

def countupper_lower_case(str):
    isupper_count=0
    islower_count=0
    for i in str:
        if i.islower():
            islower_count+=1
        elif i.isupper():
            isupper_count+=1
    return f"upper count is :{isupper_count} ,lower count is :{islower_count}"

print(countupper_lower_case(str))

name="venkatewsh"

def count_lenth_of_string(name):
    count=0
    for i in name:
        if i.isalpha():
            count+=1
    return count
print(count_lenth_of_string(name))

# name=(input("enter the string:"))
# def string_calculate(name):
#     letters=0
#     digits=0
#     for i in name:
#         if i.isalpha():
#             letters+=1
#         elif i.isdigit():
#             digits+=1
#     return f"letters:{letters} \n digits:{digits}"
# print(string_calculate(name))


l=[2,3,4,5]
print(type(l).__name__)
result=1
for i in l:
    result*=i
print("multiplication all numbers :",result)



#string slicing 
s='venkateshnarala'
print(s[0:9])
print(s[-15:-6])
#reverse a string using slicing
print(s[::-1])


#reverse a list using method

l=[10,39,48,'sai']
l.reverse()
print(f'reverse a list : {l}')


#reverse a string using function 

name='venkatesh'
reverse_name=tuple(reversed(name))
print(reverse_name)

#error handling method

try :
    name[0]='s'
except Exception as err:
    print('error :',err)
else:
    print('not error occur')
finally:
    print('always print')



#string methods all

'''
CHANGING CASE

capitailize
tittle
upper
lower

SEARCHING & FINDING

swapcase
find 
count
rfind
CHECKING STRING

isalpha
isdigit
isalnum
islower
isupper
isspace

MODIFYING STRING

rstrip
lstrip
strip
split
join
replace


'''


#string changing methods

string_name='hello world'
print(string_name.capitalize())
print(string_name.title())
print(string_name.upper())
print(string_name.lower())

#string count and finding 

count_string='venkatesh narala'

print(count_string.swapcase())
print(count_string.find("a"))
print(count_string.count('a'))
print(count_string.rfind("n"))


#string checking 

check_string='hello world'

print(check_string.isalpha())
print(check_string.isalnum())
print(check_string.isascii())
print(check_string.isupper())
print(check_string.islower())
print(check_string.isdigit())


#string change & modifying

ms='    nani    '

print(tuple(ms.lstrip()))
print(ms.rstrip())
print(ms.strip())

cs='sai nani'
print(cs.split())

print(' '.join(['a','b','c']))


print(cs.replace('sai','ravi'))






