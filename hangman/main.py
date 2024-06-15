from replit import clear
import random
import words
import art

print(art.logo)

chosen_word = random.choice(words.word_list)

list = []
already_guessed = []
lives = 6

for letter in chosen_word:
    list.append("_")

print(list)

while "_" in list and lives != 0:

    guess = input("Guess a letter: ").lower()
    clear()

    if guess in list:
        print(f"You have already guessed {guess}. Try another letter.")
    else:
        var = 0

        for letter in chosen_word:
            if guess == letter:
                list[var] = guess

            var += 1

        if guess not in chosen_word:
            print(f"You guessed {guess}. That's not in the word. You lose a life.")
            lives -= 1
            already_guessed.append(guess)

    print(f"wrong letters: {already_guessed}")
    print(art.stages[lives])
    print(f"word: {list}")

if lives == 0:
    print("you lose")
    print(f"the word was {chosen_word}")
else:
    print("YOU WINNNNNN!!!")