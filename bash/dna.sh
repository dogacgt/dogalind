#!/bin/bash
#Counting DNA Nucleotides

a=g=c=t=0

while read -r -n1 code
do
	case $code in
		A)	((a++))	;;
		C)	((c++))	;;
		G)	((g++))	;;
		T)	((t++))	;;
	esac
done < data/rosalind_dna.txt

echo "$a" "$c" "$g" "$t"
