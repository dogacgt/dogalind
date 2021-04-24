#!/usr/bin/env python
#Degree Array

with open('data/rosalind_deg.txt', 'r') as f:
    f = f.readlines()
    myList = []
    for line in f:
        line = line.rstrip('\n').split(' ')
        for i in line:
            myList.append(int(i))

newList = [i for i in range(1, myList[0]+1)]

with open('output.txt', 'w') as f:
    for i in newList:
        f.write(str(myList[2:].count(i)) + ' ')
