import os
import sys

portions = 6

rezept = int(input("[1] Pfannkuchen\n"
               "[2] Waffeln\n"
               "[3] Käsekuchen\n"
               "Bitte wähle eins der folgenden Rezepte aus: "))

if rezept == 1:
    print("Du hast das Rezept für Pfannkuchen gewählt.")
if rezept == 2:
    print("Du hast das Rezept für Waffeln gewählt.")
if rezept == 3:
    print("Du hast das Rezept für Käsekuchen gewählt.")
else:
    print("Fehlerhafte Eingabe. Bitte erneut versuchen." + os.execl(sys.executable, os.path.abspath(__file__), *sys.argv))

if rezept == 1:
    for pfannkuchen in ["\nDu benötigst:\n \n"
          "2 Eier,\n"
          "60 ml Mineralwasser, \n"
          "200 g Mehl, \n"
          "1 Prise Zucker, \n" 
          "1 Prise Salz, \n" 
          "200 ml Milch"]:
        print(pfannkuchen)

if rezept == 2:
    for waffeln in ["\nDu benötigst:\n\n"
          "3 Eier,\n"
          "125 g Butter,\n"
          "100 g Zucker, \n"
          "1 Packung Vanillezucker, \n"
          "250 g Mehl, \n"
          "1 Prise Salz, \n" 
          "1 TL Backpulver, \n" 
          "200 ml Milch"]:
        print(waffeln)

if rezept == 3:
    for käsekuchen in ["\nDu benötigst:\n\n"
          "1 Ei,\n"
          "75 g Zucker,\n"
          "75 g Margarine,\n"
          "200 g Mehl, \n"
          "1/2 Päckchen Backpulver"]:
        print(käsekuchen)