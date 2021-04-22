#!/usr/bin/env python
#Inferring Protein from Spectrum

with open('table.txt', 'r') as f:
    dict = {}
    for line in f.readlines():
        a, b = line.strip().split()[::-1]
        key = '%.4f'%float(a)
        dict[key] = b

with open('data/rosalind_spec.txt', 'r') as f:
    input = f.read().strip().split()

diff = []
i=len(input)-1
while i > 0:
    mass = float(input[i]) - float(input[i-1])
    diff.append('%.4f' % mass)
    i -= 1

pro = ''
for mass in diff:
     pro += dict[mass]
print(pro[::-1])
