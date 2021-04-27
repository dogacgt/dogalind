#!/usr/bin/env python
#Inferring Protein from Spectrum

with open('data/mass_table.txt', 'r') as f:
    mass = {}
    for line in f.readlines():
        a, b = line.strip().split()[::-1]
        key = '%.4f' % float(a)
        mass[key] = b

with open('data/rosalind_spec.txt', 'r') as f:
    inp = f.read().strip().split()

diffs = []
i=len(inp)-1
while i > 0:
    diff = float(inp[i]) - float(inp[i-1])
    diffs.append('%.4f' % diff)
    i -= 1

protein = ''
for diff in diffs:
    protein += mass[diff]

with open('output.txt', 'w') as f:
    f.write(protein[::-1])
