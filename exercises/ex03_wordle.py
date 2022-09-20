"""Structured Wordle."""

__author__ = "730597174"

# Part 1. Contains_char
def contains_char(s: str, g: str) -> bool: 
    """Matching the index of the guess word to secret."""
    assert len(g) == 1 
    counter: int = 0
    while counter < len(s):
        if s[counter] == g: 
            return True
        else: 
            counter += 1
    return False 

# Part 2. emojified
def emojified(guess: str, secret: str) -> str: 
    """Matching the right color box."""
    assert len(guess) == len(secret)
    storage_for_emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    counter: int = 0
    while counter < len(secret):
        if guess[counter] == secret[counter]:
            storage_for_emoji += GREEN_BOX
        elif contains_char(secret, guess[counter]):
            storage_for_emoji += YELLOW_BOX
        else: 
            storage_for_emoji += WHITE_BOX
        counter += 1
    return storage_for_emoji

# Part 3. Input guess 
def input_guess(a: int) -> str:
    """Input a word with the correct length as the secret word."""
    guess: str = input(f"Enter a {a} character word: ")
    while len(guess) != a:
        guess = input(f"That wasn't {a} chars! Try again: ")
    return guess

# Part 4. Main
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    counter: int = 0
    correct: bool = False
    while counter < 6 and correct == False: 
        print(f"=== Turn {counter + 1}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            correct == True 
            return f"You won in {counter + 1}/6 turns!"
        else: 
            counter += 1
    print("X/6 - Sorry, try again tomorrow!")
    if __name__ == "__main__":
        main()
