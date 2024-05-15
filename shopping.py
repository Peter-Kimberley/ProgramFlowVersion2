shopping_list = ["Keyboard", "mouse", "monitor", "Mouse matt", "printer"]
for item in shopping_list:
    if item != "printer":
        print("Buy " + item)
print("--------")
    
for item in shopping_list:
    if item == "printer":
        continue
    print("Buy " + item)
