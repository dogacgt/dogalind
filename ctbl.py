#!/usr/bin/env python
#Creating a Character Table

#for this one I slightly modified the function in the documentation
 #https://biopython.org/wiki/Phylo

from Bio import Phylo
from Bio.Phylo.Consensus import _BitString

tree = Phylo.read('data/rosalind_ctbl.txt', 'newick')

with open('output.txt', 'w') as f:
    term_names = [term.name for term in tree.get_terminals()]
    term_names.sort()
    for clade in tree.get_nonterminals()[1:]:
        clade_term_names = [term.name for term in clade.get_terminals()]
        boolvals = [name in clade_term_names for name in term_names]
        bitstr = _BitString("".join(map(str, map(int, boolvals))))
        f.write('{}\n'.format(bitstr))
