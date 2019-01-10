import random
rounds = 0
user_money = 15
playing = True
print(rounds)
print(" You have $ %d" % user_money)
print("You bet $1")
max_money = 15
max_money_round = 0
while user_money > 0 and playing:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print(a+b)
    if a + b == 7:
        print("You win!")
        user_money += 4
        rounds += 1
        print(" You have $ %d" % user_money)
    elif a + b != 7:
        user_money -= 1
        rounds += 1
        print("You lost this bet")
        print(" You have $ %d" % user_money)
    if max_money < user_money:
        max_money = user_money
        max_money_round = rounds
    if user_money == 0:
        print("You lost all your money.")
        print("You played %d rounds" % rounds)
        print("Your max money was %d" % max_money)
        print("You had the max money at round %d" % max_money_round)
