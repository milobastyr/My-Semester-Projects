#Milo Bastyr

#Init


#1.
def colorList(item, list):
    colorList=["red","black","blue"]
    if "red" in colorList:
        print("Yes red is in this list")
    elif "black" in colorList:
          print("Yes black is in list")
    elif "blue" in colorList:
         print("Yes blue is in the list")
def item_count(item, list):
    colorList=["red","black","blue","blue"]
    x = colorList.count("blue")
    print(x)
def is_list_empty(list):
    colorList=["red","black","blue","blue"]
    if not colorList:
        print("The list is empty")
    else:
        print("The list is not empty")


#Main
item_in_list("red",colorList)
item_count("blue",colorList)
is_list_empty(colorList)
