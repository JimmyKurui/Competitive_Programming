import re

def sortSentence(s):
        sen = s.split()
        senIndex = list(map(int, re.findall(r"\d", s)))
        senCopy = sen.copy()
        for i in range(len(sen)):
             for j in range(len(senIndex)):
                 if i == senIndex[j]-1:
                     senCopy[i] = sen[j]
        print(senCopy)


