
import re

text = "Hello world. This, is a test."

# Basic tokenization on spaces
result = re.split(r'(\s)', text)
print(result)

# Better tokenization (no punctuation stuck to words)
res2 = re.split(r'([,.]|\s)', text)
print(res2)

# Cleaner tokenization (empty elements removed)
cleanResult = [element.strip() for element in res2 if element.strip()]
print(cleanResult)

# More expressive code version of the above 
clean2 = []
for element in res2: 
	trimmedElement = element.strip()
	if trimmedElement != "":
		clean2.append(trimmedElement)
print(clean2)

# Handling text w/ more punctuation 
text2 = "Hello world.  This-- has more useful? punctuation."
res3 = re.split(r'([,.?_!"()\']|--|\s)', text2)
cleanResult2 = [element.strip() for element in res3 if element.strip()]
print(cleanResult2)

# Get 20kb text sample 
with open("./Data/theVerdict.txt", "r", encoding="utf-8") as f:
	rawText = f.read()
print("Total number of characters in raw text file:", len(rawText))
print(rawText[:42])

# Tokenize 20kb text sample 
cleanSample = re.split(r'([,.?_!"()\']|--|\s)', rawText)
docTextTokens = [element.strip() for element in cleanSample if element.strip()]
print(len(docTextTokens))
print(docTextTokens[:30])

# Sec 2.3 Converting tokens into token IDs
uniqueWords = sorted(list(set(docTextTokens)))
uniqueWordsSize = len(uniqueWords)
print(uniqueWordsSize) 
