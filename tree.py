#!/usr/bin/env python
#Completing a Tree

#i like this one
#for a tree graph, N nodes, N-1 edges

with open('data/rosalind_tree.txt') as f:
    list = f.readlines()
    n = int(list[0].strip())
    edges = len(list[1:])

print(n-1-edges)

