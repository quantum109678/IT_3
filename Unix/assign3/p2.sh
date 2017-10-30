echo "Enter file or directory name"
read n
if test -f $n
then 
echo "`cat $n`"
else if test -d $n
then
cd $n
ls
fi
fi

