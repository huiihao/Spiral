#!/bin/bash
rm log4th
file='E4thmin'
mkdir allCONTCAR-right/$file

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
        maxDate=${indexlist[0]}
        #echo $maxDate
        for k in ${indexlist[@]}
        do
#if [[ ${maxDate} -gt $k ]];then
                if [ ` echo "$k > $maxDate"| bc -l` -eq 1 ];then
                        maxDate=$k
                fi
        done

        for((k=0;k<${#indexlist[*]};k++))
        do
                if [ "${indexlist[k]}" = "$maxDate" ];then
                        if [ "$k" = 0 ];then
                                echo $a $b A $maxDate >> log4th
                                cp iniA/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        elif [ "$k" = 1 ];then
                                echo $a $b B $maxDate >> log4th
                                cp iniB/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        elif [ "$k" = 2 ];then
                                echo $a $b C $maxDate >> log4th
                                cp iniC/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        elif [ "$k" = 3 ];then
                                echo $a $b D $maxDate >> log4th
                                cp iniD/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        fi
                fi
        done
done
done

