echo "first question"; cat questionone.txt | sed 's/ /,/g' | cut -d "," -f1,4 

echo "second questions"; 