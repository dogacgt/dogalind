#!/bin/bash
#Complementing a Strand of DNA

rev_comp=""
while read -r -n1 code
do
	case $code in
		A)	code="T"	;;
		C)	code="G"	;;
		G)	code="C"	;;
		T)	code="A"	;;
	esac
	rev_comp="${code}${rev_comp}"
done < data/rosalind_revc.txt

echo $rev_comp > output.txt
