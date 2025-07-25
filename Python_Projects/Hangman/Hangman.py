import random
from hangman_words import word_list
from hangman_art import stages,logo

print(logo)

lives = 0

chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"*************************** {lives}/6 LIVES USED *************************")
    guess = input("Guess a letter : ").lower()

    if guess in correct_letters:
        print(f"You,ve already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives += 1
        print(f"You have guessed {guess}, that's not in the word. You lose a life")

        if lives == len(stages) - 1:
            game_over = True
            print(f"******************** IT WAS {chosen_word}! YOU LOSE ********************")

    print(display)

    if "_" not in display:
        game_over = True
        print("************************* YOU WON! ************************")

    print(stages[lives])