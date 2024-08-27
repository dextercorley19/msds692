# 1. Write a script that takes the file 1787.txt and produces a 
# version with all words in lowercase. Delete punctuation, 
# squeeze multiple spaces into one space, and delete empty lines.

# 2. Produce a file with the unique words from file 1787.txt. 
# You can use the output from previous exercise.

# 3. How many unique words do you have?

# 4. Apply similar techniques to this new dataset 

# https://www.gutenberg.org/cache/epub/5200/pg5200.txt
cat 1787.txt | tr -d "\r" | grep -v "^$" | tr -d '[:punct:]' | grep -v '^$' > output.txt

cat output.txt | tr " " "\n" | sort | uniq | grep -v "^[0-9]" | grep -v "^$" > newoutput.txt

wc -w newoutput.txt


cat pg5200.txt | tr -d "\r" | grep -v "^$" | tr -d '[:punct:]' | grep -v '^$' > output2.txt

cat output2.txt | tr " " "\n" | sort | uniq | grep -v "^[0-9]" | grep -v "^$" > newoutput2.txt

wc -w newoutput2.txt