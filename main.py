MENU = {
    "Butterscotch":{
        "Ingrediants":{
            "milk":50,
            "butter":40,
            "sugar":30,
            "nuts":10,
            "cream":60,
        },
        "cost": 380,
    },
    "Vanilla": {
        "Ingrediants":{
            "milk":50,
            "sugar":20,
            "cream":40,
            "Vanilla_seeds":30
        },
        "cost":180,
    },
    "Chocolate":{
        "Ingrediants":{
            "milk":50,
            "cocoa_powder":20,
            "sugar":40,
            "cream":40,
            "Vanilla_seeds":10,
            "eggs":2
        },
        "cost":240
    },
    "Strawberry":{
        "Ingrediants":{
            "strawberries":40,
            "lemon_juice":50,
            "milk":50,
            "sugar":30,
            "cream":60,
            "Vanilla_seeds":10
        },
        "cost":125,
    }
}

profit = 0
resources = {
    "milk": 300,
    "sugar": 200, 
    "cream": 300, 
    "butter": 50,
    "nuts": 50,
    "Vanilla_seeds":110,
    "cocoa_powder":30,
    "eggs":20,
    "strawberries":50,
    "lemon_juice":60
}

def is_resource_sufficiants(order_ingrediants):
    for item in order_ingrediants:
        if order_ingrediants[item] >= resources[item]:
            print(f"Sorry there is not enough {item}. ")
            return False
    return True


def process_coins():
    print("please insert money: ")
    total = int(input("how many ruppee: "))
    return total


def is_transaction_successful(money_received, ice_cream_cost):
    if money_received >= ice_cream_cost:
        change = round(money_received - ice_cream_cost, 2)
        print(f"Here is ₹{change} in change")
        global profit
        profit += ice_cream_cost
        return True
    else:
        print("Sorry that's not enough money. Money refund")
        return False



def make_ice_cream(ice_cream_name, order_ingrediants):
    for item in order_ingrediants:
        resources[item] -= order_ingrediants[item]
    print(f"Here is your {ice_cream_name}")

is_on = True
while is_on:
    choice = input("what would you like? \n1. Butterscotch\n2. Vanilla\n3. Chocolate\n4. Strawberry  :")
    if choice == "off":
        is_on:False
    elif choice == "report":
        print(f"Milk:{resources['milk']}ml")
        print(f"Sugar:{resources['sugar']}")
        print(f"Cream:{resources['cream']}")
        print(f"Butter:{resources['butter']}")
        print(f"Nuts:{resources['nuts']}")
        print(f"Vanilla Seeds:{resources['vanilla_seeds']}")
        print(f"Chocolate Power:{resources['cocoa_powder']}")
        print(f"Eggs:{resources['eggs']}")
        print(f"Strawberry:{resources['strawberries']}")
        print(f"Lemon Juice:{resources['lemon_juice']}")
        print(f"Money: ${profit}")
    else:
        ice_cream = MENU[choice]
        if is_resource_sufficiants(ice_cream["Ingrediants"]):
            payment = process_coins()
            if is_transaction_successful(payment, ice_cream['cost']):
                make_ice_cream(choice, ice_cream["Ingrediants"])
