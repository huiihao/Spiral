#!/bin/bash

for file in E2ndmin E3rdmin  E4thmin  Emin
do
	CURRENT=`pwd`
	rm *_Disp.dat
	#count=0
	for((i=0;i<=20;i++))
	do
	    for((j=0;j<=i;j++))
	    do
	        #count=$(echo "$count + 1" | bc )
	        a=$(echo "3.932 + $i*0.002" | bc -l)
	        b=$(echo "3.932 + $j*0.002" | bc -l)
	
	        echo $a $b
		
		cd allCONTCAR-right
		cd $file
	
		mkdir a${a}b${b}
		cd a${a}b${b}
		cp ../CONTCAR_${a}_${b} ./CONTCAR
		
	        #cp $CURRENT/poscar2cif.py ./
	        cp $CURRENT/supercell.py ./
	        cp $CURRENT/calABX3.py ./
	        cp $CURRENT/cif2xsf.py ./
		#cp $CURRENT/vasp2cif ./
	
	        #num=`python  poscar2cif.py CONTCAR| grep  1e-10 |  awk '{print $3}' | sed 's/[()]//g'`
		rm M.cif ; ase convert -i vasp -o cif CONTCAR M.cif
	        #cp CONTCAR_${num}.cif M.cif
	        python supercell.py
	        python cif2xsf.py supercell.cif
	        python calABX3.py 6 12 > d.log
	
	        dA=$(grep "A " d.log | awk '{print $4, $5, $6}')
	        echo $a $b $dA >> $CURRENT/A_Disp.dat
	        dB=$(grep "B " d.log | awk '{print $4, $5, $6}')
	        echo $a $b $dB >> $CURRENT/B_Disp.dat
	
	        cd $CURRENT
	
	    done
	done
	mv A_Disp.dat A_Disp.dat-$file
	mv B_Disp.dat B_Disp.dat-$file
done
