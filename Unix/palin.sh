echo "Enter the string"
read s
flag=1
l=${#s}
for (( i=0; i<l; i++ ))
do
if test "${s:i:1}" != "${s:l-i-1:1}" 
then 
flag=0
fi
done

if [ $flag -eq 0 ]
then
echo "Not a palindrome"
else
echo "palindrome"
fi

 
