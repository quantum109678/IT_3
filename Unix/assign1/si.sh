
echo "1 for Simple Interest"
echo "2 for Area"
echo "Enter your choice"
read ch
if [ $ch -eq 1 ]
then
echo "Enter principal amount"
read p
echo "Enter Rate of Interest"
read r
echo "Enter Time"
read t
echo "Simple Interest= "
echo "scale=2; $p*$r*$t/100" | bc
elif [ $ch -eq 2 ]
then
echo "Enter radius"
read r
echo "Area = "
echo "scale=2; $r*$r*3.14" |bc
else
echo "Not valid input"
fi

