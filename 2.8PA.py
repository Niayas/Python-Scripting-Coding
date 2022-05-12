import random

leaderboard = ''


replay = True
while replay:
    number_to_guess = random.randint(1,10)
    print("welcome enter your name then guess a number between 1 & 10 to win!")
    name = input("What is your name?")
    print(name)

    score = 0
    game_over = False
    while not game_over:
        guess = int(input('Please enter a number between 1 & 10: '))
        if guess < number_to_guess:
            print("Guess too low...")
            score +=1

        elif guess > number_to_guess:
            print("Guess too high..")
            score +=1
        else:
            print("Correct! You WIN!")
            print("Your score was" + str(score))
            game_over = True
            leaderboard += name + ' ' + str(score) + '\n'
            print(leaderboard)
            again = input("Would you like to play again? (y/n)")
if again == "n":
        replay = False
