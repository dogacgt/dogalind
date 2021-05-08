#!/usr/bin/env python
#Counting Rooted Binary Trees

from math import factorial

def main():
    return (factorial(2*n-3) // (factorial(n-2)*2**(n-2))) % 10**6

if __name__ == '__main__':
    with open('data/rosalind_root.txt') as f:
        n = int(f.read().strip())
    print(main())

