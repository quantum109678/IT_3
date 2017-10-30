
echo "Enter n"
read n
echo -e "Sum of first $n numbers="
sum=$(echo "scale=2;$n*($n+1)/2" | bc)
echo -e $sum
