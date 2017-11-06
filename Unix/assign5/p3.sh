echo "File being sorted:"
cat file.txt
sort -n file.txt > abc.txt &
echo "After sorting:"
cat abc.txt
echo "Number of background processes:"
ps -u |wc -l
