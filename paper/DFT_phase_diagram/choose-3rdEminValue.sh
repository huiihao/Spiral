#!/bin/bash
rm log3rd
file='E3rdmin'
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
        echo $m
        indexlist[$m]=0
        min2ndDate=${indexlist[0]}

        for k in ${indexlist[@]}
        do
                if [ ` echo "$k < $min2ndDate"| bc -l` -eq 1 ];then
                        min2ndDate=$k
                fi
        done


        for((m=0;m<${#indexlist[*]};m++))
        do
                if [ "${indexlist[m]}" = "$min2ndDate" ];then
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
        echo $m
        indexlist[$m]=0
        min3rdDate=${indexlist[0]}

        for k in ${indexlist[@]}
        do
                if [ ` echo "$k < $min3rdDate"| bc -l` -eq 1 ];then
                        min3rdDate=$k
                fi
        done


        for((k=0;k<${#indexlist[*]};k++))
        do
                if [ "${indexlist[k]}" = "$min3rdDate" ];then
                        if [ "$k" = 0 ];then
                                echo $a $b A $min3rdDate >> log3rd
                                cp iniA/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        elif [ "$k" = 1 ];then
                                echo $a $b B $min3rdDate >> log3rd
                                cp iniB/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        elif [ "$k" = 2 ];then
                                echo $a $b C $min3rdDate >> log3rd
                                cp iniC/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        elif [ "$k" = 3 ];then
                                echo $a $b D $min3rdDate >> log3rd
                                cp iniD/a${a}b${b}/CONTCAR ./allCONTCAR-right/$file/CONTCAR_${a}_${b}
                        fi
                fi
        done
done
done

