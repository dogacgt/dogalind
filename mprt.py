#!/usr/bin/env python
#Finding a Protein Motif

import urllib.request
import re

def fasta_url(file):
    with open(file, 'r') as f:
        list_of_urls = []
        fasta_dict = {}
        for uniprot_id in f.readlines():
            uniprot_id = uniprot_id.strip()
            fasta_dict[uniprot_id] = ''
            url = 'https://www.uniprot.org/uniprot/{}.fasta'.format(uniprot_id)
            with urllib.request.urlopen(url) as h:
                for seq in h:
                    seq = seq.decode('utf-8')
                    if seq[0] != '>':
                        fasta_dict[uniprot_id] += seq.strip()
    return fasta_dict

if __name__ == '__main__':
    fasta_dict = fasta_url('data/rosalind_mprt.txt')
    with open('output.txt', 'w') as f:
        for key, value in fasta_dict.items():
            matches = re.finditer(r'(?=[N][^P][S|T][^P])', value)
            result = [int(match.start()+1) for match in matches]
            if result != []:
                f.write('%s\n' % key)
                f.write('{}\n'.format(' '.join(map(str,result))))
