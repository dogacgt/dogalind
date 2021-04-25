#!/usr/bin/env python
#Mortal Fibonacci Rabbits

with open('data/rosalind_fibd.txt', 'r') as f:
    n, m = map(int, f.read().strip().split())

def baby_rabbits(n, m):
    '''Keep track of the newborn rabbits each month,
       store them in a list.'''
    newborn = [1, 0]
    for i in range(2, n):
        newborn.append(0)
        for j in range(2, m+1):
            if i >= j:
                newborn[i] += newborn[i - j]
    return newborn

def total_rabbits(n, m):
    newborn = baby_rabbits(n, m)
    rabbits = [1, 1]
    for i in range(2, n):
        rabbits.append(0)
        rabbits[i] += rabbits[i-1]
        for j in range(2, m):
            if i >= j:
                rabbits[i] += newborn[i - j]
    return rabbits[-1]

print(total_rabbits(n, m))
