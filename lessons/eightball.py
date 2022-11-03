from random import randint

question: str = input("What is your yes/no question? ")
response: int = randint(0, 2)

if response == 0:
    print("Yes, def")
elif response == 1: 
    print("Ask agian later")
elif response == 2: 
    print("yes ofc")
else: 
    if response == 1: 
        print("My sources say no")

