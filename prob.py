#!/usr/bin/python3
#Introduction to Random Strings
import math

def main():
    output = []
    for gc in input:
        prob_gc = gc / 2
        prob_at = 0.5 - prob_gc

        total = 1
        for code in dna:
            if code == 'A' or code == 'T': total *= prob_at
            elif code == 'G' or code == 'C' : total *= prob_gc
        output.append(math.log(total, 10))

    with open('output.txt', 'w') as f:
        output = ['%.3f' % prob for prob in output]
        f.write(' '.join(output))

if __name__ == '__main__':
    with open('data/rosalind_prob.txt') as f:
        dna = f.readline().strip()
        input = map(float, f.readline().strip().split())
        main()
