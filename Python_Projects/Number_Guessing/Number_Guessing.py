import random
from logo import number_guess

print(number_guess)

guess_num = random.randint(1,100)
print(guess_num)


def compare(user_input, computer_input):
    if user_input > computer_input:
        print("Too high.")
        print("Guess again.")
    elif user_input < computer_input:
        print("Too Low.")
        print("Guess again.")
    else: 
        print(f"You got it! the number was {computer_input}")
        exit()


print("Welcome to the Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


if level == "easy":
    for chance in range(10,0,-1):
        print(f"You have {chance} attempt remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        compare(user_guess,guess_num)

elif level == "hard":
     for chance in range(5,0,-1):
        print(f"You have {chance} attempt remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        compare(user_guess,guess_num)
else:
    print("Invalid Input")




