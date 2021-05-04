#!/bin/bash
#Counting Point Mutations

eval $(awk '{ print "d"NR"="$1 }' data/rosalind_hamm.txt)
length=${#d1}

count=0
for ((i=0 ; i<$length ; i++)); do
	if [[ ${d1:$i:1} != ${d2:$i:1} ]]; then
		((count++))
	fi
done
echo $count
