"""Choose your own adventure."""

__author__ = "730597174"

points: int = 100
player: str = ""


def main() -> None:
    """The entrypoint of the program and main game loop."""
    global points
    global player
    THUMBS_UP: str = "\U0001F44D"
    THUMBS_DOWN: str = "\U0001F44E"
    still_playing: bool = True
    game_select: int
    continue_playing: str
    greet() 
    while still_playing:
        print("Select the game that you want to play by selecting the corresponding number.")
        print("1: Path Game")
        print("2: Number Game")
        print("3: Rock Paper Scissors")
        game_select = int(input("Make your selection: "))
        if game_select == 1:
            path_game()
        else:
            if game_select == 2:
                number_game()
            else:
                rock_paper_scissor()
        continue_playing = str(input("Would you like to play another game (yes/no): "))
        continue_playing = continue_playing.lower()
        if continue_playing == "no":
            still_playing = False
            print("Thanks for playing!")
            print(f"Final score: {points}%")
            satifsfaction: str = input("Do you enjoy the game (yes/no)? ")
            if satifsfaction == str("yes"):
                print(THUMBS_UP)
            else:
                print(THUMBS_DOWN)
        else:
            print("Lets play again.")
            still_playing = True    


def greet() -> None:
    """Welcome the player."""
    print("Welcome player. Let's play a million dollars game.")
    player: str = input("Before we began, what is your name? ")
    print(f"Good luck {player}, you're going to need it!")


def path_game() -> None: 
    """Game 1 will ask the player to pick a left or right door."""
    global points
    guess: str = input("There are two paths, left and right. Which do you choose? ")
    path: str = ""
    i: int = 0
    while i <= 0: 
        if guess == "left":
            points = points - 25
            path = "Wrong choice! The left path is cover with spike! Better luck next time!"
            print(path)
            print(f"Your current score is {points}.")
            i += 1
        elif guess == "right":
            path = "Good choice, you may continue to the next round."
            print(path)
            print(f"Your current score is {points}.")
            i += 1
        else: 
            if guess != "left" or "right":
                path = "You can only enter 'left' or 'right', try again!"
                print(path)
                i += 1

              
def number_game() -> str: 
    """Game 2 will ask the player to pick a number between 1 and 5."""
    global points
    secret_number: int = 3
    print("For game 2, I'm thinking of a number between 1 and 5.")
    guess: int = int(input("What is the magic number? "))
    if guess == secret_number:
        print(f"Correct! The magic number is {secret_number}.")
        print(f"Your current score is {points}.")
    else: 
        if guess < 1:
            print(f"Opps, that's incorrect. The magic number is {secret_number}. Your guess is way too low, follow the instruction next time!") 
            print("You may continue to the next round but you will get 30 points off for not following the instruction!") 
            points = points - 30
            print(f"Your current score is {points}.")
        elif guess > 5:
            print(f"Opps, that's incorrect. The magic number is {secret_number}. Your guess is way too high, follow the instruction next time!")
            print("You may continue to the next round but you will get 30 points off for not following the instruction!") 
            points = points - 30
            print(f"Your current score is {points}.")
        elif guess != secret_number:
            print("Opps, that's not the magic number. Better luck next time!")
            points = points - 20
            print(f"Your current score is {points}.")


def rock_paper_scissor() -> None:
    """Game 3 is rock, paper, scissor."""
    print("For game 3, we will play a game of rock, paper, scissor.")
    print("To make things more interesting, it will be just one round with either big rewards or big loss.")
    print("If you win, you will get back 50 points. If you lose, you will lose 50 points.")
    print("Sounds fun? Let's do it!")
    global points
    end_game: bool = False
    while end_game == False:     
        r_p_s: list[str] = ["rock", "paper", "scissor"]
        from random import randint
        computer_guess: str = r_p_s[randint(0, 2)] 
        user_guess: str = input("rock...paper...scissor...Go!... ")
        if user_guess == computer_guess:
            print(f"The computer also pick {computer_guess}. It's a tie, let's play agian.")
        else:
            if user_guess == "rock" and computer_guess == r_p_s[1]:
                print("The computer pick paper and paper beats rock, you lose!")
                print("Game over, better luck next time.")
                points = points - 50
                print(f"Your current score is {points}.")
                end_game = True
            else: 
                if user_guess == "rock" and computer_guess == r_p_s[2]:
                    print("The computer pick scissor and rock beats scissor, you win!")
                    print("Congratulation, you beat the computer!!!")
                    points = points + 50
                    print(f"Your current score is {points}.")
                    end_game = True
                else:
                    if user_guess == "paper" and computer_guess == r_p_s[0]:
                        print("The computer pick rock and paper beats rock, you win!")
                        print("Congratulation, you beat the computer!!!")
                        points = points + 50
                        print(f"Your current score is {points}.")
                        end_game = True
                    else: 
                        if user_guess == "paper" and computer_guess == r_p_s[2]:
                            print("The computer pick scissor and scissor beats paper, you lose!")
                            print("Game over, better luck next time.")
                            points = points - 50
                            print(f"Your current score is {points}.")
                            end_game = True
                        else: 
                            if user_guess == "scissor" and computer_guess == r_p_s[0]:
                                print("The computer pick rock and rock beats scissor, you lose!")
                                print("Game over, better luck next time.")
                                points = points - 50
                                print(f"Your current score is {points}.")
                                end_game = True
                            else:
                                if user_guess == "scissor" and computer_guess == r_p_s[1]:
                                    print("The computer pick paper and scissor beats paper, you win!")
                                    print("Congratulation, you beat the computer!!!")
                                    points = points + 50
                                    print(f"Your current score is {points}.")
                                    end_game = True
                                else:
                                    if user_guess != "rock" or "paper" or "scissor":
                                        print("Invalid answer, try again.")


if __name__ == "__main__":
    main()
