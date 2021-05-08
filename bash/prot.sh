#!/bin/bash
#Translating RNA into Protein

declare -A codons
while read -r line; do
	codon=$(echo "$line" | cut -d " " -f1)
	aa=$(echo "$line" | cut -d " " -f2)
	codons[$codon]="$aa"
done < data/codon_table.txt

protein=""
while read -r -n3 code; do
	[ "${codons[$code]}" = "Stop" ] && break
	protein+=${codons[$code]}
done < data/rosalind_prot.txt

echo "$protein" > output.txt
