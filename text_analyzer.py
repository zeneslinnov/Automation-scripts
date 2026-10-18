import string

def word_counter(the_word, text):
    counter = 0
    the_word_clean = the_word.lower().strip(string.punctuation)
    
    for word in text.split():
        word_cleaned = word.lower().strip(string.punctuation)
        
        if word_cleaned == the_word_clean:
            counter += 1
            
    return counter

text = input("Masukkan teks: ")

length = len(text)
words = len(text.split())
length_no_space = 0

for word in text.split():
    for letter in word:
        length_no_space += 1

print("")
print(f"Characters: {length}")
print(f"Words: {words}")
print(f"Character (no space): {length_no_space}")

wanted_word = input("Wanted word: ").lower()
print(f"{word_counter(wanted_word, text)}")

