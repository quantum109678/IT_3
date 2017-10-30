echo "Enter the string"
read st
l=${#st}
flag=0
for((i=0;i<=l/2;i++))
do
c1="${st:$i:1}"
c2="${st:$l-$i-1:1}" 
if [ $c1 != $c2 ]
then
echo "Not a palindrome"
flag=1
break
fi
done
if [ $flag == 0 ]
then
echo "Palindrome"
fi

