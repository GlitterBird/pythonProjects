import art

print(art.logo)
all_bids = {}
highest_bid = 0
person_with_highest = "x"
keep_going = True

while keep_going:
    name = input("Please enter your name: ")
    bid = int(input("Please enter how much you would like to bid: $"))
    keep_running = input("Is there a bidder after you? Type 'yes' if there is and 'no' if there isn't: ")

    all_bids[name] = bid

    if keep_running == "yes":
        keep_going = True
    else:
        keep_going = False

    print("\n"*10000)

for each_bid in all_bids:
    money = all_bids[each_bid]

    if money > highest_bid:
        highest_bid = money
        person_with_highest = each_bid

print(f"{person_with_highest} had the highest bid of ${highest_bid}. Thus they win the silent auction!")