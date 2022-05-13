from tkinter import *

import random

aantalBeurten = 0

print('Hallo! Hoe heet je?')
mijnNaam = input()

getal = random.randint(1, 20)
print('OK ' + mijnNaam + ', ik denk aan een getal tussen 1 en 20.')

while aantalBeurten < 6:
    print('Raad eens.') # Er staan vier spaties voor print.
    poging = input()
    poging = int(poging)

    aantalBeurten = aantalBeurten + 1

    if poging < getal:
        print('Je hebt te laag geraden.') # Er staan acht spaties voor print.

    if poging > getal:
        print('Je hebt te hoog geraden.')

    if poging == getal:
        break

    if poging == getal:
        aantalBeurten = str(aantalBeurten)
        print('Gaaf, ' + mijnNaam + '! Je hebt het getal geraden in ' + aantalBeurten + ' beurten!')

        if poging != getal:
            getal = str(getal)
            print('Jammer. Het getal waar ik aan dacht was ' + getal + '.')