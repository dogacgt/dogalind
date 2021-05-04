#!/usr/bin/env python
#Computing GC Content

def gc_content(st):
    gc = st.count('G') + st.count('C')
    return (gc/len(st) * 100)

def fasta_dict(file):
    with open(file, 'r') as f:
        fasta_dict = {}
        for line in f.readlines():
            if line.startswith('>'):
                key = line.strip('>\n')
                fasta_dict[key] = ''
            else: fasta_dict[key] += line.strip()
    return fasta_dict

dict = fasta_dict('data/rosalind_gc.txt')

hi = 0
for key, value in dict.items():
    if gc_content(value) > hi:
        hi = gc_content(value)
        true_key = key

print(true_key)
print('%.3f' % hi)
