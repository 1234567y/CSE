import random
a = random.randint(1, 10)

guesses = 5
playing = True
while guesses > 0 and playing:
    guess = int(input("Guess the number"))
    if guess > a:
        print("Guess is high")
        guesses -= 1
    elif guess < a:
        print("Guess is low")
        guesses -= 1
    elif guess == a:
        print("You got it")
        guesses -= 5














    if guess == answer:
        Guesses -= 10
        print("You got it.")
    elif guess != answer:
        Guesses -= 1
        print(guess)
        print("Wrong letter")