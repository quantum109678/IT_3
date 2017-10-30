h=$(date +%H)
m=$(date +%M)
if [ $h -ge 0 ] && [ $h -lt 12 ]
then
echo "Good Morning"
fi
if [ $h -ge 12 ] && [ $h -lt 18 ]
then
echo "Good Afternoon"
fi
if [ $h -ge 18 ] && [ $h -lt 20 ]
then
echo "Good Evening"
fi
if [ $h -ge 20 ] && [ $h -le 23 ]
then
echo "Good Night"
fi


