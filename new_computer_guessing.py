import random


#main game function#
def get_guess(x):
    guess = 0
    random_number = random.randint(1,x)
    num_already_entered = False
    guess_count = 0
    while guess != random_number and guess_count < 3:
        guess = int(input(f" Guess the random number between 1 and {x}: "))

        if guess < random_number:
            if num_already_entered:
                print("OOps!! this number was previously entered .. Try different higher number .. ")
            else:
                num_already_entered = True
                print("sorry.. too low... please try higher number")

        elif guess > random_number:
            if not num_already_entered:
                num_already_entered = True
                print("sorry.. too high ... please try lower number")
            else:
                num_already_entered = False
                print("OOPS... This number was entered previously.. please try different lower number")

        else:
            print("Yay!!... congratulations.. you have guessed the correct number")
            break

        guess_count += 1
    print("Sorry .. you lost the game.. Thanks for playing..")

#function call.. #
get_guess(10)