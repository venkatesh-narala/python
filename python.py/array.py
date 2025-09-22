
'''
 array methods:
 1:append
 2:remove 
 3:pop
 4:clear
 5:copy
 6:extend
 7:index
 8:insert
 9:sort
'''
import array as arr

numbers = arr.array('i',[10,12,12,13])
print(type(numbers))
print("slicing :",numbers[0:2])
print(len(numbers))

int_list =numbers.tolist()
print(int_list)

import array 

numbers=array.array("i",[10,20,30,40])
numbers.append(67)

print("append using :",numbers)

import array 

numbers=array.array("i",[10,20,30,40])


numbers.remove(10)

print("remove an array :",numbers)

removed =numbers.pop(2)
print("pop method using an array:",numbers)

numbers.clear()
print("clear using an array:",numbers)

num=numbers.__copy__()
print("copy method in array:",num)

numbers.extend([123,134,127])
print("extend using in array:",numbers)


import array 

numbers=array.array("i",[10,20,30,40])

x=numbers.index(10) 
print("index of an array:",x)

numbers.insert(1,77)
print("insert an array:",numbers)


numbers[3]=50

print("modify an element :",numbers)

import array
arr = array.array('i', [10, 20, 30, 40])
arr.remove(30)
arr.pop()
print(arr)   # 2

