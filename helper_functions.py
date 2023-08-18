from variables import resources_ingredients, DRINKS, TYPE_OF_CHANGE, resources_money, current_change


def get_order(drinks: list) -> str:
    """Takes in a list of drinks, asks user to choose one and returns the chosen drink"""
    while True:
        drink = input(f"We have: {', '.join(drinks)}. What would you like to drink?: ")
        if drink not in drinks:
            print("Sorry, we don't serve that.")
        else:
            return drink


def get_available_drinks() -> list:
    """Checks the list of ingredients and returns the list of drinks that can be offered"""
    available_drinks = set()
    drinks = DRINKS.keys()
    ingredients = resources_ingredients.keys()
    for drink in drinks:
        for ingredient in ingredients:
            if DRINKS[drink]["ingredients"][ingredient] < resources_ingredients[ingredient]:
                available_drinks.add(drink)
    return list(available_drinks)


def is_drinks_empty(all_drinks):
    """Takes in a list of drinks and returns False if list is empty, True if it's not"""
    return len(all_drinks) != 0


def get_money(total: float) -> float:
    """Takes in the total money entered by the user so far, if any,
    asks the user for coins and keeps tracks of the entered coins,
    returns the total money entered by the user"""
    for change in TYPE_OF_CHANGE.keys():
        while True:
            money = input(f"How many {change} will you add: ")
            if money.isnumeric():
                break
            else:
                print("I'm sorry. That's not real money. I'll pretend I never saw it.")
        total += TYPE_OF_CHANGE[change] * int(money)
        manage_current_change(change, int(money))
    return total


def cancel_order() -> bool:
    """Asks the user if they wish to cancel their order, returns a Boolean to that effect"""
    while True:
        to_add_money = input("Please enter 'yes' or 'no': ").lower()
        if to_add_money not in ('yes', 'no'):
            print("That's not a valid input. Please try again.")
        else:
            return to_add_money == "no"


def deduct_ingredients(drink: str) -> None:
    """Takes in the drink ordered by the user, deducts the ingredients necessary to make the same drink
    from the available ingredients"""
    for ingredient in DRINKS[drink]["ingredients"]:
        resources_ingredients[ingredient] = \
            resources_ingredients[ingredient] - DRINKS[drink]["ingredients"][ingredient]


def increase_change() -> None:
    """Adds the coins entered by the user to the machine's coins resources"""
    for change, quantity in current_change.items():
        resources_money[change] += quantity


def manage_current_change(type_of_change: str, quantity: int) -> None:
    """Takes in the type and quantity of coins entered by the user and adds them
    to dictionary used for storing the change of the current transaction"""
    current_change[type_of_change] += quantity


def reset_change() -> None:
    """Resets all entry of the current transaction to all 0"""
    for change in current_change:
        current_change[change] = 0
