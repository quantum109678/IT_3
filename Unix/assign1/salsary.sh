
echo "Enter the basic"
read b
echo "Salary = "
echo "scale=2; $b+ 0.5*$b + 0.35*1.5*$b + 0.08*1.5*$b +0.03*1.5*$b -0.1*1.5*$b" |bc

