
import re
import SimpleTokenizerV1

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
print("Sample first 42 characters: %s" % rawText[:42])

# Tokenize 20kb text sample 
cleanSample = re.split(r'([,.?_!"()\']|--|\s)', rawText)
docTextTokens = [element.strip() for element in cleanSample if element.strip()]
print("Number of tokens %d" % len(docTextTokens))
print("Sample of 30 tokens:")
print(docTextTokens[:30])

# Sec 2.3 Converting tokens into token IDs
uniqueWords = sorted(list(set(docTextTokens)))
uniqueWordsSize = len(uniqueWords)
print("Count unique words: %d" % uniqueWordsSize) 

# Listing 2.2
# Creating a vocabulary 
vocab = {token:integer for integer, token in enumerate(uniqueWords)}
for i, item in enumerate(vocab.items()):
	#print("%d = %s " % (i, item)) 
	print(item)
	if i > 50:
		break

# Listing after 2.3
tokenizer = SimpleTokenizerV1.SimpleTokenizerV1(vocab)
 
# Test with a line found in the data file used to create the vocabulary 
text = """"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)

# Decode the encoded sample text 
print(tokenizer.decode(ids))

# Break it.
try:
	text = "Hello, do you like tea?"
	tokenizer.encode(text)
except:
	print("The test of a missing word in the vocab was caught here.")
	

#Add unknown placeholder token and end of text marker token to the vocab
uniqueWords = sorted(list(set(docTextTokens)))
uniqueWords.extend(["<|endoftext|>", "<|unk|>"])
vocab = {token:integer for integer,token in enumerate(uniqueWords)}
print("With placeholders...")
print(len(vocab.items()))

print ("show last 5 entries in vocab")
for i, item in enumerate(list(vocab.items())[-5:]):
	print(item)

