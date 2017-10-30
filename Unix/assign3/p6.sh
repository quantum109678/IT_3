declare -A m1
declare -A m2
r=0
c=0
echo "Enter the number of rows and columns"
read r
read c
echo "Enter the elements of first matrix"
for((i=0;i<r;i++))
do
for((j=0;j<c;j++))
do
read m1[$i,$j]
done
done
echo "Enter the elements of second matrix"
for((i=0;i<r;i++))
do
for((j=0;j<c;j++))
do
read m2[$i,$j]
done
done
for((i=0;i<r;i++))
do
for((j=0;j<c;j++))
do
echo -n $(echo "${m1[$i,$j]} + ${m2[$i,$j]} " | bc)
echo -n " "
done
echo
done



