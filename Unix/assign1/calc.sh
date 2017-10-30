echo "enter two numbers"
read n1
read n2
echo "enter operator"
read op
if [ $n2 == 0 ] && [ "$op" == "/" ]
then 
echo "Division not possible"


else
res=$(echo "scale=2; $n1 $op $n2" | bc)
echo "Result=$res"
fi

