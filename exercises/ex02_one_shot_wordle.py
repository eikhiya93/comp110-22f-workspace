"""One shot wordle."""

__author__ = "730597174"

# Part 1
secret_word: str =  "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess?: ") 
while len(secret_word) != len(guess): 
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
if secret_word != guess: 
    print("Not quite. Play again soon!")
else: 
    print("Woo! You got it!")

# Part 2
counter: int = 0 
storage_for_emoji: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while counter < len(secret_word): 
    if guess[counter] == secret_word[counter]:
        storage_for_emoji = storage_for_emoji + GREEN_BOX
        counter += 1
    else:
        character_exist: bool = False
        second_counter: int = 0
        while character_exist != True and second_counter < len(secret_word):
            if secret_word[second_counter] == guess[counter]:
                character_exist = True
            else: 
                second_counter += 1
        if character_exist == True: 
            storage_for_emoji += YELLOW_BOX
            counter += 1
        else: 
            storage_for_emoji += WHITE_BOX
            counter += 1

print(storage_for_emoji)