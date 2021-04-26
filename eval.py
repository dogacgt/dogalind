#!/usr/bin/env python
#Expected Number of Restriction Sites

def gc_count(s):
    return (s.count('G') + s.count('C'))

def main():
    s_gc = gc_count(s)
    s_at = len(s) - s_gc
    B = []
    for i in A:
        prob = (n-len(s)+1) * (i/2)**s_gc  *  ((1-i)/2)**s_at
        B.append(float('{:.3f}'.format(prob)))

    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, B)))

if __name__ == '__main__':
    with open("data/rosalind_eval.txt", 'r') as f:
        n = int(f.readline().strip())
        s = str(f.readline().strip())
        A = [float(i) for i in f.readline().strip().split()]
    main()
