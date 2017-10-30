echo "files whose names begin with a vowel:"
ls -f| grep -i '^[aeiou].*$'
echo "Number of blank lines in c.txt"
grep -c '^$' c.txt
