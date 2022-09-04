"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730597174"

# Part 1

chosen_word: str = input("Enter a 5-character word: ") 
if (len(chosen_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
else: 
    single_character: str = input("Enter a single character: ")
    if (len(single_character) != 1):
        print("Error: Character must be a single character.")
        exit()
    else: 
        print("Seaching for " + single_character + " in " + chosen_word)



# Part 2

number_of_count: int = 0

if (single_character == chosen_word[0]):
   print(single_character + " found at index 0")
   number_of_count = number_of_count + 1
if (single_character == chosen_word[1]):
   print(single_character + " found at index 1")
   number_of_count = number_of_count + 1
if (single_character == chosen_word[2]):
   print(single_character + " found at index 2")
   number_of_count = number_of_count + 1
if (single_character == chosen_word[3]):
   print(single_character + " found at index 3")
   number_of_count = number_of_count + 1
if (single_character == chosen_word[4]):
   print(single_character + " found at index 4")
   number_of_count = number_of_count + 1



# Part 3

if (number_of_count == 0):
   print("No instances of " + single_character + " found in " + chosen_word)  
if (number_of_count == 1): 
    print("1 instance of " + single_character + " found in " + chosen_word)
if (number_of_count == 2):
    print("2 instance of " + single_character + " found in " + chosen_word)
if (number_of_count == 3):
    print("3 instance of " + single_character + " found in " + chosen_word)
if (number_of_count == 4): 
    print("4 instance of " + single_character + " found in " + chosen_word)
if (number_of_count == 5): 
    print("You guess all the letter correctly!!!")
