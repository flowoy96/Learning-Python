name = input("Bitte gib Deinen vollständigen Namen ein: ")
name_personal = input("Bitte gib den Namen der/des Ansprechpartner/in an: ")
age = input("Wie alt bist Du? ")
city = input("Woher kommst Du? ")
flat = input("Seit wann wohnst Du an der Adresse? ")

is_woman = True

if is_woman:
    print("Sehr geehrte Frau " + name_personal + ",")
else:
    print("Sehr geehrter Herr " + name_personal + ",")

print("mein Name ist " + name + ".")
print("Ich bin " + age + " Jahre alt")
print("und ich komme aus " + city + ". Ich wohne seit dem " + flat + " in einer eigenen Wohnung.")

input("Bitte beliebige Taste drücken...")