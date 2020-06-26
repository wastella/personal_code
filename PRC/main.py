from list import CheckList

#example uses:
#Makes new list:
Grocery_List = CheckList("Grocery List")
#Adding tasks to list:
Grocery_List.add_task("apples")
Grocery_List.add_task("banana", "1 banana")
Grocery_List.add_task("orange", "get oranges from giant eagle")
#Printing List Contents:
Grocery_List.show_list()

