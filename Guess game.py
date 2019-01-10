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






















string2 = "Join"
list2 = list(string2)
print(list2)

string3 = "myth"
list3 = list(string3)
print(list3)

string4 = "phone"
list4 = list(string4)
print(list4)

string5 = "laptop"
list5 = list(string5)
print(list5)

string6 = "desk"
list6 = list(string6)
print(list6)

string7 = "light"
list7 = list(string7)
print(list7)

string8 = "handle"
list8 = list(string8)
print(list8)

string9 = "kid"
list9 = list(string9)
print(list9)

string10 = "pencil"
list10 = list(string10)
print(list10)
