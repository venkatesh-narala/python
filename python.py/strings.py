
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

name=(input("enter the string:"))
def string_calculate(name):
    letters=0
    digits=0
    for i in name:
        if i.isalpha():
            letters+=1
        elif i.isdigit():
            digits+=1
    return f"letters:{letters} \n digits:{digits}"
print(string_calculate(name))


l=[2,3,4,5]
print(type(l).__name__)
result=1
for i in l:
    result*=i
print("multiplication all numbers :",result)