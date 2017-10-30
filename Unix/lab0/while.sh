if [ -z $1 ]
then
rental="***Unknown vehicle***"
elif [ -n $1 ]
then
rental=$1
fi
case $rental in "car") echo "For $rental Rs20 per km";;
                "van") echo "For $rental Rs 10 per km";;
                "jeep") echo "For $rental Rs5 per km";;
             "bicycle") echo "For $rental 20 ps per km";;
                 *) echo "Sorry I cannot get a $rental for you";;
                 esac
