#IFS='$twoliner'
twoliner="This is line 1.
This is line 2."
echo "$twoliner"
echo $twoliner
echo
echo $IFS | cat -vE
