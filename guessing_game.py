'''guessing game
let correct anser be 13'''

correct_guess=13
user_guess = int(input("Please guess a number"))
while  (user_guess != correct_guess):
    if (user_guess < correct_guess):
        print("number is  small,guess bigger number")
        user_guess = int(input("Please guess a number"))
        continue;

    elif(user_guess > correct_guess):
        print("number is  big,guess smaller number")
        user_guess = int(input("Please guess a number"))
        continue;

print("WOW!! WELL DONE .Congratulations!! correct guess CHAMP !!")









