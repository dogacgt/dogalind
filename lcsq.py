#!/usr/bin/python
#Finding a Shared Spliced Motif

import numpy as np
from Bio import SeqIO

def table():
    arr = np.zeros([ls+1, lt+1])
    for j in range(1, lt+1):
        for i in range(1, ls+1):
            if s[i-1] == t[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i][j-1], arr[i-1][j])
    return arr


def longest_common_subseq():
    arr = table()
    result = ''
    i, j = ls, lt

    while i != 0 and j != 0:
        if arr[i][j] == arr[i-1][j]:
            i -= 1
        elif arr[i][j] == arr[i][j-1]:
            j -= 1
        else:
            result += s[i-1]
            i -= 1
            j -= 1

    return result[::-1]


if __name__ == '__main__':
    with open('data/rosalind_lcsq.txt', 'r') as f:
        seqs=[]
        for seq in SeqIO.parse(f, 'fasta'):
            seqs.append(seq.seq)

    s, t = seqs[0], seqs[1]
    ls, lt= len(s), len(t)

    with open('output.txt', 'w') as f:
        f.write(longest_common_subseq())
