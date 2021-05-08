#!/usr/bin/env python
#Creating a Character Table from Genetic Strings

# get characterizable positions
def _get_snp(dna_list):
    snp = []
    for i in range(len(dna_list[0])):
        states={}
        for dna in dna_list:
            if dna[i] not in states:
                states[dna[i]] = 1
            else:
                states[dna[i]] += 1

        if 1 not in states.values() and len(states) == 2:
            snp.append(i)

    return snp

def character_table():
    snps = _get_snp(dna_list)
    res = []
    for snp in snps:
        char_table='1'
        s1 = dna_list[0][snp]
        for dna in dna_list[1:]:
            if dna[snp] == s1:
                char_table += '1'
            else:
                char_table += '0'
        res.append(char_table)
    return res


if __name__ == '__main__':
    with open('data/rosalind_cstr.txt') as f:
        dna_list = f.read().strip().split()

    with open('output.txt', 'w') as f:
        f.write('\n'.join(character_table()))
