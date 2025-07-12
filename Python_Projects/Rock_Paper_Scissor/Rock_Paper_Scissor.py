import random
# # Rock Paper Scissor
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock,paper,scissors]

user_choice = int(input("What is you choices?\nEnter youe choice 0 for rock, 1 for paper and 2 for scissors.\n"))
print("Your Choice: ")
if user_choice >= 0 and user_choice <=2:
    print(game_images[user_choice])

computers_choice = random.randint(0,2)
print("Computer's Choice: ")
print(game_images[computers_choice])

if user_choice >=3 and user_choice < 0:
    print("You typed an invalid number.You Lose!")
elif user_choice == 0 and computers_choice == 2:
    print("You Win!")
elif computers_choice == 0 and user_choice == 2:
    print("You Lose")
elif user_choice > computers_choice:
    print("You Win!")
elif computers_choice > user_choice:
    print("You Lose")
elif user_choice == computers_choice:
    print("It's a draw")
