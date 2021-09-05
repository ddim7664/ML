#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

for roll in range(10):
    print(random.randrange(1, 7), end=' ')


# In[8]:


fre1 = 0
fre2 = 0
sam = 10_000 # 숫자 1000단위 구분은 _를 사용한다.

for roll in range(sam):
    face = random.randrange(0,2)
    if face == 0:
        fre1 += 1
    else:
        fre2 += 1
print(f'{"Face"}{"Frequency" : >13},{"Ratio":>10}') #중괄호[문자] 뒤 비교연산자 + 숫자는 공간을 확보하여 숫자,문자를 출력할 수 있다. 
print(f'{0:>4}{fre1:>13}{fre1/sam*100:>10.2f}')
print(f'{1:>4}{fre1:>13},{fre2/sam*100:>10.2f}')


# In[10]:


random.seed(20210905)

for roll in range(10):
    print(random.randrange(1, 7), end = ' ')


# In[14]:


from math import ceil, floor, pi
import statistics as stat


# In[15]:


print(pi, ceil(9.8), floor(9.8))
x = [3,4,5]
print(stat.mean(x))


# In[18]:


list1 = [1,2,3,4,5,6,11,'a','b']
print(type(list1), list1)


# In[19]:


print(list1[1], list1[7])


# In[20]:


len(list1)


# In[21]:


list1[6]


# In[22]:


print(list1)


# In[23]:


list1[6] = 'c'
print(list1)


# In[24]:


list2 = []
for item in range(11, 14, 1):
    list2 += [item]
print(list2)


# In[25]:


list3 = []
list3 += 'python kooc'
print(list3, len(list3))


# In[26]:


list3.append('a')


# In[27]:


print(list3)


# In[28]:


list3.reverse()


# In[29]:


print(list3)


# In[32]:


print(list3[0:3])


# In[33]:


list3 += ('M','O')
print(list3, len(list3))


# In[34]:


list3 = list1 + list2


# In[35]:


print(list3)


# In[42]:


for i in range(len(list3)):
    print(f'({i}, {list3[i]}))', end = ' ')


# In[43]:


t1 = 10,20,30,'john'
t1 += (40,50)
print(t1)


# In[44]:


t2 = tuple([1,2,3,4])
print(t2)
print(t2[2])
print(t2[:3])


# In[48]:


t3 = 'k','ki','kweo',[80,90,100]
print(t3, len(t3), t3[2])


# In[50]:


t4 = (('k','par','wo'),[80,90,142])
print(len(t4))
last_name, grades = t4
print(last_name, grades, type(last_name),type(grades))


# In[51]:


first, second, third, fourth = 'WIFI'
print(first, second, third, fourth)


# In[52]:


colors = ['r', 'y', 'b', 'bl', 'w']
print(list(enumerate(colors)))


# In[54]:


for index, color in enumerate(colors):
    print(f'{index} : {colors}')


# In[55]:


bar = [19, 9, 15, 14, 14]
print('creating a bar chart: ')
print(f'index{"value :>8 "})  Bar')


# In[59]:


for index, value in enumerate(bar):
    print(f'{index:>5}{value:>8} {"*"*value}')


# In[ ]:




