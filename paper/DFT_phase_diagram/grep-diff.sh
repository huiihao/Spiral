#!/bin/bash

echo a b ini Edft Edp Edp-dft > Energy-diff-all
for m in A B C D
do

for((i=0;i<=20;i++))
do
    for((j=0;j<=i;j++))
    do
        a=$(echo "3.932 + $i*0.002" | bc -l)
        b=$(echo "3.932 + $j*0.002"| bc -l)

        dft=`grep "free  energy   TOTEN  ="  ini${m}/a${a}b${b}/OUTCAR | tail -1 | awk '{print $5}'`
        dp=`grep -B1 "Loop time"  ini${m}/a${a}b${b}/dp/log.lammps | grep -v time | awk '{print $5}'`
        delta=$(echo "$dp - $dft" | bc -l)
        echo $a $b $m $dft $dp $delta >> Energy-diff-all
        done
done

done

