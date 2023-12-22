#!/bin/bash
file='Emin'
mkdir allCONTCAR-right/$file
rm log1st

for((i=0;i<=20;i++))
do
    for((j=0;j<=i;j++))
    do
        a=$(echo "3.932 + $i*0.002" | bc -l)
        b=$(echo "3.932 + $j*0.002"| bc -l)
        declare -a indexlist
        indexlist[0]=`grep "free  energy   TOTEN  =" iniA/a${a}b${b}/OUTCAR | tail -1 | awk '{print $5}'`
        indexlist[1]=`grep "free  energy   TOTEN  =" iniB/a${a}b${b}/OUTCAR | tail -1 | awk '{print $5}'`
        indexlist[2]=`grep "free  energy   TOTEN  =" iniC/a${a}b${b}/OUTCAR | tail -1 | awk '{print $5}'`
        indexlist[3]=`grep "free  energy   TOTEN  =" iniD/a${a}b${b}/OUTCAR | tail -1 | awk '{print $5}'`
        #echo ${indexlist[@]}
#indexlist=($A $B $C $D)
        minDate=${indexlist[0]}
        #echo $minDate
        for k in ${indexlist[@]}
        do
#if [[ ${minDate} -gt $k ]];then
                if [ ` echo "$k < $minDate"| bc -l` -eq 1 ];then
                        minDate=$k
                fi
        done

        for((k=0;k<${#indexlist[*]};k++))
        do
                if [ "${indexlist[k]}" = "$minDate" ];then
                        if [ "$k" = 0 ];then
                                echo $a $b A $minDate >> log1st
                                dft=`grep "free  energy   TOTEN  ="  iniA/a${a}b${b}/OUTCAR | tail -1 | awk '{print $5}'`
                                dp=`grep -B1 "Loop time"  iniA/a${a}b${b}/dp/log.lammps | grep -v time | awk '{print $5}'`
                                delta=$(echo "$dp - $dft" | bc -l)
                                echo $a $b A $dft $dp $delta >> Energy-min1st
                                cp iniA/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        elif [ "$k" = 1 ];then
                                echo $a $b B $minDate >> log1st
                                dft=`grep "free  energy   TOTEN  ="  iniB/a${a}b${b}/OUTCAR | tail -1 | awk '{print $5}'`
                                dp=`grep -B1 "Loop time"  iniB/a${a}b${b}/dp/log.lammps | grep -v time | awk '{print $5}'`
                                delta=$(echo "$dp - $dft" | bc -l)
                                echo $a $b B $dft $dp $delta >> Energy-min1st
                                cp iniB/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        elif [ "$k" = 2 ];then
                                echo $a $b C $minDate >> log1st
                                dft=`grep "free  energy   TOTEN  ="  iniC/a${a}b${b}/OUTCAR | tail -1 | awk '{print $5}'`
                                dp=`grep -B1 "Loop time"  iniC/a${a}b${b}/dp/log.lammps | grep -v time | awk '{print $5}'`
                                delta=$(echo "$dp - $dft" | bc -l)
                                echo $a $b C $dft $dp $delta >> Energy-min1st
                                cp iniC/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        elif [ "$k" = 3 ];then
                                echo $a $b D $minDate >> log1st
                                dft=`grep "free  energy   TOTEN  ="  iniD/a${a}b${b}/OUTCAR | tail -1 | awk '{print $5}'`
                                dp=`grep -B1 "Loop time"  iniD/a${a}b${b}/dp/log.lammps | grep -v time | awk '{print $5}'`
                                delta=$(echo "$dp - $dft" | bc -l)
                                echo $a $b D $dft $dp $delta >> Energy-min1st
                                cp iniD/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        fi
                fi
        done
done
done

