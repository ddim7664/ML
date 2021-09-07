# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd 
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer

a = np.array([7,8,9,10,11])

sentences = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], ['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], ['barber', 'went', 'huge', 'mountain']]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

encoded = tokenizer.texts_to_sequences(sentences)
print(encoded)

ml = max(len(item) for item in encoded)
print(ml)

for item in encoded:
    while len(item) < ml:
        item.append(0)

padded_np = np.array(encoded)
padded_np

from tensorflow.keras.preprocessing.sequence import pad_sequences

encoded = tokenizer.texts_to_sequences(sentences)
print(encoded)

pad1 = pad_sequences(encoded)
pad1

pad1 = pad_sequences(encoded, padding = 'post', maxlen = 5)
pad1

lv = len(tokenizer.word_index) +1 
print(lv)

pad2 = pad_sequences(encoded, padding= 'post', maxlen =5)
print(pad2)

pad3 = pad_sequences(encoded, padding= 'post', value = lv)
print(pad3)

from konlpy.tag import Okt  
okt=Okt()  
token=okt.morphs("나는 자연어 처리를 배운다")  
print(token)

word2index ={}
for voca in token:
    if voca not in word2index.keys():
        word2index[voca] =len(word2index)
print(word2index)

def ohe(word, word2index):
    ohv = [0]*(len(word2index))
    index = word2index[word]
    ohv[index]=1
    return  ohv

ohe("자연어", word2index)



from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import  to_categorical

text = "나랑 라면먹으러 갈래? 나 알쓰야"

t = Tokenizer()
t.fit_on_texts([text])
print(t.word_index)

text2 = "점심 먹으러 갈래 메뉴는 햄버거 최고야"
encoded2 =t.texts_to_sequences([text2])[0]
print(encoded2)

text3 = to_categorical(encoded2)
print(text3)

import numpy as np
b = np.array([[1,0,2,3,4,5], [8,9,10,11,12,2]])
print(f'{b}\n {"object tpye:":>12} {type(b)}\n{"data type:":>12} {b.dtype}\n{"shape:":>12} {b.shape}\n {"dimension:":>12} {b.ndim}\n{"array size:":>12} {b.size}')


a = np.array([7,8,9,10,11])
print(f'{a}\n{"object type:>12"} {type(a)}\n{"data type:":>12} {a.dtype}\n{"shape:":>12}\a1 = np.array([a]); print(a1.shape)')

abc = np.zeros((2,3))
abcd = np.ones((2,4))
print(abc,abcd)
abcde = np.full((2,5),7)
print(abcde)
print(np.eye(3))

abcdef = np.random.random((2,3,4))
print(f'{abcdef}\n {abcdef.dtype}')

t = np.array([[1,2,3,4,5], [8,9,10,11,12],[4,5,6,7,8], [10,11,12,13,14]])
print(f'{t}\n {"object type:":>12} {type(t)}\n {"data type:":>12} {t.dtype}\n {"shape:":>12} {t.shape}\n{"dimension:":>12} {t.ndim}\n {"array size:":>12} {t.size}')

t = ([1,2,31,412,5], [14,12,41,2,4])
print(t)
print(t[1,0,4])
print(t[1][0][4])
print(t[0,0,4])

print(t)
l = []
for i in t:
    for j in i:
        for k in j:
            l.append(k)
print(f'{l}\n{np.array(1)}')
print(np.array(t.flat))

g = np.arange(21)
print(f'{g}\n {type(g)}')
print(f'g.reshape(1, 3, 7)')

h = np.arange(5, 21, 2)
print(h)
print(np.arange(1,23).reshape(4,15))



