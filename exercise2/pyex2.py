# pyex2.py - Word length occurrences in english.sorted

# 1. Create input file object
input_file = open('english.sorted', 'r')

# 2. declare empty dictionary
wordlengths = {}

# 3. iterate through lines of input_file
for word in input_file:
    length = len(word) - 1 # hidden newline
    
    # 4. populate dict
    if (length in wordlengths):
        wordlengths[length] += 1
    else:
        wordlengths[length] = 1

# 5. print word length occurrences table.
print("Word Length\t\tOccurences")

for length in sorted(wordlengths.keys()):
    print(str(length) + "\t\t\t" + str(wordlengths[length]))
