#!/bin/bash
#Finding a Motif in DNA

eval "$(awk '{ print "d"NR"="$1 }' data/rosalind_subs.txt)"
sl=${#d1}
tl=${#d2}

for ((i=0 ; i<sl ; i++)); do
	if [ "${d1:$i:$tl}" == "${d2}" ]; then
		echo -n $((i+1))' ' >> output.txt
	fi
done
