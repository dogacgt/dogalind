#!/usr/bin/env python
#Comparing Spectra with the Spectral Convolution

with open('data/rosalind_conv.txt', 'r') as f:
    S1 = [float(i) for i in f.readline().rstrip('\n').split()]
    S2 = [float(i) for i in f.readline().rstrip('\n').split()]


subs = []
for i in S1:
    for j in S2:
        if i-j not in subs:
            subs.append("%.5f" % (i-j))

count = 0
for i in subs:
    if subs.count(i) > count:
        count = subs.count(i)
        max = i

with open('output.txt', 'w') as f:
    f.write(str(count) + '\n')
    f.write(max)
