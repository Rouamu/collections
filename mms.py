import random


kleuren = ['oranje','rood','geel','bruin']

def mms(aantal):
    zak = {
        'oranje':0,
        'rood':0,
        'geel':0,
        'bruin':0
    }
    for i in range(aantal): 
        kleur = random.choice(kleuren)
        zak[kleur] +=1
    return zak
aantal= int(input('hoeveel mms wil je hebben?'))
x = mms(aantal)
print(mms(aantal))




    