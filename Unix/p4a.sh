for ((i=1;i<5;i++))
do
k=$i
for ((j=1;j<2*$i;j++))
do
if [ $j -le $i ]
then
echo -n "$k"
k=$(($k+1))
m=$(($k-1))
else
m=$(($m-1))
echo -n "$m"
fi
done
echo
done
