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
    "Money" : 0
}


found = False
while found == False:






      choose = input("What would you like? (espresso/latte/cappuccino): ")
      if choose == "espresso":
            if  MENU["espresso"]["ingredients"]["water"] <= resources["water"]:
                  if  MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
                        print("Please insert coins: ")
                        quaters = int(input("How many quaters?: ")) * 0.25
                        dimes = int(input("How many dimes?: ")) * 0.1
                        nickles = int(input("How many nickles?: ")) * 0.05
                        pennies = int(input("How many pennies?: ")) * 0.01 
                        result = quaters + dimes + nickles +pennies  
                        print(f" Voici le montant que vous avez rentrer {result}") 
                        if result >= MENU["espresso"]["cost"]:
                              change = result - MENU["espresso"]["cost"]
                              print(f"Voici la monnaie {change}.")
                              print("Savourez votre café")
                              
                              resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                              resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                              resources["Money"] += MENU["espresso"]["cost"]
                              print(resources)



                        else:
                              print("Pas assez de credits")

                  else:
                        print("ressoursce not sufficent")
            else:
                  print("ressources not sufficient")

      if choose == "cappuccino":
            if  MENU["cappuccino"]["ingredients"]["water"] <= resources["water"]:
                  if  MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"]:
                        if MENU["cappuccino"]["ingredients"]["coffee"] <= resources["milk"]:
                              print("Please insert coins: ")
                              quaters = int(input("How many quaters?: ")) * 0.25
                              dimes = int(input("How many dimes?: ")) * 0.1
                              nickles = int(input("How many nickles?: ")) * 0.05
                              pennies = int(input("How many pennies?: ")) * 0.01 
                              result = quaters + dimes + nickles +pennies  
                              print(f" Voici le montant que vous avez rentrer {result}") 
                              if result >= MENU["cappuccino"]["cost"]:
                                    change = result - MENU["cappuccino"]["cost"]
                                    print(f"Voici la monnaie {change}.")
                                    print("Savourez votre café")
                                    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                                    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                                    resources["Money"] += MENU["cappuccino"]["cost"]
                                    print(resources)

                              else:
                                    print("Pas assez de credits")

                        else:
                              print("ressoursce not sufficent")
                  else:
                        print("ressources not sufficient")
            else:
                  print("ressources not sufficent")
                      

      if choose == "latte":
            if  MENU["latte"]["ingredients"]["water"] <= resources["water"]:
                  if  MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"]:
                        if MENU["latte"]["ingredients"]["milk"] <= resources["milk"]:
                              print("Please insert coins: ")
                              quaters = int(input("How many quaters?: ")) * 0.25
                              dimes = int(input("How many dimes?: ")) * 0.1
                              nickles = int(input("How many nickles?: ")) * 0.05
                              pennies = int(input("How many pennies?: ")) * 0.01 
                              result = quaters + dimes + nickles +pennies  
                              print(f" Voici le montant que vous avez rentrer {result}") 
                              if result >= MENU["latte"]["cost"]:
                                    change = result - MENU["latte"]["cost"]
                                    print(f"Voici la monnaie {change}.")
                                    print("Savourez votre café")
                                    resources["water"] -= MENU["latte"]["ingredients"]["water"]
                                    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                                    resources["Money"] += MENU["latte"]["cost"]
                                    print(resources)
                              else:
                                    print("Pas assez de credits")
                        else:
                              print("ressoursce not sufficent")
                  else:
                        print("ressources not sufficient")
            else:
                  print("ressources not sufficient")
            
            
      if choose == "report":
            print(resources)
                        
            
