#!/usr/bin/env python
#Double-Degree Array

#takes quite a while, not optimized

def count_neighbors(D, i):
    arr=[]
    for d in D:
        if i in d:
            if d[0] != i: arr.append(d[0])
            else: arr.append(d[1])

    total = 0
    for i in arr:
        total += (sum(d.count(i) for d in D))
    return total


def main():
    res=[]
    for i in range(1, n+1):
        res.append(str(count_neighbors(D, i)))
    return ' '.join(res)


if __name__ == '__main__':
    with open('data/rosalind_ddeg.txt') as f:
        n, _ = map(int, f.readline().strip().split())
        D = [[int(i) for i in line.strip().split()] for line in f.readlines()]

    with open('output.txt', 'w') as f:
        f.write(main())
