t=`ls -l| cut -c1|wc -l`
for ((i=1;i<=t;i++))
do
if [ "`ls -l| cut -c1| paste -s -d ""| cut -c $i`" == '-' ] && [ "`ls -l| cut -c2| paste -s -d ""| cut -c $i`" == 'r' ] && [ "`ls -l| cut -c3| paste -s -d ""| cut -c $i`" == 'w' ]
then
echo "`ls -l| tr -s " "| cut -d " " -f9| paste -s -d " "| cut -d " " -f$i`" 
fi
done
