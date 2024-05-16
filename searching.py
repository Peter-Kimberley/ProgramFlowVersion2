shopping_list = ["Keyboard", "mouse", "monitor", "Mouse matt", "printer", "Paper"]

item_to_find = "printer"
found_at = None

for index in range(len(shopping_list)): # The len allows us to see how many items are in the list
    if shopping_list[index]  == item_to_find:
        found_at = index
        break
    
print("Item found at position {}". format(found_at))

    