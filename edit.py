#!/usr/bin/python3
#Edit Distance

import numpy as np

with open('data/rosalind_edit.txt', 'r') as f:
    seqs = []
    seq = ''
    for line in f.readlines():
        if line.startswith('>'):
            if seq != '': seqs.append(seq)
            seq = ''
        else: seq += line.strip()
    seqs.append(seq)

n, m = seqs[0], seqs[1]
x, y = len(n), len(m)

arr = np.zeros([x+1, y+1])
for i in range(1, x+1):
    arr[i][0] = arr[i-1][0] + 1
for i in range(1, y+1):
    arr[0][i] = arr[0][i-1] + 1


for j in range(1, y+1):
    for i in range(1, x+1):
        if n[i-1] == m[j-1]:
            arr[i][j] = arr[i-1][j-1]
        else:
            arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1

print(int(arr[-1][-1]))
