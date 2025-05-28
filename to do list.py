#Milo Bastyr

#1/23/2025

#Initialize

mydestinationlist = []
#Functions
def mydestination_list():
    global mydestinationlist
    print("Welcome to Shop list")
    while True:
        print("What do you wanna do? ")
        print("""1. View the current shopping list
2. Add an item to the shopping list
3. Remove a task from the shopping list
4. Sort the list alphabetically
5. Count and print the # of items on the To-do List
6. Quit
        """)
        Option = int((input("(1-6) Option:")))
        try :
        if Option == 1:
            if not mydestinationlist:
                print("You have nothing on the list")
            else:
                for item in mydestinationlist:
                    print(item)

        if Option == 2:
            item = input("Enter the item to add: ")
            mydestinationlist.append(item)

        if Option == 3:
            item = input("Enter the item to remove: ")
            if item in myShoppinglist:
                mydestinationlist.remove(item)
            else:
                print("Item is not found on your list")
        if Option == 4:
            mydestinationlist.sort()
            print("List sorted alphabetically")
        if Option == 5:
            print(f"Number of items in the list:{len(mydestinationlist)}")
        if Option == 6:
            except
            break


#Main
mydestination_list()
