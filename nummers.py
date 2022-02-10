list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8,10,12,14,16,18,20]

def addAndDisplayLists (list1, list2):
    for i in range(10):
       print(f'{list1[i]}+{list2[i]}={list1[i]+list2[i]}')

addAndDisplayLists(list1,list2)

def substractAndDisplayLists  (list1, list2):
    for i in range(10):
       print(f'{list1[i]}-{list2[i]}={list1[i]-list2[i]}')

substractAndDisplayLists (list1,list2)

def multiplyAndDisplayLists (list1, list2):  
    for i in range(10):
       print(f'{list1[i]}*{list2[i]}={list1[i]*list2[i]}')

multiplyAndDisplayLists (list1, list2)

def divideAndDisplayLists  (list1, list2):  
    for i in range(10):
       print(f'{list1[i]}/{list2[i]}={list1[i]/list2[i]}')

divideAndDisplayLists (list1, list2)

import random
def spelProgramma(spelList,min,max):
    spellen = []
    nummer = random.randint(min,max)
    for x in range(nummer):
        spellen.append(random.choice(spelList))
    return spellen
spellist =['Monopoly','Yathzee','Bridge','Poker','Pesten','Mens erger je niet','Cluedo']
list = spelProgramma(spellist,3,10)
print(list)

