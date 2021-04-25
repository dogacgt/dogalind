#!/usr/bin/env python
#Finding a Protein Motif

import urllib.request
import re

def fasta_url(file):
    with open(file, 'r') as f:
        list_of_urls = []
        fastaDict = {}
        for line in f.readlines():
            line = line.strip()
            fastaDict[line] = ''
            url = f'https://www.uniprot.org/uniprot/{line}.fasta'.format(line)
            with urllib.request.urlopen(url) as fme:
                for lime in fme:
                    lime = lime.decode('utf-8')
                    if lime[0] != '>':
                        fastaDict[line] += lime.strip()
    return fastaDict

if __name__ == '__main__':
    dict = fasta_url('data/rosalind_mprt.txt')
    with open('output.txt', 'w') as f:
        for key, value in dict.items():
            matches = re.finditer(r'(?=[N][^P][S|T][^P])', value)
            result = [int(match.start()+1) for match in matches]
            if result != []:
                f.write(key + '\n')
                f.write(' '.join(map(str,result)) + '\n')
