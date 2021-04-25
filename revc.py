#!/usr/bin/env python
#Complementing a Strand of DNA

dna_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

def rev_comp(s):
    sc = ''
    for nu in s:
        sc += dna_dict[nu]
    return sc[::-1]

if __name__ == '__main__':
    with open('data/rosalind_revc.txt', 'r') as f:
        s = f.read().strip()
    with open('output.txt', 'w') as f:
        f.write(rev_comp(s))
