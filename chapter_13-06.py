'''
(Count words) Write a program that counts the number of words in President
Abraham Lincoln’s Gettysburg Address from http://cs.armstrong.edu/liang/data/
Lincoln.txt.
'''

# NOTE: Mentioned web address is not accessible  http://cs.armstrong.edu/liang/data/Lincoln.txt
# Consider this as a President Abraham Lincoln’s Gettysburg Address
address = '2450 camellia ln ne atlanta, ga 30324 united states'

wordCount = 0
# adding prefix as space to address to fit below logic to avoid number being counted as words
address = ' ' + address
for i in range(len(address) - 1):
    if(str.isspace(address[i]) and str.isalpha(address[i+1])):
        wordCount += 1

print('Number of words in address are', str(wordCount))
