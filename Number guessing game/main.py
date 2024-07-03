import random

ANSWER = random.randint(0,100)

def guesser(number_of_guesses):
    global ANSWER
    for i in range(number_of_guesses):
        print(f"You have {number_of_guesses - i} remaining chances to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == ANSWER:
            return True
        else:
            if guess > ANSWER:
                print("Too high.")
            else:
                print("Too Low.")
    return False

def easy():
    return guesser(10)

def hard():
    return guesser(5)

def final_result(correct_answer):
    if correct_answer:
        print(f"You got it!")
    else:
        print("You've run out of guesses, you lose.")
    print(f"The correct answer was {ANSWER}.")

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty.lower() == "easy":
    correct_answer = easy()
else:
    correct_answer = hard()

final_result(correct_answer)