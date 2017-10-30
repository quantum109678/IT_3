echo "Enter a number"
read num
l=${#num}
l=`expr $l - 1`
div=$((10**$l))
while [ $num -gt 0 ]
do
rem=$(($num/$div))
num=$(($num % $div))
div=$(($div/10))
case $rem in
	1) echo -n "one " ;;
	2) echo -n "two " ;;
	3) echo -n  "three " ;;
	4) echo -n "four " ;;
	5) echo -n "five " ;;
	6) echo -n "six " ;;
	7) echo -n "seven " ;;
	8) echo -n "eight " ;;
	9) echo -n "nine " ;;
 	0) echo -n "zero " ;;
	*) echo -n "Invalid " ;;
esac
done
 
