#Milo Bastyr

#Init

#Functions
#This functions counts how many words are in a given text
import string 
def word_counter(text):
    x=text.split()
    print(x)
    x = len(x)
    print(x)

#Main
word_counter("This is an example of a text supplied as an argument")

