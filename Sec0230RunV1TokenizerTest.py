#!/usr/local/bin/python

import re
import SimpleTokenizerV1

# Get 20kb text sample into a string
with open("./Data/theVerdict.txt", "r", encoding="utf-8") as f:
	rawText = f.read()
print("Total number of characters in raw text file:", len(rawText))
print("Sample first 42 characters: %s" % rawText[:42])

# Tokenize 20kb text sample
# Step 1, make an array list of words in the 20kb sample text string 
cleanSample = re.split(r'([,.?_!"()\']|--|\s)', rawText)
docTextTokens = [element.strip() for element in cleanSample if element.strip()]
print("Number of tokens %d" % len(docTextTokens))
print("Sample of 30 tokens:")
print(docTextTokens[:30])

# Step 2, Associate unique tokens (array elements) with token IDs
# Get unique words from words in array list (includes some symbols)
uniqueWords = sorted(list(set(docTextTokens)))
uniqueWordsSize = len(uniqueWords)
print("Count unique words: %d" % uniqueWordsSize) 

# Step 3, Store token/ID in a vocabulary dictionary
# Create an instance of the tokenizer (v1) class, populated with vocabulary
vocab = {token:integer for integer, token in enumerate(uniqueWords)}
tokenizer = SimpleTokenizerV1.SimpleTokenizerV1(vocab)

# Step 4, Test the encoding and decoding process w/ both good and 'bad' (failing) samples
# Encode and Decode test with a line found in the data file used to create the vocabulary 
text = """"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)

print("Original Text:")
print(text)

print("Encoded sample output:")
print(ids)

print("Decoded sample output:")
print(tokenizer.decode(ids))

# Test encoding with a sample including word(s) not in the vocabulary 
try:
	text = "Hello, do you like tea?"
	tokenizer.encode(text)
except:
	print("The test of a missing word in the vocab was caught here.")
	
