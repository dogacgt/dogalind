#!/usr/bin/env python
#Catalan Numbers and RNA Secondary Structures

from Bio import SeqIO

def is_complement(s, t):
    rna_dict = {'A':'U','U':'A', 'C':'G', 'G':'C'}
    if s == rna_dict[t]: return True
    else: return False


def check_equals(s):
    if s.count('A') != s.count('U') or s.count('G') != s.count('C'):
        return False
    else: return True


#memoized function
def catalan(s, memo={}):
    if not check_equals(s):
        return 0

    elif s in memo.keys():
        return memo[s]

    count=0
    for i in range(1, len(s)):
        if is_complement(s[0], s[i]):
            count += catalan(s[1:i], memo)*catalan(s[i+1:], memo)
    memo[s] = count

    return count % 10**6


if __name__ == '__main__':
    for record in SeqIO.parse('data/rosalind_cat.txt', 'fasta'):
        s = str(record.seq)
    memo = {'':1} #initialize memo with empty string
    print(catalan(s, memo))
