import string

def word_counter(the_word, text):
    counter = 0
    the_word_clean = the_word.lower().strip(string.punctuation)
    
    for word in text.split():
        word_cleaned = word.lower().strip(string.punctuation)
        
        if word_cleaned == the_word_clean:
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
        print("1. Type the text")
        print("2. Read from file")
        print("0. Exit")
        choice = input()
        
        if choice.isdigit() and int(choice) == 0:
            break
            
        elif choice.isdigit() and int(choice) == 1:
            text = input("\nPut your text: ")
        
        elif choice.isdigit() and int(choice) == 2:
            source = input("\nPut the file name here: ")
            with open(source, "r") as file:
                text = file.read()
                print(f"\n{text}")
        
        else:
            print("\nInput tidak valid!")
            continue
        
        length = calc_length(text)
        word = calc_words(text)
        character = calc_length_no_space(text)
        
        with open("report.txt", "w") as file:
            file.write(f"Length: {length}\n")
            file.write(f"Words: {word}\n")
            file.write(f"Characters: {character}\n")
        
        print("\nType 1 if you want to search for a word")
        opt = input()
        
        if opt.isdigit() and int(opt) == 1:
            wanted_word = input("\nWanted word: ").lower()
            
            num_of_word = word_counter(wanted_word, text)
            with open("report.txt", "a") as file:
                file.write(f"Occurences({wanted_word}): {num_of_word}")
        
        print()
        
main()
