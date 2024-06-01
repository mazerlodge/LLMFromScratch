#!/usr/local/bin/python

import re
import SimpleTokenizerV2


# Get 20kb text sample into a string
with open("./Data/theVerdict.txt", "r", encoding="utf-8") as f:
	rawText = f.read()
print("Total number of characters in raw text used to make vocab:", len(rawText))

# Tokenize 20kb text sample
# Step 1, make an array list of words in the 20kb sample text string 
cleanSample = re.split(r'([,.?_!"()\']|--|\s)', rawText)
docTextTokens = [element.strip() for element in cleanSample if element.strip()]

# Step 1.5, add the |unk| and EOF tokens for unknown words  (v2 enhancement)
docTextTokens.append("<|unk|>")
docTextTokens.append("<|EOF|>")
print("Number of tokens %d" % len(docTextTokens))

# Step 2, Associate unique tokens (array elements) with token IDs
# Get unique words from words in array list (includes some symbols)
uniqueWords = sorted(list(set(docTextTokens)))
uniqueWordsSize = len(uniqueWords)
print("Count unique words: %d" % uniqueWordsSize) 

# Step 3, Store token/ID in a vocabulary dictionary
# Create an instance of the tokenizer (v1) class, populated with vocabulary
vocab = {token:integer for integer, token in enumerate(uniqueWords)}
tokenizer = SimpleTokenizerV2.SimpleTokenizerV2(vocab)

# Set up two text samples separated by EoF token.
text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|EOF|> ".join((text1, text2))
print(text)

tokenizer = SimpleTokenizerV2.SimpleTokenizerV2(vocab)
print("Encoded text:")
print(tokenizer.encode(text))

print("Decoded text:")
print(tokenizer.decode(tokenizer.encode(text)))
