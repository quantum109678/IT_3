declare -a arr
echo "Enter 10 numbers"
for ((i=0;i<10;i++))
do
read arr[$i]
done
p=0
n=0
z=0
for((i=0;i<10;i++))
do
if [ ${arr[$i]} -gt 0 ]
then
p=`expr $p + 1`
else if [ ${arr[$i]} -lt 0 ]
then
n=`expr $n + 1`
else
z=`expr $z + 1`
fi
fi
done

for (( i = 0; i <10; i++ ))
do
for (( j = $i; j <10; j++ ))
do
if [ ${arr[$i]} -gt ${arr[$j]}  ]
then
t=${arr[$i]}
arr[$i]=${arr[$j]}
arr[$j]=$t
fi
done
done

echo "Positive numbers=$p"
echo "Negative numbers=$n"
echo "Zeroes=$z"
echo "Array in ascending order:"
for ((i=0;i<10;i++))
do
echo "${arr[$i]}"
done



