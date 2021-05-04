#!/usr/bin/env python
#Calculating Expected Offspring

def iev():
    prob = [1, 1, 1, .75, .5, 0]
    sum = 0
    for i in range(6):
        sum += prob[i] * vec[i] * 2
    return sum

if __name__ == '__main__':
    with open('data/rosalind_iev.txt', 'r') as f:
        vec = [int(i) for i in f.read().strip().split()]
    print(iev())
