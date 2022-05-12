import random

randNum = random.randint(1,10)
tries = 0
win = False

print("Please enter your name first then guess a number between 1 & 10: ")
name = input("what is your name?")
print(name)
print("Welcome!")

while not win:
    guess = int(input())
    tries = tries + 1
    if guess == randNum:
        win = True
    elif guess < randNum:
        print("Guess Higher..")
    elif guess > randNum:
        print("Guess Lower..")
if win:
    print("Congratulations you guessed correctly!")
    print("Number of tries: " + str(tries) + " ")
