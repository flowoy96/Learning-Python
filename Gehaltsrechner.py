print("Herlichen willkommen beim Gehaltsrechner.")

stundenlohn = int(input("Bitte gib Deinen Stundenlohn in € ein: "))
geschlecht = input("Bitte gib Dein Geschlecht an: ")
alter = int(input("Bitte gib Dein Alter an: "))

is_männlich = True
lebenserwartung_m = 79
lebenserwartung_f = 83

lebensende_m = lebenserwartung_m - alter
lebensende_f = lebenserwartung_f - alter

print("Dein Stundenlohn beträgt " + str(stundenlohn) + " €.")

if is_männlich:
    print("Du musst noch " + str(lebensende_m) + " Jahre arbeiten.")
else:
    print("Du musst noch " + str(lebensende_f) + " Jahre arbeiten.")

tageprojahr = 365
tag = 8 * stundenlohn
woche = 5 * tag
monat = 20 * tag
jahr = 12 * monat

print("Dein Stundenlohn pro Tag beträgt " + str(tag) + " €.")
print("Dein Stundenlohn pro Woche beträgt " + str(woche) + " €.")
print("Dein Stundenlohn pro Monat beträgt " + str(monat) + " €.")
print("Dein Stundenlohn pro Jahr beträgt " + str(jahr) + " €.")

if is_männlich:
    print("Mit diesem Stundenlohn würdest Du bis an Dein Lebensende " + str(lebensende_m * jahr) + " € verdienen.")
else:
    print("Mit diesem Stundenlohn würdest Du bis an Dein Lebensende " + str(lebensende_f * jahr) + " € verdienen.")

input("Drücke eine beliebige Taste, um das Programm zu schließen. ")