## Vending Machine Data ##
vending_machine = {
    1: { # id number
        "name": "Cookie", # id's name
        "price": 0.89 # id's price
    },
    2: {
        "name": "Cigarette",
        "price": 0.25
    },
    3: {
        "name": "Mega Candy Bar",
        "price": 0.93
    },
    4: {
        "name": "Cup Noodle",
        "price": 0.76
    }
}

def display_vending_machine(machine: dict) -> None:
    """The allows the vending machine list to be dynamic.

    Args:
        machine (dict): dictionary that contains everything in the vending machine
    """
    # iterates through dictionary
    for item_id in machine:
        item_name = machine[item_id]["name"]
        item_price = machine[item_id]["price"]
        print(f"{item_id}. {item_price}$ {item_name}")

def calculate(leftover_change: int) -> tuple:
    """This takes in the leftover change and converts it to quarters, dimes, nickels, and pennies.

    Args:
        leftover_change (int): the leftover change that'll be converted to coins
    """

    # converts to quarters
    quarters = leftover_change // 25
    leftover_change %= 25

    # converts to dimes
    dimes = leftover_change // 10
    leftover_change %= 10

    # converts to nickels
    nickels = leftover_change // 5
    leftover_change %= 5

    # leftover will be pennies
    pennies = leftover_change

    return(quarters, dimes, nickels, pennies)

def main() -> None:

    # Vending machine welcome
    print("Welcome to the CPP Vending Machine!")
    display_vending_machine(vending_machine)

    # Main loop that runs the input
    while True:
        # users item that corresponds with the items listed
        user_item = input("\nSelect item (1,2,3,4): ")

        try:
            # determines items name, price, and leftover change
            item_name = vending_machine[int(user_item)]["name"]
            item_price = vending_machine[int(user_item)]["price"]
            item_change = round(1 - item_price, 2)

            # leftover change is converted to various variables
            quarters, dimes, nickels, pennies = calculate(int(item_change * 100))

            # displays the item, cost, and change in exact amount
            print(f"\nItem selected: {item_name}")
            print(f"Item cost: ${item_price}")
            print(f"Change ${item_change}:")
            print(f"\tquarters: {quarters}\n\tDimes: {dimes}\n\tnickels: {nickels}\n\tPennies: {pennies}")
            
            # breaks out of the loop
            break

        except:
            # displays invalid item and will prompt the user to enter a new item
            print("Invalid item, try again!")

if __name__ == "__main__":
    # iykyk
    main()
