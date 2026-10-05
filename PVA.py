import random
cislo = random.randint(1, 100)

while True:    
    tip = input("hádej čislo 1-100: ")

    if not tip.isdigit():
        print("piš čísla!")
        continue

    tip = int(tip)

    if tip < cislo: 
        print("hádej vetší čislo")
    elif tip > cislo:
        print("hádej menší čislo")

    else:
        print("uhodl jsi!")
        break


