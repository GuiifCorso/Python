import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
        "quarter": 0.25,
        "dimes": 0.1,
        "nickel": 0.05,
        "pennies": 0.01
}

total = 0

def off():
    print("Turning off...")

#Report the avaible ingredients
def report_ingredients():
    report = input("Would you like to see how much ingredients we have avaible? Type report for yes, or no for no: ")
    while report not in ("report", "no", "off"):
        report = input("Would you like to see how much ingredients we have avaible? Type report for yes, or no for no: ")
    if report == "report":
        display_ingredients()
        display_option()
    elif report == "no":
        display_option()
    else:
        off()

#Ask the client option from menu
def ask_option():
    option = input("What would you like? (espresso/latte/cappuccino): ")
    while option not in ("espresso", "latte", "cappuccino", "off"):
        print("Enter a valid option, please.")
        option = input("What would you like? (espresso/latte/cappuccino): ")
    return option

def display_option():
    option = ask_option()
    check_ingredients(option)

def display_ingredients():
    for resource in resources:
        if resource == "coffee":
           print(resource, ": ", resources[resource], "g", sep="") 
        else:
            print(resource, ": ", resources[resource], "ml", sep="")

def check_ingredients(option):
    info = MENU[option]
    print("Your", option, "requires: ")
    for ingredient in info["ingredients"]:
        if ingredient == "coffee":
           print(ingredient, ": ", info["ingredients"][ingredient], "g", sep="")
           pass
        else:
            print(ingredient, ": ", info["ingredients"][ingredient], "ml", sep="")

        if info["ingredients"][ingredient] > resources[ingredient]:
            print("There is not enough", ingredient)
            display_option()
    print("Cost: ", info["cost"], "$", sep="")

    follow = input(f"Would you like to continue? Your actual option is: {option}\nType yes for continue or no to stop: ")
    while follow.lower() not in ("yes", "no", "off"):
        print("Enter a valid command, please.")
        follow = input(f"Would you like to continue? Your actual option is: {option} \nType yes for continue or no to stop: ")
    if follow.lower() == "off":
        off()
    elif follow.lower() == "yes":
        pass
    else:
        report_ingredients()
    payment(option)

def payment(option):
    print("The", option, "costs:", MENU[option]["cost"])
    global total

    while total < MENU[option]["cost"]:
        user_coins = []
        print(f"You actually have: {total}$")
        print(f"Write *in order* how many coins do you want to insert, and press enter to go to the next coin")
        for i, coin in enumerate(coins):
            print(f"{i+1}. {coin}")
            value = input(f"How many {coin}? ")
            user_coins.append(value)
        total = update_value(user_coins)
        follow = input(f"Would you like to continue inserting coins? You already have {total}$. Y/N? ")
        while follow.upper() not in ("Y", "N"):
            print("Please, enter a valid input.")
            follow = input(f"Would you like to continue inserting coins? You already have {total}$. Y/N: ")
        if follow.upper() == "Y":
            continue
        else:
            if total < MENU[option]["cost"]:
                print(f"You don't have enough money. The {option} costs {MENU[option]["cost"]}$, but you have only {total}")
                pass

    buy = input("You already have the amount necessary to buy your drink. Should we continue? Y/N: ")
    while buy.upper() not in ("Y", "N"):
        print("Please, enter a valid input.")
        buy = input("You already have the amount necessary to buy your drink. Should we continue? Y/N: ")
    if buy.upper() == "Y":
        buy_drink(option, total)
    else:
        report_ingredients()

def buy_drink(option, total):
    print(f"You are buying a {option}. Wait a few seconds...")
    time.sleep(3)
    update_ingredients(option)
    print("Your drink is done! Thank you for choosing us! Bye bye.")
    print(f"Your coins refund is: {total - float(MENU[option]["cost"])}$")
    total = 0
    time.sleep(5)
    display_option()
        
def update_ingredients(option):
    info = MENU[option]
    for ingredient in info["ingredients"]:
        resources[ingredient] -= info["ingredients"][ingredient]
    return resources

def update_value(user_coins):
    i = 0
    coins_values = [0.25, 0.1, 0.05, 0.01]
    total = 0
    for coin in user_coins:
        value = coins_values[i]
        total += int(coin) * value
        i += 1
    return total

report_ingredients()

