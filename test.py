# -*- coding: utf-8 -*-
__author__ = 'PCPC'

def letterCombinations(digits):
    if '' == digits: return []
    kvmaps = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    ret=['']
    for c in digits:
        tmp=[]
        for y in ret:
            for x in kvmaps[c]:
                print(tmp,x+y)
                tmp+=y+x
                print(tmp)
        ret=tmp

    return ret

letterCombinations('22')

import sys

for line in sys.stdin:
    arr = line.split()
coursedict={}
param=arr[0].split(' ')
sum=0
for s in arr[1:]:
    val = s.split(' ')
    sum+=val[0]
    coursedict[val[1]]=coursedict.get(val[1],0)+param[1]-val[0]
left=param[2]*param[0]-sum
time=0
for key in coursedict.keys.sort():
    if left-coursedict[key]>0:
        left-=coursedict[key]
        time+=coursedict[key]*key
    else:
        time+=left*key

print(time)
