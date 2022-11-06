



MENU = {
    "black_coffee": {
        "ingredents": {
            "water": 50,
            "coffee": 18,

        },
        "cost": 1.5,
    },
    "coffee": {
        "ingredents": {
            "water": 100,
            "milk": 150,
            "coffee": 24,

        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredents": {
            "water": 250,
            "milk": 100,
            "coffee": 24,

        },
        "cost": 3.0,
    },
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
def calculation(coffee_type,ingredents):
    cost = MENU[f"{coffee_type}"]["cost"]
    resources["money"] = cost
    for key in resources:
        menu=MENU[f"{coffee_type}"][f'{ingredents}']
        for key1 in menu:
            if key == key1:
                resources[key]-=menu[key1]
            
    for key in resources:
        if resources[key] < 0:
            return False
        else:
            return True
    
def money(choice_coffee):
    cost_of_coffee = MENU[f"{choice_coffee}"]["cost"]
    print("Please insert coins ")

    quarters = int(input("How many quarters :"))
    dimes = int(input("How many dimes :"))
    nickles = int(input("How many nickles :"))
    pennies = int(input("How many pennies :"))

    total = quarters*0.25 + dimes*0.10 + nickles*0.5 + pennies*0.1
    if total < cost_of_coffee:
        print("Sorry! Thats not enough money ,money Refunded ")
        return False
    else:
        change = (total - cost_of_coffee)
        change = round(change,3)
        print(f"Your {change}$ change ")
        return True
   


another = True

while another:
    choice_coffee = input("What would you like to have (black_coffee/coffee/cappuccino) :")

    def coffee_meachine(choice):

        if choice == "report":
            for key in resources:
                if key == "money":
                    print(f"{key} : {resources[key]} $")
                else:
                    print(f"{key} : {resources[key]} ml")
            return True
        else:
            cal=calculation(choice_coffee,"ingredents")
            if cal==True:
                one_more = money(choice_coffee)
                if one_more==True:
                    print(f" Your {choice_coffee} is ready :)")
                    return True 
                else:
                    return False
            else:
                print("sorry shortage of ingredents")

    another = coffee_meachine(choice_coffee)


