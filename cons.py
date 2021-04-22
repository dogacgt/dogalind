#!/usr/bin/python3
#Consensus and Profile

with open('data/rosalind_cons.txt', 'r') as f:
    f = f.readlines()
    dna = ''
    seqs = []
    for line in f:
        if line.startswith('>'):
            if dna != '':
                seqs.append(dna)
            dna = ''
        else: dna += line.strip()
    seqs.append(dna)

def profile(seqs, letter):
    length = len(seqs[0])
    count = [0] * length
    for i in range(length):
        for seq in seqs:
            if seq[i] == letter:
                count[i] += 1
    return count

A = profile(seqs, 'A')
G = profile(seqs, 'G')
C = profile(seqs, 'C')
T = profile(seqs, 'T')

def consensus():
    cons = ''
    for i in range(len(A)):
        hi = max(A[i], G[i], C[i], T[i])
        if hi == A[i]: cons += 'A'
        elif hi == G[i]: cons += 'G'
        elif hi == C[i]: cons += 'C'
        elif hi == T[i]: cons += 'T'
    return cons

with open('output.txt', 'w') as f:
    f.write(consensus() + '\n')
    f.write('A: ' + ' '.join(map(str, A)) + '\n')
    f.write('C: ' + ' '.join(map(str, C)) + '\n')
    f.write('G: ' + ' '.join(map(str, G)) + '\n')
    f.write('T: ' + ' '.join(map(str, T)))
