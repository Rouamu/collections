import random
from secrets import choice


kleuren = ['oranje','rood','geel','bruin']

def mms(aantal):
    zak = []
    for i in range(aantal): 
        zak.append(choice(kleuren))
    return zak
aantal= int(input('hoeveel mms wil je hebben?'))
x = mms(aantal)
print(x)




    