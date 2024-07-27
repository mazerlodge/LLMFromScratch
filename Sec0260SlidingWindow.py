#!/usr/local/bin/python3



with open("./Data/theVerdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
 
enc_text = tokenizer.encode(raw_text)
print(len(enc_text))