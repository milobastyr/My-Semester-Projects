#Milo","Bastyr

#Init
Dog_breeds=["Affenpinscher","AfghanHound","AiredaleTerrier","AkbashDog","Akita","AlapahaBlueBloodBulldog","AlaskanHusky","AlaskanMalamute","AmericanEskimoDog","AmericanFoxhound","AmericanPitBullTerrier","AmericanWaterSpaniel","AnatolianShepherdDog","AustralianKelpie","AustralianShepherd","Azawakh","Basenji","BassetBleudeGascogne","Beagle","Beauceron","BedlingtonTerrier","BelgianMalinois","BelgianTervuren","BerneseMountainDog","BlackandTanCoonhound","Bloodhound","BluetickCoonhound","Boerboel","BorderTerrier","BostonTerrier","BouvierdesFlandres","Boxer","BoykinSpaniel","BraccoItaliano","Briard","Brittany","Bullmastiff","CairnTerrier","CaneCorso","CardiganWelshCorgi","CatahoulaLeopardDog","CaucasianShepherd(Ovcharka)","CavalierKingCharlesSpaniel","ChineseCrested","Chinook","ChowChow","ClumberSpaniel","CockerSpaniel(American)","CotondeTulear","Dalmatian","DogoArgentino","EnglishShepherd","EnglishSpringerSpaniel","Eurasier","FieldSpaniel","FinnishLapphund","GermanPinscher","GermanShepherdDog","GermanShorthairedPointer","GiantSchnauzer","GlenofImaalTerrier","GoldenRetriever","GordonSetter","GreatDane","GreatPyrenees","Greyhound","Harrier","Havanese","IrishSetter","IrishWolfhound","ItalianGreyhound","JapaneseChin","Keeshond","Komondor","Kuvasz","LabradorRetriever","LagottoRomagnolo","Leonberger","LhasaApso","Maltese","MiniatureSchnauzer","Newfoundland","NorfolkTerrier","Papillon","PembrokeWelshCorgi","PharaohHound","Plott","Pug","RedboneCoonhound","RhodesianRidgeback","Rottweiler","Samoyed","Schipperke","ScottishDeerhound","ShihTzu","SilkyTerrier","SoftCoatedWheatenTerrier","SpanishWaterDog","Vizsla","Weimaraner"]
dog_min_weights=[6,50,40,90,65,55,38,65,20,65,30,25,80,31,35,33,22,35,20,80,17,40,40,65,65,80,45,110,12,10,70,50,25,55,70,30,100,13,88,25,50,80,13,10,50,40,55,20,9,50,80,44,35,40,35,33,25,50,45,65,32,55,45,110,85,50,40,7,35,105,7,4,35,80,70,55,24,120,12,4,11,100,11,3,25,40,40,14,45,75,75,50,10,70,9,8,30,30,50,55]
filtered_list=[]

#Functions


#Main

#Filter list by size of dogs
#Ask for input
print("What dog would you like")
print("Welcome to dog breed")
print("""1. weight of small dog
2.weights of medium dog
3.weights of large dog
4.Quit""")
option= int(input("(1-4)Select Option: "))
if option==1:
        def dog_weights():
            for i in range(0, len(dog_weights)):
                if dog_weights [i] <= 10:
                    filtered_list.append(dog_breeds[i])
        print(filtered_list)
if option==2:
        def dog_weights():
            for i in range(0, len(dog_weights)):
                if dog_weights [i] <= 25 and >11:
                    filtered_list.append(dog_breeds[i])
        print(filtered_list)
