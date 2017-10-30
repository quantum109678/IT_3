echo "Enter a filename"
read f
echo "User:"
if [ "`ls -l $f|cut -c2`" == "r" ]
then
echo -n "read "
fi
if [ "`ls -l $f|cut -c3`" == "w" ]
then
echo -n "write "
fi
if [ "`ls -l $f|cut -c4`" == "x" ]
then
echo "execute "
fi
echo "Group:"
if [ "`ls -l $f|cut -c5`" == "r" ]
then
echo -n "read "
fi
if [ "`ls -l $f|cut -c6`" == "w" ]
then
echo -n "write "
fi
if [ "`ls -l $f|cut -c7`" == "x" ]
then
echo "execute "
fi
echo "Others:"
if [ "`ls -l $f|cut -c8`" == "r" ]
then
echo -n "read "
fi
if [ "`ls -l $f|cut -c9`" == "w" ]
then
echo -n "write "
fi
if [ "`ls -l $f|cut -c10`" == "x" ]
then
echo -n "execute "
fi

