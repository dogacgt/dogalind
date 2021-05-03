#!/usr/bin/python
#Error Correction in Reads

from Bio import SeqIO

dna_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
contigs=[]
for record in SeqIO.parse('data/rosalind_corr.txt', 'fasta'):
    contigs.append(str(record.seq))

def reverse(s):
    rev=''
    for code in s:
        rev+=dna_dict[code]
    return rev[::-1]

def hdist(s1, s2):
    h=0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            h+=1
    if h==1: return True
    else: return False

correct, wrong = [], []
for s1 in contigs:
    count=0
    for s2 in contigs:
        if s1==s2 or reverse(s1)==s2:
            count+=1
    if count>1:
        correct.append(s1)
        correct.append(reverse(s1))
    elif count<2:
        wrong.append(s1)

with open('output.txt', 'w') as f:
    for s1 in wrong:
        for s2 in correct:
            if hdist(s1, s2):
                f.write('{}->{}\n'.format(s1, s2))
                break
