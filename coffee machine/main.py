import recipes
AMOUNTS = recipes.resources
TYPE = recipes.MENU
profit = 0
water = AMOUNTS["water"]
milk = AMOUNTS["milk"]
coffee = AMOUNTS["coffee"]
is_on = True
order = ""


def take_order():
    global is_on, order
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        report()
    else:
        calc_money()


def report():
    global profit, water, milk, coffee
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nProfit: ${profit}")


def calc_money():
    global profit, order, water, milk, coffee
    order_name = TYPE[order]
    elements = [water, milk, coffee]
    x = 0
    not_possible = False
    ran_out = ""
    for i in order_name["ingredients"]:
        if elements[x] < order_name["ingredients"][i]:
            not_possible = True
            ran_out = i
        x += 1
    if not_possible:
        print(f"Sorry there is not enough {ran_out}.")
    else:
        print("Please insert coins.")
        quarters = 0.25 * int(input("How many quarters? "))
        dimes = 0.10 * int(input("How many dimes? "))
        nickels = 0.05 * int(input("How many nickels? "))
        pennies = 0.01 * int(input("How many pennies? "))
        amount_payed = round(quarters + dimes + nickels + pennies, 2)
        cost_of_order = order_name["cost"]
        if amount_payed < cost_of_order:
            print("Sorry that's not enough money. Money refunded.")
        else:
            return_amount = round(amount_payed - cost_of_order, 2)
            profit += cost_of_order
            print(f"Here is ${return_amount} in change.")
            water -= order_name["ingredients"]["water"]
            milk -= order_name["ingredients"]["milk"]
            coffee -= order_name["ingredients"]["coffee"]
            print(f"Here is your {order}. Enjoy!")


while is_on:
    take_order()
