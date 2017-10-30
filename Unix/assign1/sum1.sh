echo "Enter n"
read num
sum=0
for(( i=1;i<=num;i++ ))
do
sum=`expr $sum + $i`
done 
echo "Sum=$sum"
