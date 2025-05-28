#Milo Bastyr

#Initialize


from PIL import Image
import requests
from io import BytesIO
import random


#Define a function called open_image with a url parameter for the image address
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


#Call your function with an image URL
open_image("https://static.independent.co.uk/2023/07/13/16/iStock-467335200.jpg?width=1200") # 1 Switzerland ski
open_image("https://media.cnn.com/api/v1/images/stellar/prod/230516121517-01-body-crossroads-maldives-aerial.jpg?c=original")#2 Maldives
open_image("https://tinyurl.com/37feje7u")#Rome
open_image("https://www.wendywutours.co.uk/blog/wp-content/uploads/2017/03/japanese-castle-sakura.jpg")#Japan
open_image("https://tinyurl.com/3rrbw8e8")#Athens from https://expertvagabond.com/athens-things-to-do/ and it is published on september 11,2024 by expervagabound


destination_List["https://static.independent.co.uk/2023/07/13/16/iStock-467335200.jpg?width=1200","https://media.cnn.com/api/v1/images/stellar/prod/230516121517-01-body-crossroads-maldives-aerial.jpg?c=original",
"https://tinyurl.com/37feje7u","https://www.wendywutours.co.uk/blog/wp-content/uploads/2017/03/japanese-castle-sakura.jpg",
"https://tinyurl.com/3rrbw8e8"]
from PIL import Image
import requests
from io import BytesIO
import random

#Define a function called open_image with a url parameter for the image address
def open_image(url):

    response = requests.get(url)#HTTP REQUEST IS MADE
    img = Image.open(BytesIO(response.content))
    img.show()


#Call your function with an image URL
print("Welcome to travel  recommender")
while True:
    ans = input("Would you like a recommendation:(Yes/No) ")
    if ans == "Yes":
        random.choice(movies)
        selected_destination = random.choice(destination)
        if selected_destination == "https://static.independent.co.uk/2023/07/13/16/iStock-467335200.jpg?width=1200":
            open_image("https://static.independent.co.uk/2023/07/13/16/iStock-467335200.jpg?width=1200")
            print("Switzerland is know for there winter sports such as skiing and snowboarding with great mountain slopes to go on")
        if selected_destination == "https://media.cnn.com/api/v1/images/stellar/prod/230516121517-01-body-crossroads-maldives-aerial.jpg?c=original":
            open_image("https://media.cnn.com/api/v1/images/stellar/prod/230516121517-01-body-crossroads-maldives-aerial.jpg?c=original")
            print("The maldives is a warm destination with nice villas, clear water and good views")
        if  selected_destination == "https://tinyurl.com/37feje7u":
            open_image("https://tinyurl.com/37feje7u")
            print("Rome is a place with good food and nice art")
        if selected_destination == "https://www.wendywutours.co.uk/blog/wp-content/uploads/2017/03/japanese-castle-sakura.jpg":
            open_images("https://www.wendywutours.co.uk/blog/wp-content/uploads/2017/03/japanese-castle-sakura.jpg")
            print("Japan is a place with rich history and very good views")
        if selected_destination == "https://tinyurl.com/59fhzf98":
            open_images("https://tinyurl.com/3rrbw8e8")
            print("Athens is a very rich and historical place with great views")
    if ans == "No":
        print("Thank you, Give us a 5 star on our review page")
        break


#Main
destination_List()
