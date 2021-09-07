# -*- coding: utf-8 -*-

# -- Sheet --

country = {'korea' : 'kr', 'japan' : 'jp', 'taiwan' : 'tw', 'finland' : 'fi'}
countries = {'korea' : 'kr', 'japan' : 'jp', 'taiwan' : 'tw', 'finland' : 'fi'}
for country, code in countries.items():
    print(f'the country code of {country} is {code}.')
    

for country in countries.keys():
    print(country, end= ' ')
    print()

for codes in countries.values():
    print(codes, end= ' ')

code1 = {'korea' : '91', 'japan' : '78', 'taiwan' : '42', 'finland' : '142'}
print(list(code1.keys()))
print(list(code1.values()))
code2 = list(code1.items())
print(code2, code2[1])




for i, j in zip(code2.keys(), code2.values()):
    print(f'the country code of {i} is, {j}.')

    #실행오류 발생 

print(sorted(code1))
print(sorted(code1.keys()))
print(sorted(code1.values()))
print(sorted(code1.items()))

switched = {code: code1 for code1, code in code1.items()}
print(sorted(switched.items()))

tem = { 'japan' : [23,542,152], 'korea' : [125125,1242,1525]}
tem1 = { k: sum(v)/len(v) for k, v in tem.items()}
print(tem1)
tem3 = {k: v for k, v in sorted(code1.items(), key = lambda code1: code1[1])}
print(tem3)

switced1 = {code: code1 for code1, code in code1.items()}
print((sorted(switced1.items())))
tem4 = { 'japan': [25125,24124,21512], 'korea' : [15125,14124,15215]}
tem4 = { k: sum(v)/len(v) for k, v in tem4.items()}
print(tem4)

drm1 = """I have a dream that one day this nation will rise up and live out the true meaning of its creed We hold these truths to be self-evident that all men are created equal

I have a dream that one day on the red hills of Georgia the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood

I have a dream that one day even the state of Mississippi a state sweltering with the heat of injustice sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice

I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character

I have a dream today

I have a dream that one day, down in Alabama, with its vicious racists, with its governor having his lips dripping with the words of interposition and nullification one day right there in Alabama little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers"""

drm2 = drm1.split()
wordlist = {}
for word in drm2:
    if word in wordlist:
        wordlist[word] += 1
    else:
        wordlist[word] = 1
print(drm2)

print(wordlist, len(wordlist))
awl = {k: v for k, v in sorted(wordlist.items(), key = lambda i: i[1], reverse = True)}
print(awl)
    

print(f'{"word": <16} count')
for word, count in awl.items():
    if count >= 6:
        print(f'{word:<16}{count}')
print('\nNumber of unique word: ', len(wordlist))

import collections 
wordlist1 = counter(drm1)
print(wordlist1)
srw1 = {k: v for k, v in sorted(worldlist1.items(), key = lambda i: i[1], reverse = True)}
print(srw1)

print(f'{ "WORD"<<16}COUNT')

for word, count in drm2.items():
    if count >= 6:
        print(f'{word:<16}{count}')
print

mon = {'fuck', ' you', 'fuck', 'may', 'june','fuckk'}
print(mon)

mon2 = set(list(range(10)) + list(range(5,15)))
print(mon2)
print(len(mon2))
print((10 in mon2))

mon2.remove(8)
print(mon2)

mon2.clear()
print(mon2)

mon2.update(range(45))
print(mon2)

a1 = ({1,2,3,})
a2 = ({1,2,3,4,5,6,7})

a1 <= a2
a1 | a2 #집합연산 중 합집합 
a2 - a1

mon3 = {i for i in a1 if i % 2 != 0}
print((mon3))



