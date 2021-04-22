#!/usr/bin/python3
#Expected Number of Restriction Sites

with open("data/rosalind_eval.txt", 'r') as f:
    f = f.readlines()
    n = int(f[0].strip())
    s = str(f[1].strip())
    A = [float(i) for i in f[2].strip().split()]

def gc_count(s):
    return (s.count('G') + s.count('C'))

s_gc = gc_count(s)
s_at = len(s) - s_gc
B = []
for i in A:
    prob = (n-len(s)+1) * (i/2)**s_gc  *  ((1-i)/2)**s_at
    B.append(float('{:.3f}'.format(prob)))

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, B)))
