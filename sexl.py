#!/usr/bin/env python
#Sex-Linked Inheritance

with open('data/rosalind_sexl.txt', 'r') as f:
    A = f.read().split()

B = []
for i in A:
    num= (float(i) * (1-float(i)) * 2)
    B.append(str(round(num, 3)))

with open('output.txt', 'w') as f:
    f.write(' '.join(B))
