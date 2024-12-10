import random

array = []
for _ in range(10):
    random_cislo = random.randint(0, 100)
    array.append(random_cislo)

print("Pole:", array)

array1 = sorted(array)
print("Jednoduchý sort:", array1)


array3 = [10,54,575,45,4752,7,547862,8325785,47,42,47,12,4,4,2,4,2,1,4,5,54,654,1,35,465,43,51,6846,457]
#Funkce probublávání
def bubble_sort ():
    #Změření délky pole
    n = len(array3)
    #Tato smyčka prochází celé pole
    for i in range(n-1):
        #Tato smyčka prochází sousední prvky/čísla
        for j in range(0, n-i-1):
            #Porovnání a výměna prvků/čísel
            if array3[j] > array3[j+1]:
                array3[j+1], array3[j] = array3[j], array3[j+1]
                #Vypíše jednotlívý krok po přehození
                print(array3)
    return array3

print(bubble_sort())



array4 = [48,445,425,4245,245,2445,4855,4505,42445]            

#Pokud je prvek větší než následující
def is_sorted(array4):
    #Smyčka
    for i in range(len(array4) - 1):
        if array4[i] > array4[i + 1]:
            #Bude se opakovat
            return False
        #Ukončí program
    return True
#Přeházení pole
def bogo_sort(array4):
    #Pokud není srovnané pole
    while not is_sorted(array4):
        #Náhodně promíchat
        random.shuffle(array4)
    return array4




array5 = [64, 34, 25, 5, 22, 11, 90, 12, 87, 86, 822]
#Délka pole
n = len(array5)
#Tato smyčka prochází celé pole
for i in range(n-1):
    #Najde doslova nejmenší číslo
    min_index = i
    #Prochází celé pole
    for j in range(i+1, n):
        #Pokud minimum je větší jak číslo v poli
        if array5[j] < array5[min_index]:
            #Tak je prohodí
            min_index = j
            #Smaže poslední hodnotu nejmenší číslo
    min_value = array5.pop(min_index)
    #Vymění to číslo
    array5.insert(i, min_value)

print("Selection Sort:", array5)


array6 = [64, 34, 25, 12, 22, 11, 90]
# Délka pole
n = len(array6)
# Prochází pole a začínáme na druhém čísle, proto indexová hodnota 1
for i in range(1, n):
    # Uložíme si hodnotu, kterou chceme přesunout
    current_value = array6[i]
    # Najdeme místo kde ten prvek patří
    j = i - 1
    # Pokud jsou prvky menší jak current_value, tak je posouváme doprava
    while j >= 0 and array6[j] > current_value:
        # Posunutí prvku doprava
        array6[j + 1] = array6[j] 
        # Posuneme se k dalšímu prvku vlevo
        j = j - 1  
    # Vložíme current_value na správnou pozici
    array6[j + 1] = current_value

print("Insertion Sort:", array6)
