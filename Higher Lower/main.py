#Higher Lower game!! guess the number of followers that instagram accounts have!
import game_data
import random
import pyfiglet

data_list = game_data.data
score = 0
correct = True
first = random.randint(0, len(data_list)-1)


def check_answer(first, second):
    global score, correct

    if data_list[first]["follower_count"] > data_list[second]["follower_count"] and guess == "a":
        correct = True
        score += 1
        print(f"You're right! Current score: {score}")
    elif data_list[first]["follower_count"] < data_list[second]["follower_count"] and guess == "b":
        correct = True
        score += 1
        print(f"You're right! Current score: {score}")
    elif data_list[first]["follower_count"] == data_list[second]["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Wrong. Final score: {score}")
        correct = False

    return second


print(pyfiglet.figlet_format("HigherLower", font = "slant"))
while correct:
    second = random.randint(0, len(data_list)-1)

    print(
        f"Compare A: {data_list[first]["name"]} a {data_list[first]["description"]} from {data_list[first]["country"]}")
    print(
        f"Compare B: {data_list[second]["name"]} a {data_list[second]["description"]} from {data_list[second]["country"]}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    first = check_answer(first, second)