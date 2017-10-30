d=0
f=0
t=`ls -l| cut -c1| wc -l`
for((i=1;i<=t;i++))
do
if [ "`ls -l| cut -c1| paste -s -d ""| cut -c $i`" == '-' ]
then
f=`expr $f + 1`
else if [ "`ls -l| cut -c1| paste -s -d ""| cut -c $i`" == 'd' ]
then 
d=`expr $d + 1`
fi
fi
done
echo "Number of files=$f"
echo 
echo "Number of directories=$d"
echo
echo "Files:"
for((i=1;i<=t;i++))
do
if [ "`ls -l| cut -c1| paste -s -d ""| cut -c $i`" == '-' ]
then
echo "`ls -l| tr -s " "| cut -d " " -f9| paste -s -d " "| cut -d " " -f$i`" 
fi
done
echo

echo "Directories:"
for((i=1;i<=t;i++))
do
if [ "`ls -l| cut -c1| paste -s -d ""| cut -c $i`" == 'd' ]
then
echo "`ls -l| tr -s " "| cut -d " " -f9| paste -s -d " "| cut -d " " -f$i`" 
fi
done




