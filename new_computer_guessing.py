import random


# Part 1: source code for human guessing the secret number created by computer...
# main game function...
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
            print("Congratulations you have won the game")
            break
        guess_count += 1

    else:
        print("Sorry you lost the game")




# function call..
get_guess(x)

# source code for computer guessing the secret number thought by human..
print('''
NOw the game of computer vs human.. 
''')

def computer_guess(y):
    lower_boundary = 1
    higher_boundary = y
    human_response = ""

    while human_response != "correct":
        guess = random.randint(lower_boundary, higher_boundary)
        human_response = input(f"Is the computer guess of {guess} too High, too Low, or Correct? :").lower()

        if human_response == "high":
            higher_boundary = guess -1
        elif human_response == "low":
            lower_boundary = guess +1

    print("Yay.. congrats to the computer, you beat the human player...")


computer_guess(y)

