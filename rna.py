#!/usr/bin/env python
#Transcribing DNA into RNA

with open('data/rosalind_rna.txt', 'r') as f:
    t = f.read().strip()

t = t.replace('T', 'U')

with open('output.txt', 'w') as f:
    f.write(t)
