import string

def word_counter(the_word, text):
    counter = 0
    the_word_clean = 
the_word.lower().strip(string.punctuation)
    
    for word in text.split():
        word_cleaned = 
word.lower().strip(string.punctuation)
        
        if word_cleaned == 
the_word_clean:
            counter += 1
            
    return counter

def calc_length(text):
    return len(text)

def calc_words(text):
    return len(text.split())
    
def calc_length_no_space(text):
    length_no_space = 0
    
    clean_text = text.replace(" ", "")
    
    for letter in clean_text:
        length_no_space += 1
        
    return length_no_space

def main():
    print("=========================")
    print("     TEXT ANALYZER")
    print("=========================")
    
    while True: 
        print("Type 0 to exit") 
        print("Put your text here:\n")  
        text = input()
        
        if text.isdigit() and int(text) 
== 0:
            break
        
        print(f"\nLength: 
{calc_length(text)}")
        print(f"Word: 
{calc_words(text)}")
        print(f"Characters: 
{calc_length_no_space(text)}")
        
        print("\nType 1 if you want to 
search for a word")
        opt = input()
        
        if opt.isdigit() and int(opt) == 
1:
            wanted_word = 
input("\nWanted word: ").lower()
            print(f"{word_counter(wanted_word, 
text)}")
        
        print()
        
main()
