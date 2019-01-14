import random
Guesses = 10
words = ["crypt", "Join", "myth", "phone", "laptop", "desk", "light", "handle", "kid", "pencil"]
answer = random.choice(words)
print("You have 10 tries.")

# crypt code

if answer == "crypt":
    string1 = "crypt"
    list1 = list(string1)
    print("*".join(list1))

# Join code

if answer == "Join":
    string2 = "Join"
    list2 = list(string2)
    print(list2)

# myth code

if answer == "myth":
    string3 = "myth"
    list3 = list(string3)
    print(list3)

# phone code

if answer == "phone":
    string4 = "phone"
    list4 = list(string4)
    print(list4)

# laptop code

if answer == "laptop":
    string5 = "laptop"
    list5 = list(string5)
    print(list5)

# desk code

if answer == "desk":
    string6 = "desk"
    list6 = list(string6)
    print(list6)

# light code

if answer == "light":
    string7 = "light"
    list7 = list(string7)
    print(list7)

# handle code

if answer == "handle":
    string8 = "handle"
    list8 = list(string8)
    print(list8)

# kid code

if answer == "kid":
    string9 = "kid"
    list9 = list(string9)
    print(list9)

# pencil code

if answer == "pencil":
    string10 = "pencil"
    list10 = list(string10)
    print(list10)

while Guesses > 0:
    guess = input("Guess a letter.")
    if guess == answer:
        Guesses -= 10
        print("You got it.")
    if guess in answer:
        Guesses -= 1
        print(guess)
        print("*".join(answer))
    elif guess != answer:
        Guesses -= 1
        print(guess)
        print("Wrong letter")
