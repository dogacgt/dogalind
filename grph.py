#!/usr/bin/python3
#Overlap Graphs

# value[:3] prefix
# value[-3:] suffix

def fasta_dict(file):
    with open(file, 'r') as f:
        fastaDict = {}
        for line in f.readlines():
            if line.startswith('>'):
                key = line.strip('>\n')
                fastaDict[key] = ''
            else: fastaDict[key] += line.strip()
    return fastaDict

dict = fasta_dict('data/rosalind_grph.txt')

with open('output.txt', 'w') as f:
    for key, value in dict.items():
        v, k = value, key
        for key, value in dict.items():
            if v == value:
                continue
            if value[:3] == v[-3:]:
                res = k + ' ' + key + '\n'
                f.write(res)
