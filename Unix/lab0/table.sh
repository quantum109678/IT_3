if [ $# -eq 0 ]
then
echo "Error - Numbering missing from command line argument"
echo "Syntax :$0 number"
echo "Use to print multiplication table of the given number"
fi
n=$1
for i in 1 2 3 4 5 6 7 8 9 10
do 
echo "$n * $i =`expr $i \* $n`"
done
