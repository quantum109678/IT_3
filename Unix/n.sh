echo "Enter n"
read n
sum=$(echo "($n*($n+1))/2" | bc)
echo $sum
