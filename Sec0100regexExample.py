#!/usr/local/bin/python

import re

# Sample text for this example
text = "Hello world. This, is a test."

# Basic tokenization on spaces
result = re.split(r'(\s)', text)
print ("Basic tokenization on spaces:")
print(result)

# Better tokenization (no punctuation stuck to words)
print ("Better tokenization on spaces, commas, and periods:")
res2 = re.split(r'([,.]|\s)', text)
print(res2)

# Cleaner tokenization (empty elements removed)
print ("Cleaner output of the above with empty elements removed:")
cleanResult = [element.strip() for element in res2 if element.strip()]
print(cleanResult)

# More expressive code version of the above 
clean2 = []
for element in res2: 
	trimmedElement = element.strip()
	if trimmedElement != "":
		clean2.append(trimmedElement)
print ("Same as above coded in a more expressive manner:")
print(clean2)

# Handling text w/ more punctuation 
text2 = "Hello world.  This-- has more useful? punctuation."
print("More complex example:\n%s" % text2)
res3 = re.split(r'([,.?_!"()\']|--|\s)', text2)
cleanResult2 = [element.strip() for element in res3 if element.strip()]
print("Splitting and stripping on more punctuation")
print(cleanResult2)

# Get 20kb text sample 
with open("./Data/theVerdict.txt", "r", encoding="utf-8") as f:
	rawText = f.read()
print("Total number of characters in raw text file:", len(rawText))
print("Sample first 42 characters: %s" % rawText[:42])

# Tokenize 20kb text sample 
cleanSample = re.split(r'([,.?_!"()\']|--|\s)', rawText)
docTextTokens = [element.strip() for element in cleanSample if element.strip()]
print("Number of tokens %d" % len(docTextTokens))
print("Sample of 30 tokens:")
print(docTextTokens[:30])
