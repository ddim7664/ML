# -*- coding: utf-8 -*-

# -- Sheet --

num1 = ['i am not hero']
num2 = ['1,24,2,41,25,141']
print(num1)

num1.insert(3, 'not')
print(num1)
num1.append('not world')
num1.append('hate')
print(num1)
print(num1+['i', 'and'])
num1.extend(['i', 'and'])

nopied = num1.copy()
print(nopied)

num1.clear()
print(num1)

#list comprehensions



list_range = (range(0, 10))
print(list_range)

list_com = [i for i in range(0, 10, 2)]
print(list_com)

list_con = [i for i in range(0, 10,) if i % 2 != 0]
print(list_con)

list_op = [i ** 2 for i in range(0, 10, 2)]
print(list_op)

list_op1 = [i.upper() for i in list()]
print(list_op1)


list3 = (range(0,25))
list4 = (range(0,40))

print(list3)

def num3(x):

    return x % 3 == 0

num3(0)

list_gen = (i**2 for i in range(10) if i % 2 == 0)
print((list_gen))

list_gen1 = [i+4  for i in list_gen] 

list2 = [1,42,4,125]


list4 = list(filter(map(lambda x: x**2, num2)))
print(list4)

list5 = list(filter(lambda x: x % 3 == 0, list4))
print(list5)

[x**2 for x in list3 if x % 3 == 0]

list7 = list(filter(lambda x: x % 3 == 0, list4))


[x**2 for x in list3 if x % 3 == 0]

car = ['santafe', 'mini', 'pony', 'grandeur', 'sonata', 'excel', 'elantra']
car.sort(key = len)
print(car)
print(sorted(car))
print(max(car), min(car))
max(car, key = lambda  i : i.lower())

player = ['ryu', 'son', 'park', 'kwon']
goals = [7,20,15,7]
for ln, goal in zip(player, goals):
    print(f'{ln}: {goal}')

abc = [[1,2,4,5], [5,12,65,165], [15,125,1256,241,124]]
print(abc)
for row in abc:
    for column in row:
        print(column, end=" ")
    print()
    #다차원 코딩은 numpy를 이용하면 효율적이다.

country = {'korea':'kr', 'japan': 'jp', 'taiwan' : 'tw', 'finland':'fi'}
print(country)
print(len(country))
print(country['korea'])

print('korea' in country)
country['korea'] = 82
print(country)

country.update(japan = '81')
print(country)

country['canada'] = 'ca'
print(country)
country.update(china = 'cn')
print(country)
del country['korea']
print(country)






