shopping_list = ["Keyboard", "mouse", "monitor", "Mouse matt", "printer"]
for item in shopping_list:
    if item != "printer":
        print("Buy " + item)
print("--------")
    
for item in shopping_list:
    if item == "printer":
        continue # This will continue if the condition is returned true, and will not be added to the code
    print("Buy " + item)
print("--------")

for item in shopping_list:
    if item == "printer":
        break # added a break point for the code, this is good if you want to search through a list of a 1000 items
    print("Buy " + item)
