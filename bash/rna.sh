#!/bin/bash
#Transcribing DNA into RNA

rna=""
while read -r -n1 code
do
	[ "$code" == "T" ] && code="U"
	rna+="${code}"
done < data/rosalind_rna.txt

echo $rna > output.txt
