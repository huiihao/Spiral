#!/bin/bash
rm log2nd
file='E2ndmin'
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
        minDate=${indexlist[0]}
        for k in ${indexlist[@]}
        do
                if [ ` echo "$k < $minDate"| bc -l` -eq 1 ];then
                        minDate=$k
                fi
        done

        for((m=0;m<${#indexlist[*]};m++))
        do
                if [ "${indexlist[m]}" = "$minDate" ];then
                        if [ "$m" = 0 ];then
                                echo A $m > m.log
                        elif [ "$m" = 1 ];then
                                echo B $m > m.log
                        elif [ "$m" = 2 ];then
                                echo C $m > m.log
                        elif [ "$m" = 3 ];then
                                echo D $m > m.log
                        fi
                fi
        done

        m=`cat m.log | awk '{print $2}'`
        indexlist[$m]=0
        min2ndDate=${indexlist[0]}

        for k in ${indexlist[@]}
        do
                if [ ` echo "$k < $min2ndDate"| bc -l` -eq 1 ];then
                        min2ndDate=$k
                fi
        done


        for((k=0;k<${#indexlist[*]};k++))
        do
                if [ "${indexlist[k]}" = "$min2ndDate" ];then
                        if [ "$k" = 0 ];then
                                echo $a $b A $min2ndDate >> log2nd
                                cp iniA/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        elif [ "$k" = 1 ];then
                                echo $a $b B $min2ndDate >> log2nd
                                cp iniB/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        elif [ "$k" = 2 ];then
                                echo $a $b C $min2ndDate >> log2nd
                                cp iniC/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        elif [ "$k" = 3 ];then
                                echo $a $b D $min2ndDate >> log2nd
                                cp iniD/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        fi
                fi
        done
done
done

