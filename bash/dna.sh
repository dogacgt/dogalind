#!/bin/bash
#Counting DNA Nucleotides

a=0
c=0
g=0
t=0

while read -n1 code
do
	case $code in
		A)	a=$(( $a + 1 ))	;;
		C)	c=$(( $c + 1 ))	;;
		G)	g=$(( $g + 1 ))	;;
		T)	t=$(( $t + 1 ))	;;
	esac
done < data/rosalind_dna.txt

echo $a $c $g $t
