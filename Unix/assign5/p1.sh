echo "PID of current user:"
ps u
echo "Current shell PID:"
ps | sed '2q'