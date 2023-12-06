#!/bin/bash

CURRENT=`pwd`
for ini in A B C D E
do
	mkdir ini$ini
	for((i=0;i<=20;i++))
	do
	    for((j=0;j<=i;j++))
	    do
	        a=$(echo "3.932 + $i*0.002" | bc -l)
	        b=$(echo "3.932 + $j*0.002" | bc -l)
	
	        cd ini$ini
	        rm -r a${a}b${b}
	        cd ..
	
	        cp -r example-ab/z/$ini ini$ini/a${a}b${b}
	        cd  ini$ini/a${a}b${b}
	
	        sed -i 's/1.3.873/'"$a"'/g' POSCAR~
	        sed -i 's/2.3.873/'"$b"'/g' POSCAR~
	
	        mv POSCAR~ POSCAR
	        #sbatch run_zrelax.sh
	        cd $CURRENT
	     done
	done
done

