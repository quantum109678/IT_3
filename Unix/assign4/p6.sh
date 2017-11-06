echo "File before replacemaent:"
cat file.txt
echo "File after replacement:"
sed '1,3s/|/:/g' file.txt

