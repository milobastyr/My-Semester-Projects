
#Initialize
print("Welcome to Mad Libs!")#Welcomes the user to the game
print("You'll be asked to provide some words to fill in the blanks of a story.")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
story="Once upon a time in"+place+",there was a"+adjective+" "+noun+"who loved to "+verb+"." "In the " + place + ", a " + adjective + " " + noun + " decided to " + verb + " all day long.","A " + adjective + " " + noun + " went to " + place + " to " + verb + "."
#For above takes the word the user gave and put it into the story
#Main
print(story) #Prints the whole story


