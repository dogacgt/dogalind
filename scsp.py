#!/usr/bin/env python
#Interleaving Two Motifs

import numpy as np

def table(m, n):
    R = np.zeros([m+1, n+1])
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                R[i][j] = R[i-1][j-1]+1
            else:
                R[i][j] = max(R[i-1][j], R[i][j-1])
    return R

def shortest_common_superseq(m, n):
    R = table(m, n)
    i, j = len(s), len(t)
    res = ''
    while i>0 or j>0:
        if R[i][j] == R[i-1][j]:
            i -= 1
            res += s[i]
        elif R[i][j] == R[i][j-1]:
            j -= 1
            res += t[j]
        else:
            res += s[i-1]
            i -= 1
            j -= 1
    return res[::-1]


if __name__ == '__main__':
    with open('data/rosalind_scsp.txt', 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()
        m, n = len(s), len(t)

    with open('output.txt', 'w') as f:
        f.write(shortest_common_superseq(m, n))
