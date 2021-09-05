#!/usr/bin/env python
# coding: utf-8

# In[1]:


def findmin():
    
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))
    z = int(input('enter third number: '))
    
    minimum = x 
    
    if y < minimum:
        minimum = y
    if z < minimum:
        minimum = z
    return minimum
        


# In[3]:


findmin()


# In[4]:


def aa1(x,y,z):
    
    return min(x,y,z)


# In[5]:


print(aa1(7,8,9))
print(aa1)


# In[6]:


def rectangle(width=3, height=5):
    
    return width*height


# In[8]:


print(rectangle(), rectangle(5), rectangle(4,5))


# In[9]:


def aver(*nums):
    
    return sum(nums)/len(nums)


# In[10]:


aver(50)


# In[11]:


aver(50,10)


# In[13]:


grad = [1,2,3,4,5,6,7,8,9]
aver(*grad)


# In[38]:


import math
def circle(radius):
    
    return math.pi*radius**2, 2*math.pi*radius


# In[52]:


def main_function(x):
    print(f'the area and circumference of a circle with {x}cm radius are {circle(x)[0]:.2f}cm squared and {circle(x)[1]:.3f}cm.')
    print('Main function is excuted!')

if __name__ == '__main__':
    main(4)

main_function(5); __name__

  


# In[47]:





# In[53]:


import main_function as mf 
print(mf.circle(5))
print(mf.__name__)


# In[ ]:




