available_exits = ["north", "east", "south", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        break

else:
    print("Aren't you glad that you got out of there")
