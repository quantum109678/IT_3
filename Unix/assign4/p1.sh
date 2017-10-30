echo "Enter number of entries to be made"
read n
for((i=0;i<$n;i++))
do
echo "Enter name:"
read f1
echo "Enter address:"
read f2
echo "$f1 $f2" >> address.lst
done
cat address.lst

