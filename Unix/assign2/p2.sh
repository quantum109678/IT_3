echo "Current Home directory :$HOME"
echo "Current user :$USER"
echo "Today is : $(date +%m/%d/%Y) "
echo "Number of users logged in :"
who | wc -l
echo "Terminal:$(tty)"

