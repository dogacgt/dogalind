#!/usr/bin/python
#Genome Assembly as Shortest Superstring

from Bio import SeqIO

start=time()
with open('data/rosalind_long.txt') as f:
    seqs=[]
    for seq in SeqIO.parse(f, 'fasta'):
        seqs.append(str(seq.seq))

def match(s1, ls):
    ll = len(s1)
    for k in range(ll, ll//2, -1):
        for s2 in ls:
            if s1 != s2 and s1[:k] == s2[-k:]:
                return str(s2+s1[k:])

while len(seqs)!=1:
    contigs=[]
    for b in seqs:
        m = match(b, seqs)
        if m!=None and m not in seqs:
            contigs.append(m)
    seqs=contigs

with open('output.txt', 'w') as f:
    f.write(seqs[-1])
