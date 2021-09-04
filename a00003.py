#!/usr/bin/env python
# coding: utf-8

# In[21]:


import keras as kr 
import numpy as np
import math as ma
import pandas as pd 
import tensorflow as tf 
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[ ]:


plt.title('test')
plt.plot([1,2,3,4],[2,5,10,30])
plt.show()


# In[3]:


a = np.array([[10,20,30],[60,70,80]])
print(a)


# In[5]:


print(a.ndim)


# In[6]:


print(a.shape)


# In[7]:


c = np.zeros((2,3))
print(c)


# In[8]:


d = np.ones((3,4))


# In[9]:


e = np.eye(3)
print(e)


# In[10]:


f = np.random.random((2,2))
print(f)


# In[11]:


a = np.arange(10)
print(a)


# In[15]:


xxx= np.array([[1,2,3,],[4,5,6]])
yyy= xxx[0:2, 0:4] 
print(yyy)


# In[16]:


abcd = np.array([1,2,3])
abcde = np.array([4,5,7])


# In[34]:


plt.title('students')
plt.plot([1,2,3,4],[2,4,8,6])
plt.plot([1.5,2.5,3.5,4.5],[3,5,8,10]) #라인 새로 추가
plt.xlabel('hours')
plt.ylabel('score')
plt.legend(['A student', 'B student']) #범례 삽입
plt.show()


# In[44]:


import pandas as pd 
import pandas_profiling
data = pd.read_csv(r'C:\Users\Jo\Desktop\spam.csv',encoding='latin1')


# In[45]:


data[0:10]


# In[50]:


data1 = np.array([data[:10]])
data2 = np.array([data[:20]])


# In[54]:


prt = data.profile_report()


# In[55]:


prt.to_file('./pr_report.html')


# In[56]:


prt


# In[57]:


from nltk.tokenize import word_tokenize  


# In[58]:


print(word_tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))  


# In[59]:


from nltk.tokenize import WordPunctTokenizer  
print(WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))


# In[60]:


be an ideal. it doesn't have a food chain or restaurant of their own."
print(tokenizer.tokenize(text))from nltk.tokenize import TreebankWordTokenizer
tokenizer=TreebankWordTokenizer()
text="Starting a home-based restaurant may


# In[61]:


from nltk.tokenize import sent_tokenize
text="His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to make sure no one was near."
print(sent_tokenize(text))


# In[62]:


from nltk.tokenize import sent_tokenize
text="I am actively looking for Ph.D. students. and you are a Ph.D student."
print(sent_tokenize(text))


# In[63]:


from nltk.tokenize import word_tokenize
text="I am actively looking for Ph.D. students. and you are a Ph.D. student."
print(word_tokenize(text))


# In[64]:


from nltk.tokenize import word_tokenize
text="I am actively looking for Ph.D. students. and you are a Ph.D. student."
print(word_tokenize(text))


# In[65]:


from nltk.tag import pos_tag
x=word_tokenize(text)
pos_tag(x)


# In[66]:


from konlpy.tag import Kkma  
kkma=Kkma()  
print(kkma.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))


# In[67]:


import re
text = "I was wondering if anyone out there could enlighten me on this car."
shortword = re.compile(r'\W*\b\w{1,2}\b')
print(shortword.sub('', text))


# In[69]:


from nltk.stem import WordNetLemmatizer
n=WordNetLemmatizer()
words=['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
print([n.lemmatize(w) for w in words])


# In[71]:


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
s = PorterStemmer()
text="This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."
words=word_tokenize(text)
print(words)


# In[72]:


print([s.stem(w) for w in words])


# In[73]:


from nltk.stem import PorterStemmer
s=PorterStemmer()
words=['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
print([s.stem(w) for w in words])


# In[74]:


from nltk.stem import LancasterStemmer
l=LancasterStemmer()
words=['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
print([l.stem(w) for w in words])


# In[75]:


from nltk.corpus import stopwords  
stopwords.words('english')[:10]  


# In[76]:


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

example = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words('english')) 

word_tokens = word_tokenize(example)

result = []
for w in word_tokens: 
    if w not in stop_words: 
        result.append(w) 

print(word_tokens) 
print(result) 


# In[78]:


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
stop_words = "아무거나 아무렇게나 어찌하든지 같다 비슷하다 예컨대 이럴정도로 하면 아니거든"
# 위의 불용어는 명사가 아닌 단어 중에서 저자가 임의로 선정한 것으로 실제 의미있는 선정 기준이 아님
stop_words=stop_words.split(' ')
word_tokens = word_tokenize(example)

result = [] 
for w in word_tokens: 
    if w not in stop_words: 
        result.append(w) 
# 위의 4줄은 아래의 한 줄로 대체 가능
# result=[word for word in word_tokens if not word in stop_words]

print(word_tokens) 
print(result)


# In[80]:


import re
r=re.compile("a.c")
r.search("kkk") # 아무런 결과도 출력되지 않는다.


# In[81]:


import re 
r = re.compile("^a")
r.search("bbc")


# In[82]:


r.search("ab")


# In[83]:


a = input()

def omg:
    b = re.sub('[a-zA-]', ' ', text)
    print(b)
    
print(b)
    


# In[84]:


import re  

text = """100 John    PROF
101 James   STUD
102 Mac   STUD"""  

re.split('\s+', text)  


# In[ ]:




