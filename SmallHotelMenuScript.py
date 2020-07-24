print("-----------------------------------")
print("Welcome to Ghazali Larik Restaurant")
print("-----------------------------------")

client_name=input("What is your full name: ")
print(f"{client_name}, We have this food items for you today")
print('''1 - Roll
2 - Burger
3 - Tikka''')

client_options=input(f"{client_name}, Which food item you want")
no_items = 0

if client_options == "1":
    print(f"{client_name}, We have these rolls today")
    print('''1 - Chatni Roll
2 - Mayo Roll
3 - Broast Roll''')
    type_of_roll=input("Which type of roll you want")
    if type_of_roll == "1": # Nested if
        no_items=int(input("How many Chatni Rolls you want"))
        print(f"{client_name}, Your Bill is :", no_items*90)
    elif type_of_roll == "2":
        no_items=int(input("How many Mayo Rolls you want"))
        print(f"{client_name}, Your Bill is :", no_items*100)
    elif type_of_roll == "3":
        no_items=int(input("How many Broast Rolls you want"))
        print(f"{client_name}, Your Bill is :", no_items*120)

elif client_options == "2":
    print(f"{client_name}, We have these Burgers today")
    print('''1 - Zinger Burger
2 - Chicken Cheese Burger
3 - Beef Burger''')
    type_of_burger=input("Which type of Burger you want")
    if type_of_burger == "1":
        no_items=int(input("How many Zinger Burgers you want"))
        print(f"{client_name}, Your Bill is :", no_items*150)
    elif type_of_burger == "2":
        no_items=int(input("How many Chicken Cheese Burgers you want"))
        print(f"{client_name}, Your Bill is :", no_items*180)
    elif type_of_burger == "3":
        no_items=int(input("How many Beef Burgers you want"))
        print(f"{client_name}, Your Bill is :", no_items*200)

elif client_options == "3":
    print(f"{client_name}, We have these Tikka Flavours today")
    print('''1 - Chicken Tikka
2 - Green Tikka
3 - Malai Tikka''')
    type_of_tikka=input("Which type of Tikka Flavour you want")
    if type_of_tikka == "1":
        no_items=int(input("How many Chicken Tikka you want"))
        print(f"{client_name}, Your Bill is :", no_items*160)
    elif type_of_tikka == "2":
        no_items=int(input("How many Green Tikka you want"))
        print(f"{client_name}, Your Bill is :", no_items*200)
    elif type_of_tikka == "3":
        no_items=int(input("How many Malai Tikka you want"))
        print(f"{client_name}, Your Bill is :", no_items*250)

else:
    print(f"Sorry {client_name} your selected item is not available")