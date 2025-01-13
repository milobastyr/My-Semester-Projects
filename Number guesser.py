#11/8/2024

#Initialize
import random

y=random.randint(0,10)

def num_guesser():
    x=int(input("Pick a number one through 10")) #Asks for input 
    if x==y:
        print("you are correct play again?") #
    elif (x!=y):
        print("you are not correct try again")
    print(y)
    if (x>y):
        print("you are too high")
    elif (x<y):
        print("you are too low")
    elif (x==y):
        print("you are equal")


#Main
num_guesser()

