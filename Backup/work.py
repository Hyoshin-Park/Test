
import re

regex = r'\([^)]*\)'
word = input("Enter word: ")

text = re.sub(regex,'', word)
text_word = " ".join(text.split())
print(text_word)
