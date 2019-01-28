import random
Guesses = 10
words = ["crypt", "Join", "myth", "phone", "laptop", "desk", "light", "handle", "kid", "edison's"]
answer = random.choice(words)
print("You have 10 tries.")
letters_guessed = ["'"]

# crypt code

if answer == "crypt":
    string1 = "crypt"
    list1 = list(string1)
    ("*".join(list1))

# Join code

if answer == "Join":
    print("1st letter upper cased")
    string2 = "Join"
    list2 = list(string2)
    ("*".join(list2))

# myth code

if answer == "myth":
    string3 = "myth"
    list3 = list(string3)
    ("*".join(list3))

# phone code

if answer == "phone":
    string4 = "phone"
    list4 = list(string4)
    ("*".join(list4))

# laptop code

if answer == "laptop":
    string5 = "laptop"
    list5 = list(string5)
    ("*".join(list5))

# desk code

if answer == "desk":
    string6 = "desk"
    list6 = list(string6)
    ("*".join(list6))

# light code

if answer == "light":
    string7 = "light"
    list7 = list(string7)
    ("*".join(list7))

# handle code

if answer == "handle":
    string8 = "handle"
    list8 = list(string8)
    ("*".join(list8))

# kid code

if answer == "kid":
    string9 = "kid"
    list9 = list(string9)
    ("*".join(list9))

# edison's code

if answer == "edison's":
    string10 = "edison's"
    list10 = list(string10)
    ("*".join(list10))

while Guesses > 0:
    output = []
    guess = input("Guess a letter.")
    letters_guessed.append(guess)
    print(letters_guessed)
    for letter in answer:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("_ ")
    print("".join(output))
    if output == list(answer):
        print("You got it")
        Guesses -= 10
    if guess in answer:
        print(guess)
    elif guess != answer:
        Guesses -= 1
        print("Wrong letter")
