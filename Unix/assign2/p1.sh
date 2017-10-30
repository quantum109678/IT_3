if [ $1 -lt 1 ] || [ $2 -lt 1 ]
then
echo "Invalid Input,try again"
else
if [ $1 -gt $2 ]
then
echo "scale=2; $2/$1" | bc
else
echo "scale=2; $1/$2" | bc
fi
fi
 
