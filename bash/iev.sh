#!/bin/bash
#Calculating Expected Offspring

vec=($(cat data/rosalind_iev.txt))
prob=(1 1 1 .75 .5 0)

sum=0
for ((i=0 ; i<6 ; i++)); do
	a=`echo ${prob[$i]} ${vec[$i]} | awk '{ print $1 * $2 * 2 }'`
	sum=`echo $sum + $a | bc`
done

echo $sum
