echo "1.Add\n2.Search\n3.Delete\n4.Quit"
read ch
while [ $ch -ne 4 ]
do
	case $ch in
		"1")echo -n "Enter roll number:"
	    	read rn
	    	echo -n "Enter name:"
	    	read name
	    	echo -n "Enter semester:"
	    	read sem
	    	echo -n "Enter marks in sub1:"
	    	read s1
	    	echo -n "Enter marks in sub2:"
	    	read s2
	    	echo -n "Enter marks in sub3:"
	    	read s3
	    	echo "$rn|$name|$sem|$s1|$2|$s3" >> mydb.txt
	    	echo "Successfully added";;
		"2")echo -n "Enter the roll number to be searched for:"
			read srn
			c=wc-l mydb.txt
			flag=0
			for((i=1;i<=$c;i++))
			do
				tmp=`cat mydb.txt| cut -f1 -d "|"| paste -s -d"|"| cut -f$i -d"|"`
				if [ $srn -eq $tmp ]
					then
					flag=1
					echo "Name:`cat mydb.txt| cut -f2 -d "|"| paste -s -d"|"| cut -f$i -d"|"`"
					echo "Semester:`cat mydb.txt| cut -f3 -d "|"| paste -s -d"|"| cut -f$i -d"|"`"
					echo "Subject1:`cat mydb.txt| cut -f4 -d "|"| paste -s -d"|"| cut -f$i -d"|"`"
					echo "Subject2:`cat mydb.txt| cut -f5 -d "|"| paste -s -d"|"| cut -f$i -d"|"`"
					echo "Subject3:`cat mydb.txt| cut -f6 -d "|"| paste -s -d"|"| cut -f$i -d"|"`"
				fi
			done
			if [ $flag -eq 0]
				then
				echo "Not found!"
			fi
			


