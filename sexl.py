#!/usr/bin/env python

# q = 0.1
# p = 0.9
# 2*p*q = 0.18

with open('data/rosalind_sexl.txt', 'r') as f:
    A = f.read().split()

B = []
for i in A:
    num= (float(i) * (1-float(i)) * 2)
    B.append(round(num, 3))

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, B)))
