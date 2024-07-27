
from importlib.metadata import version
import tiktoken

# QNote: This is important, getting gpt2 provided tokens.
tokenizer = tiktoken.get_encoding("gpt2")

text = ("Hello, do you like tea? <|endoftext|> In the sunlit terraces"
     	"of someunknownPlace."
		)

print("Original text follows:")
print(text)

integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print("Encoded values:")
print(integers)

strings = tokenizer.decode(integers)
print("Decoded text:")
print(strings)

print("Test value", tokenizer.decode([27271]))
