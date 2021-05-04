#!/usr/bin/env python
#Open Reading Frames

codons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
    "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

dna_dict = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}

with open('data/rosalind_orf.txt', 'r') as f:
    dna = ''
    for line in f.readlines():
        if line[0] != '>':
            dna += line.strip()

rev_dna = ''
for code in dna:
    rev_dna += dna_dict[code]
rev_dna = rev_dna[::-1]

rna = rev_dna.replace('T', 'U')
rev_rna = dna.replace('T', 'U')

def count_indices(string, substring):
    index = []
    for i in range(0, len(string)):
        if substring == string[i:i+len(substring)]:
            index.append(i)
    return index

index_rna = count_indices(rna, 'AUG')
index_revrna = count_indices(rev_rna, 'AUG')

proteins = []

for index in index_rna:
    pro = ''
    seq = rna[index:]
    for i in range(0, len(seq), 3):
        if i+3 > len(seq): break
        pro += codons[seq[i:i+3]]
    if 'Stop' in pro:
        pro = pro[:pro.find('Stop')]
        if pro not in proteins: proteins.append(pro)

for index in index_revrna:
    pro = ''
    seq = rev_rna[index:]
    for i in range(0, len(seq), 3):
        if i+3 > len(seq): break
        pro += codons[seq[i:i+3]]
    if 'Stop' in pro:
        pro = pro[:pro.find('Stop')]
        if pro not in proteins: proteins.append(pro)

with open('output.txt', 'w') as f:
    for protein in proteins:
        f.write(protein + '\n')

#lol this is a mess
