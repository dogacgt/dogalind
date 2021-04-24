#!/usr/bin/python3
#Counting Phylogenetic Ancestors

with open('data/rosalind_inod.txt', 'r') as f:
    n = int(f.read().strip())

# an unrooted binary tree with n leaves
 # will have n-2 internal nodes
print(n-2)
