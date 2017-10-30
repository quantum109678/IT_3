echo "Enter 5 numbers"
declare -a arr
for ((i=0;i<5;i++))
do
read arr[$i]
done
for ((i=0;i<5;i++))
do
for ((j=i+1;j<5;j++))
do
if [ ${arr[$j]} -gt ${arr[$i]} ]
then
num=${arr[$j]}
arr[$j]=${arr[$i]}
arr[$i]=$num
fi
done 
done
min=${arr[4]}
max=${arr[0]}
minc=0
maxc=0
for ((i=3;i>=0;i--))
do
if [ ${arr[$i]} -eq $min ]
then
minc=`expr $minc + 1`
fi
done

for ((i=1;i<5;i++))
do
if [ ${arr[$i]} -eq $max ]
then
maxc=`expr $maxc + 1`
fi
done


if [ $minc -gt 0 ]
then
echo "Min=${arr[4]} and repeated ${minc+1} times"
else
echo "Min=${arr[4]}"
fi

if [ $maxc -gt 0 ]
then
echo "Max=${arr[0]} and repeated ${maxc+1} times"
else
echo "Max=${arr[0]}"
fi


