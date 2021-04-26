#!/usr/bin/env python
#Locating Restriction Sites

dna_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

def main(dna):
    rev_dna = ''
    k = len(dna)
    for code in dna:
        rev_dna += dna_dict[code]

    with open('output.txt', 'w') as f:
        for i in range(k):
            for j in range(12, 3, -2):
                if i+j < k+1:
                    fake_dna = rev_dna[i:i+j]
                    if dna[i:i+j] == fake_dna[::-1]:
                        f.write(str(i+1)+' '+str(j)+'\n')

if __name__ == '__main__':
    with open('data/rosalind_revp.txt', 'r') as f:
        dna = ''
        for line in f.readlines():
            if line[0] != '>':
                dna += line.strip()
    main(dna)
