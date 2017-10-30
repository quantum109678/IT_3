for ((i=1;i<1000;i++))
do
Number=$i
Length=${#Number}
Sum=0
OldNumber=$Number

while [ $Number -ne  0 ]
do
     Rem=$((Number%10))
     Number=$((Number/10))
     Power=$(echo "$Rem ^ 3" | bc )
     Sum=$((Sum+$Power))
done
if [ $Sum -eq $OldNumber ]
then
    echo "$OldNumber"
fi
done
