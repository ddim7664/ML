# -*- coding: utf-8 -*-

# -- Sheet --

x = [5,1,2,5]
print(x)

list1 = [154,142,152,552,142,1555]
list2 = [152,442,1525,15616,242,'a', 'b', 'c', 'abcd']

print(len(list1))
print(list1[:])
print(list1[::2])

del list2[-1]
print(list2)
del list2[:]
print(list2)

x = [5,1,2,5]
print(x)

print(list1)
del x


num1 =  [1,2,51,25,66,12,16,123,6152]
num1.sort()
print(num1)

num1.sort(reverse = True)
print(num1)
num1.reverse()
print(num1)

num2 = 'i miss you so much'
num2 = num2.split()
print(num2, type(num2))
num2.sort(key=len)
print(num2), type(num2)
num3 = sorted(num2)
print(num3)



