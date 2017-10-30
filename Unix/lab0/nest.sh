ch=0
echo "1 for UNIX"
echo "2 for LINUX"
echo "Select your choise of OS"
read ch
if [ $ch -eq 1 ]
then
echo "Your choice was UNIX"
else
if [ $ch -eq 2 ]
then
echo "YOur choice was LINUX"
else 
echo "Neither"
fi
fi

