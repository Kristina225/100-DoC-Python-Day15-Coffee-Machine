from time import sleep
from variables import DRINKS, current_change
from helper_functions import get_order, get_money, cancel_order, deduct_ingredients, reset_change, increase_change, \
    get_available_drinks, is_drinks_empty

machine_is_running = True


def coffee_machine() -> bool:
    """Coffee machine program makes a list of available drinks
    in exchange for money entered by users.
    Returns False when the machine runs out of ingredients
    to make any drink. Returns True after all other transactions."""
    available_drinks = get_available_drinks()
    if not is_drinks_empty(available_drinks):
        return False
    drink = get_order(available_drinks)
    price = DRINKS[drink]['price_USD']
    print(f"Excellent choice! That would be {price}.")
    money = get_money(0)
    while money < price:
        print(f"Sorry, you're still missing {round(price - money, 1)} USD for your drink.\n"
              f"Would you like to add more money, or cancel and get your {money} USD back.")
        cancel = cancel_order()
        if cancel:
            reset_change()
            print(f"Here is your refund: {money} USD.")
            return True
        money = get_money(money)
    print(f"Here is your change: {round(money - price, 1)} USD.\nPlease wait a few seconds for your order.")
    sleep(3)
    print(f"And here is your {drink}. Enjoy!")
    increase_change()
    reset_change()
    deduct_ingredients(drink)
    return True


if __name__ == '__main__':
    while machine_is_running:
        machine_is_running = coffee_machine()
