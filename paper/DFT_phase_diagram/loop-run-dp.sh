#!/bin/bash
CURRENT=`pwd`

for m in A B C D E
do
	for((i=0;i<=20;i++))
	do
	    for((j=0;j<=i;j++))
	    do
	        a=$(echo "3.932 + $i*0.002" | bc -l)
	        b=$(echo "3.932 + $j*0.002" | bc -l)
	
	        cd ini$m/a${a}b${b}
	
	        mkdir dp
	        cd dp
	        cp ../CONTCAR ./POSCAR~
	        cp $CURRENT/pos2lmp.py ./
	        cp $CURRENT/input_npt.lammps ./
	        cp $CURRENT/RunscriptDP ./
	
	        grep -v '0.00000000E+00' POSCAR~ > POSCAR
	        sed 's/Pb/Sr   Pb/g' POSCAR -i
	        sed 's/1     1     3/0     1     1     3/g' POSCAR -i
	        #python pos2lmp.py
	
	        z=`grep -B1 Sr POSCAR | head -1 | awk '{print $3}'`
	        sed -n 1,10p /public9/home/sc54385/hyh/L25_phase-diagram/iniD-right/a3.932b3.932/dp/conf.lmp > c.log
	        grep -A6 "Atoms " /public9/home/sc54385/hyh/L25_phase-diagram/iniD-right/a3.932b3.932/dp/conf.lmp | tail -5 | awk '{print $1,$2}' > h.log
	        grep -A5 "Direct" POSCAR | tail -5 | awk '{printf "%.9f %.9f %.9f\n", $1*'"$a"',$2*'"$b"',$3*'"$z"'}' > t.log
	        paste h.log t.log > ht.log
	        cat c.log ht.log > conf.lmp
	
	        sed 's/3.9320000000/'"$a"'/g' conf.lmp -i
	        sed 's/4.0571624382/'"$z"'/g' conf.lmp -i
	
	        #sbatch -J $m$i-$j RunscriptDP
	        #sleep 3s
	        cd $CURRENT
	     done
	done
done

