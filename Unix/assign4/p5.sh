echo "Initial file:"
cat sed.txt
sed -i '1s/^/<HTML> /' sed.txt
sed -i  '$a</HTML>' sed.txt
echo "File after insertion:"
cat sed.txt