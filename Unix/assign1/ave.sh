s=0
echo "Enter number of elements"
read n
echo "Enter the elements"
for (( i=0;i<n;i++ ))
do
read num
s=`expr $s + $num`
done
echo "Average = "
echo "scale=2; $s/$n" | bc
