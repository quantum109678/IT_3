echo "Enter the first name"
read f1
echo "Enter second name"
read f2
if test -f $f1
then
if test -f $f2
then
cat $f1 >> $f2
cat $f2
else
echo "Second one is not a file"
fi
else
echo "First one is not a file"
fi

