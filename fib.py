#!/usr/bin/python3
#Rabbits and Recurrence Relations

with open('data/rosalind_fib.txt', 'r') as f:
    n, k = map(int, f.read().strip().split())

def rabbit(n, k):
    memo = [0]*n
    for i in range(n):
        if i == 0 or i == 1:
            memo[i] = 1
        else:
            memo[i] = memo[i-2]*k + memo[i-1]
    return memo[-1]

print(rabbit(n, k))
