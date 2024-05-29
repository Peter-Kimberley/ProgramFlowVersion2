shopping_list = ["Keyboard", "mouse", "monitor", "Mouse matt", \
                 "printer", "Paper"]

item_to_find = "spam"
found_at = None

# # for index in range(len(shopping_list)): # The len allows us 
# to see how many items are in the list
# #     if shopping_list[index]  == item_to_find:
# #         found_at = index
# #         break



if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found at position {}".format(item_to_find))
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found". format(item_to_find))