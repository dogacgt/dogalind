#!/usr/bin/env python
#Counting DNA Nucleotides

def dna(s):
    res = [s.count('A'), s.count('C'), s.count('G'), s.count('T')]
    return ' '.join(map(str, res))

if __name__ == '__main__':
    with open('data/rosalind_dna.txt', 'r') as f:
        s = f.read().strip()
        print(dna(s))
