#!/usr/bin/python3
#Partial Permutations

def main():
    result = 1
    ways = range(1, n+1)
    for j in range(1, k+1):
        result *= ways[-j]
    return result % 10**6

if __name__ == '__main__':
    with open('data/rosalind_pper.txt', 'r') as f:
        n, k = map(int, f.read().strip().split())
        print(main())
