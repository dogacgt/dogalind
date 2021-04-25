#!/usr/bin/env python
#Finding a Motif in DNA

def subs(s, t):
    res = []
    ls, lt = len(s), len(t)
    for i in range(0, ls):
        if s[i:i+lt] == t:
            res.append(i+1)
    with open('output.txt','w') as f:
        f.write(' '.join(map(str, res)))

if __name__ == '__main__':
    with open('data/rosalind_subs.txt') as f:
        s, t = f.read().strip().split()
    subs(s, t)
