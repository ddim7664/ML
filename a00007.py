

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


def solutions(t):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for t in range(len(words)):
        t = t.replace(words[t], str(t))

    return int(t)

#기존 문제해답풀이

int
s = 1 ≤ s ≤ 50

#필요없는 항목

class FAT:
    int
    0 = zero:
    1 = one:
    3 = three:
    4 = four:
    5 = five:
    6 = six:
    7 = seven:
    8 = eight:
    9 = nine
    
    #클래스로 정의할 시 단순한 코딩의 범주를 벗어난다.

    for t in range(len(words)):
        t = t.replace(words[t], str(t))
        
        #다른 사람의 답안을 살펴봐도 for 함수를 대부분 사용한다.
        #class로는 풀 수없는가? 풀 수 있겠지만 비효율적
    
    def solution(s):
        answer = 0
        return answer