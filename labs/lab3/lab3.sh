cat questionone.txt | grep "Success" > questionone2.txt

echo "first question"; cat questionone2.txt | sed 's/ /,/g' | cut -d "," -f1,4 

echo "second question: 1)"; cat books.txt | grep "^[12]"

echo "second question: 2)"; cat books.txt | cut -d ";" -f2 | grep -E "^\s*[JF]"

echo "second question: 3)"; cat books.txt | grep "19"

echo "second question: 4)"; cat books.txt | grep "[^Fiction]$"

echo "second question: 5)"; cat books.txt | grep -E '(Fiction|Fantasy)$'
